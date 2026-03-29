# rheti-python

A full implementation of the RHETI (Riso-Hudson Enneagram Type Indicator) v2.5 personality test — 144 questions, scored and explained.

**Live site:** [rheti.nthmost.com](https://rheti.nthmost.com)

---

## What it does

The RHETI is a forced-choice personality test that scores across all nine Enneagram types. Unlike many online Enneagram quizzes, it doesn't ask you to rate adjectives — it asks you to choose between two statements that feel true about you. The result is a ranked breakdown of all nine types, not just a single label.

This implementation includes:

- **144-question test** with session persistence (resume if you close the browser)
- **Type profiles** for all 9 types with wing variants, stress/growth arrows, levels of development, and notable examples
- **Probable wing detection** computed from your adjacent type scores
- **Motivation & Stress follow-ups** — short differentiator mini-tests for close-scoring type pairs, so you can dig into what distinguishes similar types by what *drives* you rather than what you *do*
- **Wing identification** — separate follow-ups when your two adjacent type scores are close, phrased as "8w7 or 8w9?" rather than re-deciding your type
- **Answer review** — revisit and adjust individual answers without retaking the full test; scores recalculate immediately
- **Tie handling** — when two types score equally, you can self-identify and compare stress/growth context for both

---

## Tech stack

| Layer | Tool |
|-------|------|
| Web framework | Flask + Flask-Login + Flask-Mail |
| Database | SQLite (SQLAlchemy ORM) |
| Auth | Email + password with verification |
| Frontend | Jinja2 templates, vanilla CSS |
| Server | gunicorn + Apache reverse proxy (Debian) |
| Python | 3.11+ |

---

## Project structure

```
rheti/
  __init__.py          # Public API: load_questions(), score()
  __main__.py          # CLI test runner
  loader.py            # CSV → Question objects
  scorer.py            # Type scoring, descriptions, TYPE_MAP
  question.py          # Question / Choice dataclasses
  types.py             # Wing detail, stress/growth arrows, levels, centers
  differentiators.py   # Motivation & stress question pairs (10 type pairs)
  questions.csv        # 144 questions — reloaded on file change (no restart needed)

web/
  __init__.py          # Flask app factory
  models.py            # User, Result, TestProgress (SQLAlchemy)
  test.py              # All test routes (blueprint)
  auth.py              # Login / register / verify routes
  templates/
    base.html
    test/
      landing.html     # Public landing page
      index.html       # Authenticated dashboard (resume/start)
      question.html    # Single question view
      results.html     # Full results with wing, scores, differentiator CTAs
      type_detail.html # Per-type profile page (public)
      types.html       # All 9 types listing (public)
      differentiate.html  # Motivation & stress / wing mini-test
      review.html      # Answer review & adjust
  static/css/style.css
```

---

## Running locally

```bash
# Install dependencies
pip install -e .

# Create the database
flask --app web shell -c "from web import db; db.create_all()"

# Start the dev server
flask --app web run
```

The app will be at `http://localhost:5000`. The questions CSV is hot-reloaded on change — edit `rheti/questions.csv` and refresh without restarting.

For email verification to work locally, set these environment variables (or use a `.env` file):

```bash
MAIL_SERVER=your.smtp.host
MAIL_PORT=587
MAIL_USERNAME=you@example.com
MAIL_PASSWORD=yourpassword
MAIL_DEFAULT_SENDER=you@example.com
```

You can skip verification entirely in development by manually setting `user.email_verified = True` in the shell.

---

## CLI usage

The core scoring logic works standalone without the web app:

```bash
rheti
# or
python -m rheti
```

Answer each question with `a` or `b`. At the end you'll see a ranked breakdown of all nine Enneagram types and your dominant type.

---

## Python API

```python
from rheti import load_questions, score

questions = load_questions()           # list of Question objects
answers = ['E', 'A', 'C', ...]        # one value per question (A–I)
result = score(answers)

print(result['top_type'])             # e.g. 4
print(result['top_name'])             # e.g. 'The Individualist'
print(result['ranking'])              # all 9 types sorted by score
print(result['tied_types'])           # list of types that tied for top score
```

### Value → type mapping

| Letter | Type | Name |
|--------|------|------|
| A | 9 | The Peacemaker |
| B | 6 | The Loyalist |
| C | 3 | The Achiever |
| D | 1 | The Reformer |
| E | 4 | The Individualist |
| F | 2 | The Helper |
| G | 8 | The Challenger |
| H | 5 | The Investigator |
| I | 7 | The Enthusiast |

---

## Question data

`rheti/questions.csv` is the source of truth. Each question has two rows:

```
question,choice,text,value
q1,a,"I've been romantic and imaginative",E
q1,b,"I've been pragmatic and down to earth",B
```

The full 144-question set is included. Questions q1–q23 are verified ground truth; q24–q144 were recovered from the original PDF via OCR and vision LLM review (~91% accuracy). Questions q51, q69, q71, q76, q77 have uncertain column assignments due to a score-sheet overlay on page 10 of the source PDF.

---

## Differentiator pairs

`rheti/differentiators.py` contains motivation & stress question sets for 10 common type pairs:

`(1,2)` `(1,8)` `(1,9)` `(2,3)` `(3,4)` `(4,5)` `(5,6)` `(6,7)` `(7,8)` `(8,9)`

Each pair has 6 questions with two options keyed to the type numbers. The differentiator for a pair is shown on the results page when both types are present in the user's top scores, and used for wing identification when the pair is adjacent to the user's top type.

---

## Deployment

```bash
./deploy.sh   # git push → pull on zephyr → pip install → systemctl restart
```

The server runs gunicorn behind Apache with a `ProxyPass` to `localhost:8000`. The SQLite database lives at `web/rheti.db`.

---

## License

MIT
