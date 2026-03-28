import sys
import textwrap
from .loader import load_questions
from .scorer import score, TYPE_MAP


BANNER = """
╔══════════════════════════════════════════════════════════╗
║           RHETI — Riso-Hudson Enneagram Type             ║
║                     Indicator (v2.5)                     ║
╚══════════════════════════════════════════════════════════╝

For each question, choose the statement that best describes
you over the past year. Answer honestly — there are no right
or wrong answers.

Enter 'a' or 'b' at each prompt. Type 'q' to quit.
"""


def prompt_question(idx, total, question):
    """Display a question and return the chosen type-letter value."""
    print(f"\n─── Question {idx} of {total} ───")
    choices = {c.code: c for c in question.choices}

    for code in sorted(choices):
        wrapped = textwrap.fill(choices[code].text, width=70, initial_indent='    ',
                                subsequent_indent='       ')
        print(f"  {code})  {wrapped.lstrip()}")

    while True:
        raw = input("\nYour choice (a/b): ").strip().lower()
        if raw == 'q':
            print("\nQuitting. Goodbye.")
            sys.exit(0)
        if raw in choices:
            return choices[raw].value
        print("Please enter 'a' or 'b'.")


def show_results(results, total):
    print("\n" + "═" * 60)
    print("  RESULTS")
    print("═" * 60)

    for type_num, name, count in results['ranking']:
        bar = '█' * count + '░' * (total - count)
        pct = count / total * 100 if total else 0
        print(f"  Type {type_num:1d} {name:<22s}  {count:3d}  ({pct:4.1f}%)  {bar}")

    print()
    print(f"  Your dominant type: Type {results['top_type']} — {results['top_name']}")
    print()
    print("  " + results['description'])
    print("═" * 60)


def main():
    print(BANNER)
    questions = load_questions()
    total = len(questions)
    answers = []

    for i, question in enumerate(questions, start=1):
        value = prompt_question(i, total, question)
        answers.append(value)

    results = score(answers)
    show_results(results, total)


if __name__ == '__main__':
    main()
