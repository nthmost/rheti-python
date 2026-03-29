import os
from datetime import datetime, timezone
from flask import (Blueprint, render_template, redirect, url_for,
                   session, request, flash, abort)
from flask_login import login_required, current_user
from . import db
from .models import Result, TestProgress

bp = Blueprint('test', __name__)

# --- Question loading with hot-reload ---

_questions_cache = None
_questions_mtime = None
_CSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'rheti', 'questions.csv')


def get_questions():
    """Load questions from CSV, reloading if the file has changed."""
    global _questions_cache, _questions_mtime
    try:
        mtime = os.path.getmtime(_CSV_PATH)
    except OSError:
        mtime = None

    if _questions_cache is None or mtime != _questions_mtime:
        import sys
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
        from rheti.loader import load_questions
        _questions_cache = load_questions(_CSV_PATH)
        _questions_mtime = mtime

    return _questions_cache


def _save_progress(answers, q_index):
    """Upsert the user's in-progress test state to the database."""
    prog = db.session.get(TestProgress, current_user.id) or \
           TestProgress.query.filter_by(user_id=current_user.id).first()
    if prog is None:
        prog = TestProgress(user_id=current_user.id)
        db.session.add(prog)
    prog.answers = answers
    prog.q_index = q_index
    prog.updated_at = datetime.now(timezone.utc)
    db.session.commit()


def _delete_progress():
    prog = TestProgress.query.filter_by(user_id=current_user.id).first()
    if prog:
        db.session.delete(prog)
        db.session.commit()


# --- Routes ---

@bp.route('/')
def index():
    if current_user.is_authenticated:
        questions = get_questions()
        progress = TestProgress.query.filter_by(user_id=current_user.id).first()
        return render_template('test/index.html',
                               n_questions=len(questions),
                               results=current_user.results[:3],
                               progress=progress)
    return render_template('test/landing.html')


@bp.route('/start', methods=['POST'])
@login_required
def start():
    """Begin a new test session, discarding any saved progress."""
    _delete_progress()
    session.clear()
    session['answers'] = []
    session['q_index'] = 0
    return redirect(url_for('test.question'))


@bp.route('/resume', methods=['POST'])
@login_required
def resume():
    """Restore a saved in-progress test into the session."""
    prog = TestProgress.query.filter_by(user_id=current_user.id).first()
    if not prog:
        return redirect(url_for('test.index'))
    session.clear()
    session['answers'] = prog.answers
    session['q_index'] = prog.q_index
    return redirect(url_for('test.question'))


@bp.route('/question', methods=['GET', 'POST'])
@login_required
def question():
    questions = get_questions()
    idx = session.get('q_index', 0)
    answers = session.get('answers', [])

    if idx >= len(questions):
        return redirect(url_for('test.finish'))

    q = questions[idx]

    if request.method == 'POST':
        choice_code = request.form.get('choice')
        if choice_code not in [c.code for c in q.choices]:
            flash('Please select a or b.', 'error')
            return redirect(url_for('test.question'))

        chosen = next(c for c in q.choices if c.code == choice_code)
        answers.append({'q': q.qnum, 'choice': choice_code, 'value': chosen.value})
        session['answers'] = answers
        session['q_index'] = idx + 1

        # Persist progress to DB every 5 questions
        if (idx + 1) % 5 == 0:
            _save_progress(answers, idx + 1)

        return redirect(url_for('test.question'))

    return render_template('test/question.html',
                           question=q,
                           index=idx,
                           total=len(questions),
                           pct=int(idx / len(questions) * 100))


@bp.route('/finish')
@login_required
def finish():
    answers = session.get('answers', [])
    if not answers:
        return redirect(url_for('test.index'))

    from rheti.scorer import score
    values = [a['value'] for a in answers]
    result_data = score(values)

    result = Result(
        user_id=current_user.id,
        top_type=result_data['top_type'],
        scores={str(t): c for t, c in result_data['counts'].items()},
        answers=answers,
        n_questions=len(answers),
        completed_at=datetime.now(timezone.utc),
    )
    db.session.add(result)
    _delete_progress()
    db.session.commit()

    session.clear()
    return redirect(url_for('test.results', result_id=result.id))


@bp.route('/types')
def types():
    from rheti.scorer import TYPE_DESCRIPTIONS
    from rheti.types import TYPE_NAMES
    types = [(n, TYPE_NAMES[n], TYPE_DESCRIPTIONS[n]) for n in range(1, 10)]
    return render_template('test/types.html', types=types)


@bp.route('/types/<int:type_num>')
def type_detail(type_num):
    if type_num not in range(1, 10):
        abort(404)
    from rheti.scorer import TYPE_DESCRIPTIONS
    from rheti.types import (TYPE_NAMES, TYPE_CENTER, CENTERS, ARROWS,
                              STRESS_DESC, GROWTH_DESC, WINGS, WING_DETAIL, LEVELS, FAMOUS)
    center_key = TYPE_CENTER[type_num]
    arrows = ARROWS[type_num]
    prev_type = type_num - 1 if type_num > 1 else 9
    next_type = type_num + 1 if type_num < 9 else 1
    return render_template('test/type_detail.html',
                           num=type_num,
                           name=TYPE_NAMES[type_num],
                           description=TYPE_DESCRIPTIONS[type_num],
                           center=CENTERS[center_key],
                           wings=WINGS[type_num],
                           wing_detail=WING_DETAIL[type_num],
                           stress_type=arrows['stress'],
                           stress_name=TYPE_NAMES[arrows['stress']],
                           stress_desc=STRESS_DESC[type_num],
                           growth_type=arrows['growth'],
                           growth_name=TYPE_NAMES[arrows['growth']],
                           growth_desc=GROWTH_DESC[type_num],
                           levels=LEVELS[type_num],
                           famous=FAMOUS[type_num],
                           prev_type=prev_type,
                           next_type=next_type,
                           TYPE_NAMES=TYPE_NAMES)


@bp.route('/results/<int:result_id>')
@login_required
def results(result_id):
    result = db.session.get(Result, result_id)
    if not result or result.user_id != current_user.id:
        abort(404)

    from rheti.scorer import TYPE_MAP, TYPE_DESCRIPTIONS
    from rheti.types import TYPE_NAMES, WING_DETAIL
    ranking = sorted(
        [(int(t), c) for t, c in result.scores.items()],
        key=lambda x: -x[1]
    )
    top_type = result.top_type
    top_name = TYPE_MAP[[k for k,v in TYPE_MAP.items() if v[0]==top_type][0]][1]

    # Probable wing: whichever adjacent type scored higher
    scores = {int(t): c for t, c in result.scores.items()}
    adj = [top_type - 1 if top_type > 1 else 9,
           top_type + 1 if top_type < 9 else 1]
    wing_type = max(adj, key=lambda t: scores.get(t, 0))
    wing_code = f'{top_type}w{wing_type}'
    wing_info = WING_DETAIL[top_type].get(wing_code)

    return render_template('test/results.html',
                           result=result,
                           ranking=ranking,
                           top_type=top_type,
                           top_name=top_name,
                           description=TYPE_DESCRIPTIONS[top_type],
                           TYPE_MAP=TYPE_MAP,
                           TYPE_NAMES=TYPE_NAMES,
                           wing_type=wing_type,
                           wing_code=wing_code,
                           wing_info=wing_info,
                           adj_scores={t: scores.get(t, 0) for t in adj})
