from collections import Counter

# Maps the single-letter codes in the CSV to Enneagram type numbers and names
TYPE_MAP = {
    'A': (9, 'The Peacemaker'),
    'B': (6, 'The Loyalist'),
    'C': (3, 'The Achiever'),
    'D': (1, 'The Reformer'),
    'E': (4, 'The Individualist'),
    'F': (2, 'The Helper'),
    'G': (8, 'The Challenger'),
    'H': (5, 'The Investigator'),
    'I': (7, 'The Enthusiast'),
}

TYPE_DESCRIPTIONS = {
    1: "Type 1 — The Reformer: Principled, purposeful, self-controlled, and perfectionistic.",
    2: "Type 2 — The Helper: Generous, demonstrative, people-pleasing, and possessive.",
    3: "Type 3 — The Achiever: Adaptable, excelling, driven, and image-conscious.",
    4: "Type 4 — The Individualist: Expressive, dramatic, self-absorbed, and temperamental.",
    5: "Type 5 — The Investigator: Perceptive, innovative, secretive, and isolated.",
    6: "Type 6 — The Loyalist: Engaging, responsible, anxious, and suspicious.",
    7: "Type 7 — The Enthusiast: Spontaneous, versatile, acquisitive, and scattered.",
    8: "Type 8 — The Challenger: Self-confident, decisive, willful, and confrontational.",
    9: "Type 9 — The Peacemaker: Receptive, reassuring, complacent, and resigned.",
}


def score(answers):
    """
    Score the test.

    answers: list of type-letter strings (e.g. ['A', 'G', 'E', ...])

    Returns a dict with:
      - 'counts': Counter mapping type number -> count
      - 'top_type': the winning type number
      - 'top_name': e.g. 'The Peacemaker'
      - 'description': one-line description of the top type
      - 'ranking': list of (type_num, name, count) sorted by count desc
    """
    type_counts = Counter()
    for letter in answers:
        if letter in TYPE_MAP:
            type_num, _ = TYPE_MAP[letter]
            type_counts[type_num] += 1

    ranking = sorted(
        [(num, TYPE_MAP[l][1], type_counts[num]) for l, (num, _) in TYPE_MAP.items()],
        key=lambda x: (-x[2], x[0])
    )

    top_type, top_name, top_count = ranking[0]

    return {
        'counts': type_counts,
        'top_type': top_type,
        'top_name': top_name,
        'description': TYPE_DESCRIPTIONS[top_type],
        'ranking': ranking,
    }
