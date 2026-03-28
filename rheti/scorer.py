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
    1: (
        "Ones are principled, purposeful, and self-disciplined — driven by a deep desire to be good "
        "and to improve the world around them. They have a strong inner critic that holds them to high "
        "standards, making them reliable, thorough, and fair. At their best, Ones are wise, discerning, "
        "and inspiring — accepting of themselves and others. Under stress, they can become rigid, "
        "critical, and perfectionistic, struggling to let go of the sense that things are not as they "
        "should be. Their core desire is integrity; their core fear is being corrupt or defective."
    ),
    2: (
        "Twos are warm, caring, and interpersonally attuned — motivated by a genuine desire to be loved "
        "and to feel needed by others. They are often the first to sense what people around them need and "
        "to offer support, sometimes before being asked. At their best, Twos are unconditionally loving, "
        "generous, and deeply nurturing. Under stress, they can become possessive, people-pleasing, or "
        "resentful when their own needs go unmet. Their core desire is to be loved and appreciated; "
        "their core fear is being unwanted or unworthy of love."
    ),
    3: (
        "Threes are ambitious, adaptable, and image-conscious — oriented toward achievement and the "
        "recognition that comes with it. They excel at reading what success looks like in any environment "
        "and shaping themselves accordingly. At their best, Threes are authentic, inspiring leaders who "
        "motivate others through their own hard work and genuine accomplishment. Under stress, they can "
        "become overly focused on appearances, cutting corners, or losing touch with who they really are. "
        "Their core desire is to feel valuable and worthwhile; their core fear is being worthless or a failure."
    ),
    4: (
        "Fours are expressive, sensitive, and deeply in touch with their inner emotional world. They long "
        "to understand themselves and to be understood — to find meaning and authenticity in their lives. "
        "Creative and empathic, they often feel a sense of longing or of something essential being missing. "
        "At their best, Fours are profoundly creative, compassionate, and emotionally honest. Under stress, "
        "they can become self-absorbed, melancholic, or envious of what others seem to have. Their core "
        "desire is to find their identity and significance; their core fear is having no identity or personal meaning."
    ),
    5: (
        "Fives are perceptive, analytical, and intensely private — motivated by the desire to understand "
        "the world deeply and to conserve their inner resources. They tend to observe more than participate, "
        "preferring to master a subject fully before engaging. At their best, Fives are visionary, "
        "open-minded, and groundbreaking thinkers. Under stress, they can become isolated, withholding, "
        "or detached — retreating into their minds when overwhelmed. Their core desire is to be capable "
        "and competent; their core fear is being useless, incompetent, or incapable."
    ),
    6: (
        "Sixes are responsible, committed, and security-oriented — attuned to risk and to the trustworthiness "
        "of people and institutions around them. They are loyal to those they trust and hardworking within "
        "systems they believe in. At their best, Sixes are courageous, reliable, and deeply devoted — "
        "finding genuine courage by moving through their fears. Under stress, they can become anxious, "
        "suspicious, or caught between self-doubt and defiance. Their core desire is security and support; "
        "their core fear is being without guidance, support, or the ability to survive."
    ),
    7: (
        "Sevens are enthusiastic, spontaneous, and future-oriented — propelled by a desire for new "
        "experiences, ideas, and possibilities. They bring energy and optimism to almost everything they "
        "do, and can synthesize diverse ideas with remarkable creativity. At their best, Sevens are joyful, "
        "accomplished, and deeply grateful — present enough to find satisfaction in what they have. Under "
        "stress, they scatter their energy across too many pursuits, avoiding pain or boredom through "
        "constant stimulation. Their core desire is to be happy and satisfied; their core fear is being "
        "deprived or in pain."
    ),
    8: (
        "Eights are powerful, self-confident, and direct — motivated by a need to be in control of their "
        "own lives and to resist any form of weakness or domination. They engage the world with intensity "
        "and decisiveness, often naturally taking charge of situations. At their best, Eights are "
        "magnanimous, heroic, and protective of those they care about. Under stress, they can become "
        "domineering, confrontational, or unwilling to show vulnerability. Their core desire is to protect "
        "themselves and others; their core fear is being controlled, harmed, or violated by others."
    ),
    9: (
        "Nines are receptive, easygoing, and peace-seeking — motivated by a deep desire for harmony and "
        "a reluctance to assert themselves in ways that might cause conflict. They have a remarkable "
        "ability to see all sides of a situation and to make others feel heard and accepted. At their best, "
        "Nines are deeply stable, serene, and unifying — bringing people together with genuine equanimity. "
        "Under stress, they can become complacent, conflict-avoidant, or disconnected from their own "
        "desires and priorities. Their core desire is inner peace and wholeness; their core fear is loss "
        "and separation."
    ),
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
