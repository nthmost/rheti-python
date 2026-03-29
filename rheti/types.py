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

WING_DETAIL = {
    1: {
        '1w9': {
            'name': 'The Idealist',
            'summary': 'A quieter, more detached One. Principled and philosophical, driven by a '
                       'vision of how things ought to be rather than a need to correct others directly.',
            'emotion': (
                'Anger — the core emotional fuel of all Body types — is almost entirely internalized here. '
                'The 1w9 tends to feel a low-grade, steady resentment that rarely erupts outwardly. '
                'Instead it becomes a cold perfectionism applied mostly to themselves. They hold a tight '
                'inner standard and suffer quietly when reality falls short of it. Others may not realize '
                'how much is simmering beneath the composed surface.'
            ),
            'stress': (
                'Under stress, the 1w9 withdraws further — becoming remote, detached, and harshly '
                'self-critical. The Nine wing pulls them toward dissociation rather than confrontation. '
                'They may appear fine while privately spiraling into a conviction that they are '
                'fundamentally flawed.'
            ),
            'patterns': [
                'Drawn to ideas, systems, and reform movements more than direct people work',
                'Often appears calm and measured even when deeply bothered',
                'Tends toward academia, law, philosophy, or environmental causes',
                'Spends significant energy on inner standards and self-improvement',
                'Can be surprisingly detached and hard to read emotionally',
            ],
            'self_check': [
                'When something feels wrong, do you tend to quietly stew rather than say something?',
                'Do you hold yourself to standards you rarely voice to others?',
                'Do you often feel a subtle background dissatisfaction with the way things are?',
                'Is your first instinct to withdraw and think rather than engage and correct?',
            ],
        },
        '1w2': {
            'name': 'The Advocate',
            'summary': 'A warmer, more interpersonally engaged One. The reforming impulse is directed '
                       'outward through people — teaching, correcting, and improving others out of '
                       'genuine care as much as principle.',
            'emotion': (
                'Anger in the 1w2 is more visible than in the 1w9 — it rises when the Two wing\'s '
                'need to help collides with the One\'s standards. When people don\'t listen, don\'t '
                'improve, or don\'t appreciate the effort, frustration surfaces more openly. There is '
                'also a heart-center layer of shame borrowed from the Two wing: a fear of being seen '
                'as not good enough in the eyes of others, which drives the helping behavior as much '
                'as the principled impulse does.'
            ),
            'stress': (
                'Under stress, the 1w2 becomes visibly critical and controlling. The Two wing\'s '
                'suppressed neediness can burst out as resentment: "I do everything right and still '
                'get no appreciation." They may become preachy, intrusive, or exhaustingly demanding '
                'of perfection from those they care about most.'
            ),
            'patterns': [
                'Drawn to teaching, coaching, advocacy, social work, or ministry',
                'More openly expressive with opinions and corrections than the 1w9',
                'Genuinely wants to help people become better versions of themselves',
                'Can be warm and encouraging when standards are met; brittle when they aren\'t',
                'The hardest on the people they love most',
            ],
            'self_check': [
                'Do you find yourself giving unsolicited advice — and feeling genuinely surprised when it\'s unwelcome?',
                'Do you care a lot about being seen as a good person, not just being right?',
                'When you correct someone, is it usually because you want to help them, not just because you\'re bothered?',
                'Do you feel frustrated when people don\'t take your advice seriously?',
            ],
        },
    },
    2: {
        '2w1': {
            'name': 'The Servant',
            'summary': 'A more reserved, principled Two. Help is offered according to a clear sense '
                       'of what ought to be done — there is a moral backbone beneath the warmth.',
            'emotion': (
                'Shame — the heart of all Heart types — shows up in the 2w1 as a deep fear of being '
                'seen as selfish or not doing enough. The One wing adds guilt to the mix: a constant '
                'inner audit of whether they have given sufficiently. They often feel they haven\'t. '
                'This type rarely names their own needs because doing so feels wrong — like a '
                'violation of the self-image they\'ve built as someone who gives without expecting anything back.'
            ),
            'stress': (
                'Under stress, the 2w1 becomes self-righteous and cold. The One wing emerges as '
                'rigid judgment: "I give everything and no one does things properly." They may '
                'withdraw warmth entirely, becoming distant and correct rather than engaged and warm. '
                'Martyrdom takes a moralistic rather than dramatic form.'
            ),
            'patterns': [
                'Often in healthcare, religious service, education, or nonprofit roles',
                'Help is systematic — they show up reliably, not just when it feels good',
                'Less effusive and flattering than the 2w3; more quietly devoted',
                'Self-critical when they feel they\'ve failed someone',
                'Can be quietly resentful when their reliability goes unrecognized',
            ],
            'self_check': [
                'Do you feel uncomfortable receiving help or care, even when you genuinely need it?',
                'Is there a "right way" to give help that matters to you — not just any kind of support?',
                'Do you feel guilty when you put yourself first, even in small ways?',
                'Is your helping more driven by duty than by wanting people to like you?',
            ],
        },
        '2w3': {
            'name': 'The Host',
            'summary': 'A more outgoing, charming Two. Helping comes naturally alongside a desire '
                       'to be seen as generous, warm, and indispensable — image and love are intertwined.',
            'emotion': (
                'Shame in the 2w3 manifests as a fear of not being important enough or valued enough. '
                'The Three wing adds a performance dimension: the giving must be visible, the '
                'generosity must register. If their help goes unnoticed, the shame response is '
                'sharper and faster than in the 2w1. They can become emotionally manipulative when '
                'the image of warmth and the reality of unmet needs create internal friction.'
            ),
            'stress': (
                'Under stress, the 2w3 becomes competitive, strategically generous, and manipulative. '
                'They may engineer situations where others need them, or withdraw warmth strategically '
                'to provoke pursuit. The Three wing\'s image-focus makes them more likely to feel '
                'humiliated when their help is rejected or unacknowledged.'
            ),
            'patterns': [
                'Naturally suited to hosting, PR, management, sales, or community building roles',
                'More socially ambitious than the 2w1 — thrives in networked environments',
                'Generous in ways that are often visible; uncomfortable with anonymous giving',
                'Warm, flattering, and socially intuitive',
                'May subtly keep score of who has reciprocated and who hasn\'t',
            ],
            'self_check': [
                'When you do something generous, do you notice whether people appreciate it?',
                'Is being liked and being helpful hard to separate in your mind?',
                'Do you adapt how you present yourself depending on what people around you seem to need?',
                'Does it bother you when your efforts go unrecognized more than when the need itself goes unmet?',
            ],
        },
    },
    3: {
        '3w2': {
            'name': 'The Charmer',
            'summary': 'A more interpersonally warm Three. Success must include being liked and '
                       'valued as a person, not just admired for results.',
            'emotion': (
                'Shame in the 3w2 is most activated by the fear of being seen as cold, fake, or '
                'only self-serving. The Two wing pushes them toward genuine connection as a way of '
                'proving their worth goes beyond achievement. But the same wing can also produce a '
                'more sophisticated people-pleasing — they become excellent at reading what others '
                'want and reflecting it back. The warmth is real, but so is the calculation underneath.'
            ),
            'stress': (
                'Under stress, the 3w2 becomes emotionally manipulative and clinging. The Two wing\'s '
                'fear of abandonment surfaces: they may become disproportionately hurt by criticism, '
                'or work harder to secure others\' approval through charm rather than results. '
                'The image machine runs hotter when the performance is failing.'
            ),
            'patterns': [
                'Often in sales, entertainment, leadership, public relations, or community roles',
                'Charismatic and socially intelligent — reads rooms effortlessly',
                'More emotionally expressive and people-oriented than the 3w4',
                'Genuinely cares about the people they work with, not just the outcome',
                'Has a talent for making everyone feel like the most important person in the room',
            ],
            'self_check': [
                'Is being liked almost as important to you as being successful?',
                'Do you find yourself naturally adapting your personality to what the room seems to want?',
                'Does criticism of your character sting more than criticism of your work?',
                'Do you feel most yourself when you\'re connecting with people, not just achieving?',
            ],
        },
        '3w4': {
            'name': 'The Professional',
            'summary': 'A more introspective, image-conscious Three. Achievement is partly about '
                       'being seen as distinctive, deep, or creatively exceptional — not just successful.',
            'emotion': (
                'Shame in the 3w4 shows up as a fear of being ordinary, generic, or replaceable. '
                'The Four wing adds an emotional depth that the 3w2 often lacks, but also a '
                'melancholic undercurrent: a nagging sense that their authentic self might not be '
                'as impressive as their performed self. This can produce an exhausting internal '
                'tension between wanting to shine and fearing that the real them is somehow less than.'
            ),
            'stress': (
                'Under stress, the 3w4 becomes withdrawn, self-doubting, and prone to dark mood '
                'swings. The Four wing\'s melancholy surfaces, clashing with the Three\'s need to '
                'appear confident. They may oscillate between over-functioning and sudden crashes '
                'of self-criticism, especially when their sense of distinctive identity is threatened.'
            ),
            'patterns': [
                'Often in medicine, law, design, writing, or creative professional fields',
                'Values craft and depth alongside external recognition',
                'More serious and inward-looking than the 3w2',
                'Can feel divided between authentic expression and effective presentation',
                'Often drawn to roles that feel meaningful, not just prestigious',
            ],
            'self_check': [
                'Does being seen as ordinary feel almost as bad as failing?',
                'Do you care more about doing something you\'re proud of than just doing something that works?',
                'Is there a gap between who you feel you really are and what you show the world?',
                'Do you sometimes feel like an impostor even when your results are objectively good?',
            ],
        },
    },
    4: {
        '4w3': {
            'name': 'The Aristocrat',
            'summary': 'A more outwardly expressive, performance-oriented Four. Identity is built '
                       'through being visibly unique — presentation, style, and recognition matter.',
            'emotion': (
                'Shame in the 4w3 carries a particular sting: the fear of being seen as both '
                'ordinary and unsuccessful. The Three wing drives them toward external validation '
                'as proof that their unique identity is worth something. When recognition comes, '
                'it temporarily soothes the Four\'s longing — but the relief never lasts. Envy '
                'in this wing has a competitive edge: they don\'t just feel that others have what '
                'they lack, they feel they should be the one who has it.'
            ),
            'stress': (
                'Under stress, the 4w3 becomes image-obsessed and competitive — chasing external '
                'markers of success as a way of managing the inner sense of deficiency. They may '
                'exaggerate their accomplishments, become fiercely envious of peers, or put on a '
                'performance of confidence while privately feeling empty and behind.'
            ),
            'patterns': [
                'Often in performance arts, fashion, social media, design, or entertainment',
                'More outwardly social and expressive than the 4w5',
                'Deeply image-conscious — style is a form of self-expression and self-protection',
                'Motivated by recognition but also by genuine creative vision',
                'Can be dazzling publicly while struggling privately with adequacy',
            ],
            'self_check': [
                'Is being ordinary in a crowd one of your deeper fears?',
                'Do you find yourself comparing your creative work or lifestyle to others and feeling behind?',
                'Does recognition from the right people feel essential, not just nice?',
                'Is how you present yourself a deliberate expression of who you feel you are?',
            ],
        },
        '4w5': {
            'name': 'The Bohemian',
            'summary': 'A more withdrawn, intellectual Four. Identity is built inward — through '
                       'a rich inner world, unconventional thinking, and solitary creative work.',
            'emotion': (
                'Shame in the 4w5 is turned deeply inward, away from external performance. The '
                'Five wing reinforces withdrawal: rather than seeking recognition to soothe the '
                'inner wound, they retreat into ideas, art, and private experience. The longing '
                'is still there — they feel something essential is missing — but they tend to '
                'explore it through introspection and creative expression rather than seeking an '
                'audience. Emotions are intense but often private; the inner life is richer than '
                'what others typically see.'
            ),
            'stress': (
                'Under stress, the 4w5 becomes increasingly isolated, nihilistic, and detached. '
                'The Five wing\'s withdrawal amplifies the Four\'s already strong pull toward '
                'melancholy. They may disappear into their inner world entirely, losing contact '
                'with practical life, relationships, and even basic self-care.'
            ),
            'patterns': [
                'Often in writing, music composition, philosophy, research, or solitary art forms',
                'Less concerned with recognition than the 4w3; more interested in depth and authenticity',
                'Tends toward eccentricity and originality over convention',
                'Builds a rich internal symbolic world — often deeply spiritual or philosophical',
                'May seem mysterious or unknowable to others; prefers a few close relationships to many',
            ],
            'self_check': [
                'Do you process your emotions primarily through solitude and creativity rather than sharing them?',
                'Are you more comfortable being misunderstood than performing a version of yourself for others?',
                'Does your inner world feel more real to you than most social situations?',
                'Do you tend to find most people exhausting or shallow after a while?',
            ],
        },
    },
    5: {
        '5w4': {
            'name': 'The Iconoclast',
            'summary': 'A more emotionally attuned, creative Five. Knowledge is pursued not just '
                       'analytically but as a means of making sense of profound inner experience.',
            'emotion': (
                'Fear — the core anxiety of all Head types — in the 5w4 takes an existential and '
                'aesthetic form. It isn\'t just "I don\'t know enough to be safe" but "I don\'t '
                'understand what it all means." The Four wing brings a sensitivity to beauty, '
                'loss, and meaning alongside the Five\'s hunger for understanding. This type may '
                'feel their emotions more intensely than a 5w6, but they tend to process them '
                'privately, filtering experience through a rich inner symbolic framework.'
            ),
            'stress': (
                'Under stress, the 5w4 becomes self-absorbed, isolated, and prone to melancholy. '
                'They may stop engaging with the world entirely, retreating into increasingly '
                'abstract or dark inner territory. The Four wing amplifies the existential '
                'dimension of the retreat — this isn\'t just withdrawal, it can become a '
                'conviction that nothing is worth engaging with.'
            ),
            'patterns': [
                'Often in the humanities, fine arts, music, literature, or philosophy',
                'Drawn to unconventional, eccentric, or esoteric fields of knowledge',
                'More emotionally sensitive and aesthetically attuned than the 5w6',
                'May have a melancholic or brooding quality; emotionally deep but private',
                'Values originality above almost everything — conformity feels like a kind of death',
            ],
            'self_check': [
                'Does understanding something emotionally feel as important as understanding it logically?',
                'Do you find yourself drawn to art, music, or literature as a way of processing your inner world?',
                'Is your pursuit of knowledge driven partly by a search for meaning, not just capability?',
                'Do you often feel like an outsider — even in fields you\'ve mastered?',
            ],
        },
        '5w6': {
            'name': 'The Problem Solver',
            'summary': 'A more practical, systematic Five. Knowledge is accumulated as a reliable '
                       'defense against a world that feels unpredictable and demanding.',
            'emotion': (
                'Fear in the 5w6 is more pragmatic: the world is full of unpredictable threats, '
                'and information is the best armor. The Six wing adds a loyalty and responsibility '
                'dimension — this type isn\'t just protecting themselves, they feel responsible '
                'for being capable within systems they belong to. They tend to be more socially '
                'engaged than the 5w4 (within trusted structures), and their anxiety is more '
                'concrete: "Am I prepared? Do I know enough? What could go wrong?"'
            ),
            'stress': (
                'Under stress, the 5w6 becomes anxious, paranoid, and hypervigilant. The Six '
                'wing\'s worst-case-scenario thinking combines with the Five\'s withdrawal — '
                'they may spiral into exhaustive contingency planning that never leads to action, '
                'or retreat from trusted systems entirely when those systems feel threatening.'
            ),
            'patterns': [
                'Often in STEM, engineering, systems analysis, IT, law, or medicine',
                'More team-oriented and structured than the 5w4 — thrives within clear domains',
                'Builds loyalty carefully but keeps it reliably once established',
                'Practical intellectual: interested in knowledge that can be applied',
                'Anxiety tends to be concrete and anticipatory rather than existential',
            ],
            'self_check': [
                'Does knowing exactly how something works make you feel meaningfully safer?',
                'Do you feel responsible for being competent within systems or groups that matter to you?',
                'Is your intellectual preparation partly about preventing things from going wrong?',
                'Are you more comfortable trusting knowledge and systems than trusting people\'s intentions?',
            ],
        },
    },
    6: {
        '6w5': {
            'name': 'The Defender',
            'summary': 'A more introverted, analytical Six. Security is built through knowledge, '
                       'preparation, and self-reliance — guarding against a world felt as fundamentally unsafe.',
            'emotion': (
                'Fear in the 6w5 is managed through intellectual mastery and systematic preparation. '
                'The Five wing reinforces the Six\'s tendency to research, analyze, and plan — '
                '"if I understand it fully, it can\'t surprise me." But the anxiety is still there '
                'underneath. This type can appear highly capable and self-sufficient while privately '
                'running detailed threat assessments. Trust is built slowly and guarded carefully; '
                'betrayal is not forgotten.'
            ),
            'stress': (
                'Under stress, the 6w5 becomes isolating, paranoid, and increasingly convinced '
                'that no one and nothing can be trusted. The Five wing\'s withdrawal amplifies the '
                'Six\'s suspicion. They may cut off from support systems exactly when they need '
                'them most, retreating into a self-sufficient posture that actually deepens the fear.'
            ),
            'patterns': [
                'Often in research, law, IT security, academia, engineering, or military/intelligence fields',
                'More self-reliant and introverted than the 6w7 — builds security internally',
                'Loyal to carefully vetted people and institutions; skeptical of outsiders',
                'Thoughtful, thorough, and often deeply knowledgeable in their domain',
                'Can come across as standoffish until trust is established',
            ],
            'self_check': [
                'Does having deep knowledge of something make you feel more in control of your fear about it?',
                'Do you tend to be more comfortable trusting information than trusting people?',
                'Is your first instinct when anxious to research, prepare, and plan rather than seek reassurance?',
                'Do you find most people get access to you slowly, if at all?',
            ],
        },
        '6w7': {
            'name': 'The Buddy',
            'summary': 'A more outgoing, socially warm Six. Security is built partly through '
                       'connection — belonging to a group or community that feels reliable.',
            'emotion': (
                'Fear in the 6w7 is managed through relationship and social belonging. The Seven '
                'wing lightens the anxiety considerably — this type can seem upbeat, funny, and '
                'highly social, and often uses humor as a way of deflecting or releasing nervous '
                'energy. But underneath the warmth, the Six\'s loyalty tests are still running: '
                '"Can I really trust this person? What happens if this group fails me?" The '
                'anxiety is more interpersonal than analytical.'
            ),
            'stress': (
                'Under stress, the 6w7 becomes scattered, impulsive, and reactively optimistic — '
                'reaching for stimulation (the Seven wing) to avoid sitting with the fear. They '
                'may make reckless decisions, over-commit socially, or oscillate between seeking '
                'reassurance and suddenly defying the people they were just leaning on.'
            ),
            'patterns': [
                'Often in customer-facing roles, politics, entertainment, social work, or education',
                'Warm, funny, and easy to be around — people naturally trust them',
                'More comfortable in groups and social settings than the 6w5',
                'Uses humor and charm as a way of managing their own anxiety',
                'Genuinely loyal and hardworking within communities they believe in',
            ],
            'self_check': [
                'Do you feel meaningfully safer when you\'re around people you trust?',
                'Do you use humor to lighten your own anxiety or keep conversations from getting too heavy?',
                'Is your loyalty to groups or communities strong — and your sense of betrayal when they let you down equally strong?',
                'Do you tend to mask worry with cheerfulness more than you let on?',
            ],
        },
    },
    7: {
        '7w6': {
            'name': 'The Entertainer',
            'summary': 'A more loyal, relationship-oriented Seven. Enthusiasm is tempered by '
                       'genuine care for people and a desire to belong, not just experience.',
            'emotion': (
                'Fear in the 7w6 isn\'t just about deprivation — it also includes a fear of '
                'being abandoned or left without support. The Six wing adds an interpersonal '
                'anxiety underneath the Seven\'s natural buoyancy. This type tends to be warmer, '
                'more committed, and more reliably present than the 7w8 — but the anxiety can '
                'surface as worry, indecisiveness, or a need for reassurance that sits oddly '
                'against their bright exterior.'
            ),
            'stress': (
                'Under stress, the 7w6 becomes anxious, indecisive, and prone to seeking '
                'reassurance. The Six wing\'s worst-case thinking activates: the future, '
                'which normally feels full of possibility, suddenly feels threatening. They '
                'may cling to people for support while also feeling guilty about needing it, '
                'or oscillate between optimism and sudden bouts of worry.'
            ),
            'patterns': [
                'Often in entertainment, comedy, education, social work, or community organizing',
                'More warmth and follow-through than the 7w8 — relationships are genuinely important',
                'Uses humor to connect as much as to entertain',
                'Can be reliably fun and also genuinely present during hard times',
                'Anxiety tends to emerge as worry about people rather than systems',
            ],
            'self_check': [
                'Does being separated from people you care about feel genuinely threatening, not just inconvenient?',
                'Do you worry about people you love even when there\'s no obvious reason to?',
                'Does your enthusiasm feel partly like a way of keeping spirits up — yours and others\'?',
                'Is loyalty something you take seriously, even when it costs you?',
            ],
        },
        '7w8': {
            'name': 'The Realist',
            'summary': 'A more assertive, driven Seven. Enthusiasm combines with willpower — '
                       'this type doesn\'t just want experiences, they make them happen.',
            'emotion': (
                'Fear in the 7w8 is managed through action, dominance, and forward momentum. '
                'The Eight wing adds aggression and appetite — this type wants more, faster, and '
                'has the force of will to pursue it. They are less likely to acknowledge anxiety '
                'than the 7w6; instead they outrun it through sheer energy and decisiveness. '
                'The shadow side is a difficulty slowing down, tolerating frustration, or sitting '
                'with the pain they\'ve been sprinting away from.'
            ),
            'stress': (
                'Under stress, the 7w8 becomes reckless, aggressive, and impulsive. The Eight '
                'wing\'s force amplifies the Seven\'s scattered energy — they may take on enormous '
                'risks, lash out at constraints, or pursue stimulation in increasingly destructive '
                'ways. Slowing down feels unbearable; sitting with feelings feels like defeat.'
            ),
            'patterns': [
                'Often in entrepreneurship, politics, adventure sports, sales, or entertainment',
                'More confrontational and willing to push back than the 7w6',
                'High energy, high appetite — for experiences, challenges, and resources',
                'Can be enormously productive and compelling when channeled well',
                'Doesn\'t wait for permission; may ask forgiveness rather than seek approval',
            ],
            'self_check': [
                'Do you tend to outrun anxiety through action rather than sitting with it?',
                'When you feel limited or constrained, does your first instinct be to push through or push back?',
                'Is your appetite for experience and stimulation genuinely larger than most people\'s?',
                'Do you find waiting, slowing down, or processing feelings genuinely uncomfortable?',
            ],
        },
    },
    8: {
        '8w7': {
            'name': 'The Maverick',
            'summary': 'A more extroverted, expansive Eight. Power is channeled into building, '
                       'leading, and pursuing bold new ventures with strategic optimism.',
            'emotion': (
                'Anger — the Body type\'s core fuel — in the 8w7 is fast, hot, and often quickly '
                'released rather than held. The Seven wing adds an appetite for life that makes '
                'this the most extroverted and socially engaged Eight variant. Anger serves '
                'momentum: it clears obstacles and propels action. There is also a lighter '
                'quality here — this type can be genuinely fun, charismatic, and visionary '
                'alongside being formidable. But the shadow is a difficulty sitting with '
                'failure, loss, or limitation.'
            ),
            'stress': (
                'Under stress, the 8w7 becomes reckless, hedonistic, and controlling. The Seven '
                'wing\'s escapism shows up: rather than confronting difficulty, they may barrel '
                'into excess — more stimulation, more risk, more expansion — as a way of '
                'outrunning the feeling of being cornered. They can become genuinely dangerous '
                'to themselves and those around them when operating at the unhealthy end.'
            ),
            'patterns': [
                'Often in entrepreneurship, politics, entertainment, finance, or military leadership',
                'Charismatic, bold, and highly social compared to the 8w9',
                'Drawn to building, expanding, and taking on challenges others won\'t',
                'Can inspire enormous loyalty — or create enormous disruption',
                'Doesn\'t typically hold grudges long; anger flares and passes',
            ],
            'self_check': [
                'Do you tend to get angry quickly, but also move on from it quickly?',
                'Is life most vivid for you when there\'s a real challenge, risk, or big thing being built?',
                'Do people find you energizing and occasionally overwhelming in equal measure?',
                'Does slowing down or being constrained feel genuinely intolerable?',
            ],
        },
        '8w9': {
            'name': 'The Bear',
            'summary': 'A quieter, steadier Eight. Power is expressed through calm authority '
                       'and deep reliability rather than aggression and expansion.',
            'emotion': (
                'Anger in the 8w9 is slower to surface and harder to read — but when it comes, '
                'it is enormous and sustained. The Nine wing damps the reactivity, producing a '
                'more patient, deliberate expression of Eight energy. This type can absorb a '
                'great deal before responding, and their stillness is often mistaken for '
                'easygoing nature — right up until the line is crossed. The anger is real, it '
                'just moves like a glacier rather than a fire. This type often struggles to '
                'acknowledge how angry they actually are.'
            ),
            'stress': (
                'Under stress, the 8w9 withdraws into a fortress of silence and intransigence. '
                'The Nine wing\'s passivity combines with the Eight\'s refusal to be vulnerable '
                '— they may stop communicating entirely, become immovable, or cut off '
                'relationships with a finality that surprises people who thought everything was fine.'
            ),
            'patterns': [
                'Often in leadership, mentoring, mediation, law enforcement, or community organizing',
                'Protective rather than aggressive — people feel safe around them',
                'More patient and diplomatic than the 8w7; less interested in the spotlight',
                'Deeply loyal; the circle of trust is small but those in it are held fiercely',
                'May be underestimated — their power reveals itself only when tested',
            ],
            'self_check': [
                'Do people sometimes misjudge you as easygoing — until they realize they aren\'t?',
                'Do you protect people more than you challenge or compete with them?',
                'Does your anger tend to build quietly rather than flare immediately?',
                'Is your first response to conflict often stillness or withdrawal rather than confrontation?',
            ],
        },
    },
    9: {
        '9w8': {
            'name': 'The Referee',
            'summary': 'A more assertive, self-possessed Nine. Peacefulness coexists with '
                       'an ability to hold ground — this type can push back when pushed.',
            'emotion': (
                'Anger — the Body center\'s core issue — in the 9w8 is more accessible than in '
                'the 9w1. The Eight wing makes the Nine\'s anger occasionally visible, giving '
                'this type a groundedness and occasional bluntness the 9w1 typically lacks. '
                'But the Nine\'s fundamental strategy is still to avoid anger through merging '
                'and accommodation — the 8 wing just means that strategy has a breaking point. '
                'When the 9w8 finally says "no," it tends to be unmistakable.'
            ),
            'stress': (
                'Under stress, the 9w8 can become passive-aggressive and stubbornly unmovable. '
                'The Eight wing\'s resistance combines with the Nine\'s avoidance — rather than '
                'open conflict, they may simply stop cooperating, go silent, or dig in with a '
                'quiet immovability that\'s hard to address because it\'s never fully surfaced.'
            ),
            'patterns': [
                'Often in management, conflict resolution, athletics, skilled trades, or community roles',
                'More comfortable asserting preferences and boundaries than the 9w1',
                'Can be both deeply easy to get along with and surprisingly firm under pressure',
                'Tends to have a physical or hands-on quality; grounded in the body',
                'May surprise people with occasional bluntness after long accommodation',
            ],
            'self_check': [
                'Can you hold your ground when someone pushes you — eventually, if not immediately?',
                'Is there a quiet stubbornness underneath your easygoing exterior?',
                'Do you sometimes surprise yourself (or others) by how firmly you can say no?',
                'Is there a part of you that simply refuses to be controlled, even if you rarely show it?',
            ],
        },
        '9w1': {
            'name': 'The Dreamer',
            'summary': 'A more principled, idealistic Nine. Peacefulness is grounded in deep values — '
                       'this type wants not just harmony but harmony done right.',
            'emotion': (
                'Anger in the 9w1 is perhaps the most thoroughly buried of any Enneagram variant. '
                'The One wing converts it into a quiet resentment or dissatisfaction with how '
                'things are, and the Nine\'s merging tendency suppresses even that. This type '
                'often feels irritation as a vague sense that something isn\'t right, but '
                'struggles to name it or act on it. The inner critic is present (from the One '
                'wing) but it tends to create a quiet conscience rather than vocal judgment. '
                'They can feel chronically slightly disappointed without knowing why.'
            ),
            'stress': (
                'Under stress, the 9w1 becomes quietly withdrawn and increasingly judgmental — '
                'not outwardly critical, but internally tracking everything that\'s wrong while '
                'appearing disengaged. The One wing\'s perfectionism surfaces as a private '
                'conviction that things are not as they should be, while the Nine wing makes '
                'it impossible to say so directly.'
            ),
            'patterns': [
                'Often in education, religious or spiritual communities, nonprofit work, or counseling',
                'Guided by deep ethical convictions that rarely get voiced as demands',
                'More idealistic and principled than the 9w8; less comfortable with conflict',
                'Has a certain gentle authority — people listen to them even when they speak quietly',
                'May experience chronic mild dissatisfaction without being able to articulate the source',
            ],
            'self_check': [
                'Do you have strong values that quietly guide your choices, even when you don\'t announce them?',
                'Do you sometimes feel vaguely dissatisfied without being able to name exactly what\'s wrong?',
                'Is it hard for you to express irritation or disappointment directly, even when you\'re clearly feeling it?',
                'Do people often sense your disapproval before you\'ve said a word?',
            ],
        },
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
