"""
Detailed Enneagram type theory content.
All data is based on the Riso-Hudson model.
"""

# Centers of intelligence
CENTERS = {
    'body':  {'name': 'Body / Instinctive Center', 'types': [8, 9, 1],
              'desc': 'These types lead with gut instinct and tend to relate to the world through action, '
                      'autonomy, and control. Their core emotional issue is anger or rage.'},
    'heart': {'name': 'Heart / Feeling Center',    'types': [2, 3, 4],
              'desc': 'These types lead with emotion and tend to orient around image, identity, and '
                      'connection. Their core emotional issue is shame.'},
    'head':  {'name': 'Head / Thinking Center',    'types': [5, 6, 7],
              'desc': 'These types lead with analysis and tend to orient around safety, planning, and '
                      'mental frameworks. Their core emotional issue is fear or anxiety.'},
}

TYPE_CENTER = {1: 'body', 2: 'heart', 3: 'heart', 4: 'heart',
               5: 'head',  6: 'head',  7: 'head',  8: 'body', 9: 'body'}

# Stress (disintegration) and growth (integration) arrows
ARROWS = {
    1: {'stress': 4, 'growth': 7},
    2: {'stress': 8, 'growth': 4},
    3: {'stress': 9, 'growth': 6},
    4: {'stress': 2, 'growth': 1},
    5: {'stress': 7, 'growth': 8},
    6: {'stress': 3, 'growth': 9},
    7: {'stress': 1, 'growth': 5},
    8: {'stress': 5, 'growth': 2},
    9: {'stress': 6, 'growth': 3},
}

STRESS_DESC = {
    1: "Under significant stress, Ones take on the less healthy traits of Type 4 — becoming moody, "
       "withdrawn, and self-critical in a more emotional and dramatic way. They may feel that they "
       "are fundamentally flawed, and their usual rational control gives way to dark introspection.",
    2: "Under stress, Twos move toward Type 8 — becoming aggressive, controlling, and domineering. "
       "The warm helper suddenly asserts themselves forcefully, often surprising those around them. "
       "This is often a backlash from years of unacknowledged personal needs.",
    3: "Under stress, Threes move toward Type 9 — becoming disengaged, listless, and apathetic. "
       "The usually driven achiever loses motivation, withdraws from competition, and may numb out "
       "or dissociate from both work and relationships.",
    4: "Under stress, Fours move toward Type 2 — becoming clingy, possessive, and people-pleasing. "
       "The ordinarily self-reliant individualist starts seeking external validation and may become "
       "over-involved in others' lives to fill their sense of inner emptiness.",
    5: "Under stress, Fives move toward Type 7 — becoming scattered, hyperactive, and impulsive. "
       "The normally quiet observer starts spinning through ideas and distractions, unable to focus, "
       "seeking stimulation to escape feelings of inadequacy or overwhelm.",
    6: "Under stress, Sixes move toward Type 3 — becoming competitive, image-conscious, and "
       "driven in an anxious, workaholic way. They may perform confidence they don't feel, or "
       "project an air of competence to mask deep underlying insecurity.",
    7: "Under stress, Sevens move toward Type 1 — becoming critical, perfectionistic, and rigid. "
       "The usually fun-loving enthusiast turns judgmental and impatient, fixating on what's wrong "
       "rather than what's possible, and may become harsh with themselves or others.",
    8: "Under stress, Eights move toward Type 5 — becoming withdrawn, secretive, and isolated. "
       "The usually forceful challenger retreats, cuts off emotionally, and may become paranoid "
       "or detached, processing threats internally rather than confronting them directly.",
    9: "Under stress, Nines move toward Type 6 — becoming anxious, worried, and reactive. "
       "The normally placid peacemaker starts catastrophizing, seeking reassurance, and may "
       "oscillate between compliance and sudden spikes of fearful defensiveness.",
}

