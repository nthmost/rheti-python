import csv
import os
from collections import defaultdict
from .question import Question, Choice

QUESTIONS_CSV = os.path.join(os.path.dirname(__file__), 'questions.csv')


def load_questions(path=None):
    """Load questions from CSV and return an ordered list of Question objects."""
    path = path or QUESTIONS_CSV
    rows = defaultdict(list)
    order = []

    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qnum = row['question']
            if qnum not in rows:
                order.append(qnum)
            rows[qnum].append(Choice(
                text=row['text'],
                code=row['choice'],
                value=row['value'],
            ))

    questions = []
    for qnum in order:
        questions.append(Question(qnum=qnum, choices=rows[qnum]))
    return questions