GROWTH_DESC = {
    1: "In growth, Ones take on the healthy qualities of Type 7 — becoming more spontaneous, "
       "joyful, and generous in spirit. They relax their inner critic, appreciate the present "
       "moment, and find freedom in accepting that imperfection is part of life.",
    2: "In growth, Twos take on the healthy qualities of Type 4 — becoming more introspective, "
       "emotionally honest, and self-aware. They learn to acknowledge and express their own needs "
       "directly rather than through helping, and develop a richer inner life.",
    3: "In growth, Threes take on the healthy qualities of Type 6 — becoming more cooperative, "
       "loyal, and genuinely committed to others. They shift from self-promotion to real "
       "collaboration, and find that authentic connection matters more than status.",
    4: "In growth, Fours take on the healthy qualities of Type 1 — becoming more principled, "
       "objective, and self-disciplined. They channel their emotional depth into purposeful action "
       "and learn that meaning is built as much as it is felt.",
    5: "In growth, Fives take on the healthy qualities of Type 8 — becoming more assertive, "
       "confident, and willing to act in the world. They step out of observation mode and "
       "into engagement, trusting their knowledge and advocating for themselves.",
    6: "In growth, Sixes take on the healthy qualities of Type 9 — becoming more grounded, "
       "relaxed, and genuinely trusting. Their anxiety quiets as they find inner stability "
       "rather than seeking it from external authority or certainty.",
    7: "In growth, Sevens take on the healthy qualities of Type 5 — becoming more focused, "
       "thoughtful, and present. They stop running from discomfort and discover that depth "
       "and commitment offer a satisfaction that constant novelty never could.",
    8: "In growth, Eights take on the healthy qualities of Type 2 — becoming more open-hearted, "
       "nurturing, and willing to be vulnerable. Their protective instinct becomes genuine "
       "care, and they discover that real strength includes tenderness.",
    9: "In growth, Nines take on the healthy qualities of Type 3 — becoming more self-assured, "
       "motivated, and productive. They stop merging with others' agendas and step into "
       "their own goals, finding that their presence and contribution genuinely matter.",
}

WINGS = {
    1: {
        '1w9': ('The Idealist', 'A quieter, more detached One — philosophical and principled, '
                'often drawn to academia, law, or reform movements. Less outwardly critical '
                'but deeply inner-directed. The Nine wing softens the reforming edge.'),
        '1w2': ('The Advocate', 'A warmer, more interpersonally engaged One — driven to improve '
                'the world through helping people directly. More openly critical and more '
                'emotionally expressive than the 1w9. The Two wing adds empathy and drive.'),
    },
    2: {
        '2w1': ('The Servant', 'A more principled, reserved Two — guided by a strong moral sense '
                'alongside their caring impulse. Less overtly demonstrative, more likely to help '
                'quietly and according to principle.'),
        '2w3': ('The Host', 'A more outgoing, ambitious Two — charming, socially savvy, and '
                'motivated to be seen as both caring and successful. More image-conscious '
                'than the 2w1, thriving in social and professional roles.'),
    },
    3: {
        '3w2': ('The Charmer', 'A more socially oriented Three — warm, relationship-focused, '
                'and driven to be both successful and well-liked. The Two wing adds genuine '
                'interpersonal warmth to the Achiever\'s drive.'),
        '3w4': ('The Professional', 'A more introspective, image-conscious Three — drawn to '
                'craft, depth, and distinctive identity alongside achievement. The Four wing '
                'adds emotional complexity and a desire for authenticity.'),
    },
    4: {
        '4w3': ('The Aristocrat', 'A more outwardly expressive, ambitious Four — concerned '
                'with aesthetics and recognition, often drawn to performance or public creative '
                'work. The Three wing adds drive and image-awareness.'),
        '4w5': ('The Bohemian', 'A more withdrawn, intellectual Four — deeply inner-directed, '
                'eccentric, and original. Less concerned with recognition, more interested in '
                'understanding. The Five wing adds analytical depth and introversion.'),
    },
    5: {
        '5w4': ('The Iconoclast', 'A more emotionally attuned, creative Five — drawn to art, '
                'literature, and unconventional ideas alongside analytical pursuits. The Four '
                'wing adds sensitivity and individualism.'),
        '5w6': ('The Problem Solver', 'A more systematic, security-oriented Five — skilled at '
                'building reliable mental frameworks and working within structures. The Six '
                'wing adds loyalty, thoroughness, and a focus on practical application.'),
    },
    6: {
        '6w5': ('The Defender', 'A more introverted, intellectual Six — analytical and '
                'self-reliant, building security through knowledge and preparation. Less '
                'outwardly social, more focused on mastering information and systems.'),
        '6w7': ('The Buddy', 'A more outgoing, optimistic Six — warm, playful, and '
                'relationship-oriented, though still attentive to risk. The Seven wing '
                'lightens anxiety and adds enthusiasm for experience.'),
    },
    7: {
        '7w6': ('The Entertainer', 'A more loyal, relationship-focused Seven — warm, '
                'funny, and genuinely committed to the people in their life. The Six '
                'wing adds a layer of responsibility and interpersonal anxiety.'),
        '7w8': ('The Realist', 'A more assertive, materialistic Seven — driven, outspoken, '
                'and focused on making things happen. The Eight wing adds confidence, '
                'willpower, and a certain bluntness.'),
    },
    8: {
        '8w7': ('The Maverick', 'A more extroverted, enterprising Eight — high-energy, '
                'strategic, and driven to build and expand. The Seven wing adds optimism '
                'and a love of bold new ventures.'),
        '8w9': ('The Bear', 'A more steady, receptive Eight — powerful but calm, protective '
                'rather than aggressive. The Nine wing adds patience and a surprisingly '
                'gentle quality beneath the strength.'),
    },
    9: {
        '9w8': ('The Referee', 'A more assertive, self-confident Nine — grounded and '
                'occasionally forceful, able to stand firm when pushed. The Eight wing '
                'adds directness and a willingness to confront.'),
        '9w1': ('The Dreamer', 'A more principled, idealistic Nine — quietly motivated '
                'by deep values, drawn to harmony and improvement. The One wing adds '
                'conscientiousness and a gentle reforming impulse.'),
    },
}

LEVELS = {
    1: {
        'healthy':   'Wise, discerning, and realistic — accepting of imperfection in themselves '
                     'and others. Deeply principled yet flexible. Inspiring and morally courageous.',
        'average':   'Orderly, responsible, and rule-bound. Frequently critical of others and '
                     'perfectionistic. Can be preachy, rigid, and self-righteous.',
        'unhealthy': 'Obsessive and intolerant. May become punitive, harsh, and unable to function '
                     'without everything being "right." At the extreme, prone to complete breakdown.',
    },
    2: {
        'healthy':   'Genuinely altruistic and unconditionally loving. Emotionally attuned and '
                     'empathically gifted. Can give freely without needing to be needed.',
        'average':   'Helpful but also manipulative — giving in order to be loved. Prone to '
                     'flattery, possessiveness, and martyrdom when their efforts go unacknowledged.',
        'unhealthy': 'Coercive and guilt-inducing. May become physically or emotionally unwell '
                     'as a means of holding onto relationships. Deeply resentful underneath.',
    },
    3: {
        'healthy':   'Authentic, inspiring, and genuinely accomplished. Motivates others not '
                     'through image but through real competence and hard-won achievement.',
        'average':   'Highly efficient but image-driven. May shade truth or cut ethical corners '
                     'to maintain the appearance of success. Emotionally out of touch.',
        'unhealthy': 'Deceptive and exploitative. May falsify accomplishments or sabotage others. '
                     'Completely identified with persona, having lost touch with any inner life.',
    },
    4: {
        'healthy':   'Profoundly creative and emotionally honest. Deeply empathic. Able to transform '
                     'personal suffering into universal art or insight.',
        'average':   'Temperamental, self-absorbed, and prone to melancholy. May romanticize '
                     'suffering and push others away while longing for connection.',
        'unhealthy': 'Self-destructive and alienated. Tormented by shame and envy. May withdraw '
                     'completely or act out dramatically in ways that damage relationships.',
    },
    5: {
        'healthy':   'Visionary and profoundly insightful. Open-minded and genuinely innovative. '
                     'Able to synthesize complex knowledge and share it meaningfully.',
        'average':   'Detached and overly analytical. Hoards time, energy, and knowledge. '
                     'Can be condescending, eccentric, and emotionally unavailable.',
        'unhealthy': 'Isolated and paranoid. May reject all human contact and live entirely '
                     'in a private mental world. Prone to nihilism and bizarre thinking.',
    },
    6: {
        'healthy':   'Genuinely courageous and deeply loyal. Finds real security through '
                     'inner conviction rather than external authority. Warm and committed.',
        'average':   'Anxious and indecisive, or contrarily defiant and suspicious. Seeks '
                     'reassurance constantly. May oscillate between submission and rebellion.',
        'unhealthy': 'Paranoid and self-defeating. May lash out preemptively or freeze '
                     'completely. Prone to self-sabotage just when success is in reach.',
    },
    7: {
        'healthy':   'Joyful, accomplished, and deeply present. Able to commit and find profound '
                     'satisfaction. Brings genuine creativity and enthusiasm to everything.',
        'average':   'Scattered and impulsive. Avoids pain through constant stimulation. '
                     'May be charming but unreliable, perpetually chasing the next experience.',
        'unhealthy': 'Addicted to sensation and increasingly reckless. Escapism turns harmful. '
                     'Prone to substance abuse, mania, or complete dissipation of potential.',
    },
    8: {
        'healthy':   'Magnanimous, heroic, and genuinely protective. Uses strength in service '
                     'of others. Able to be vulnerable and deeply loyal.',
        'average':   'Domineering and confrontational. Needs to feel in control at all times. '
                     'Can be intimidating, insensitive to others\' feelings, and vengeful.',
        'unhealthy': 'Ruthless and destructive. May become tyrannical, pursuing power and '
                     'revenge with no regard for others. Prone to violence or criminality.',
    },
    9: {
        'healthy':   'Deeply stable and serene. Brings people together with genuine equanimity. '
                     'Fully present and engaged — their support feels solid and unconditional.',
        'average':   'Conflict-avoidant and complacent. Numbs out through routines and '
                     'distractions. May appear easygoing while internally checked out.',
        'unhealthy': 'Completely dissociated. Unable to act or make decisions. May become '
                     'deeply neglectful of themselves and their responsibilities.',
    },
}

FAMOUS = {
    1: ['Mahatma Gandhi', 'Nelson Mandela', 'Hillary Clinton', 'Confucius', 'Martha Stewart'],
    2: ['Desmond Tutu', 'Mother Teresa', 'Dolly Parton', 'Princess Diana', 'Leo Tolstoy'],
    3: ['Oprah Winfrey', 'Tony Robbins', 'Muhammad Ali', 'Taylor Swift', 'Bill Clinton'],
    4: ['Frida Kahlo', 'Bob Dylan', 'Billie Eilish', 'Fyodor Dostoevsky', 'Virginia Woolf'],
    5: ['Albert Einstein', 'Stephen Hawking', 'Tim Burton', 'Emily Dickinson', 'Bill Gates'],
    6: ['Tom Hanks', 'Ellen DeGeneres', 'Sigmund Freud', 'Malala Yousafzai', 'J.R.R. Tolkien'],
    7: ['Robin Williams', 'Elton John', 'Amelia Earhart', 'Jim Carrey', 'Mozart'],
    8: ['Winston Churchill', 'Serena Williams', 'Martin Luther King Jr.', 'Ernest Hemingway', 'Toni Morrison'],
    9: ['Barack Obama', 'Carl Jung', 'Fred Rogers', 'Audrey Hepburn', 'Walt Disney'],
}

TYPE_NAMES = {
    1: 'The Reformer',    2: 'The Helper',       3: 'The Achiever',
    4: 'The Individualist', 5: 'The Investigator', 6: 'The Loyalist',
    7: 'The Enthusiast',  8: 'The Challenger',   9: 'The Peacemaker',
}
