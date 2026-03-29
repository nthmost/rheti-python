"""
differentiators.py — Follow-up mini-tests for ambiguous RHETI results.

When two types score within a few points of each other, these short
motivation-focused questionnaires help the test-taker distinguish which
type is the better fit.  Questions target the *why* behind behavior —
core motivation, core fear, the triad emotion (anger / shame / fear),
and stress response — not observable behavior, which the two types
often share.

Usage:
    from rheti.differentiators import get_differentiator

    pair = get_differentiator(1, 8)
    # pair is a dict with keys: title, intro, questions
"""

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

PAIRS: dict[tuple[int, int], dict] = {

    # ------------------------------------------------------------------
    (1, 2): {
        "title": "Type 1 or Type 2?",
        "intro": (
            "The RHETI questions around helpfulness, standards, and doing "
            "the right thing weren't sharp enough to tell you apart here. "
            "Both types can look conscientious, warm, and hard-working from "
            "the outside.  The real difference is *internal*: Type 1 is "
            "driven by an inner critic that demands you live up to your own "
            "principles, while Type 2's engine is relational — a deep need "
            "to be wanted and appreciated by the people who matter to you. "
            "Where your sharpest self-judgment lands (on your performance "
            "vs. on whether others value you) is the clearest signal."
        ),
        "questions": [
            {
                "stem": (
                    "When you do something genuinely kind for someone, "
                    "what matters most to you afterward?"
                ),
                "options": [
                    [1, "That I did it correctly and without hypocrisy — "
                        "that it was truly selfless."],
                    [2, "That the person felt cared for and appreciates "
                        "what I did for them."],
                ],
            },
            {
                "stem": (
                    "When you feel a flash of inner shame or self-disgust, "
                    "it is most often because:"
                ),
                "options": [
                    [1, "I fell short of my own standard — I was lazy, "
                        "sloppy, or morally inconsistent."],
                    [2, "Someone I care about seemed disappointed in me "
                        "or didn't need me as much as I hoped."],
                ],
            },
            {
                "stem": (
                    "Your close friend is making a decision you think is "
                    "clearly wrong.  What is your first instinct?"
                ),
                "options": [
                    [1, "Say something — the right thing to do is to be "
                        "honest, even if it creates friction."],
                    [2, "Tread carefully — preserving the warmth of the "
                        "relationship matters as much as the outcome."],
                ],
            },
            {
                "stem": (
                    "When you imagine being truly autonomous — needing "
                    "no one, accountable to no one — how does that feel?"
                ),
                "options": [
                    [1, "Liberating.  I would finally be able to do things "
                        "correctly without compromise."],
                    [2, "Lonely and purposeless.  My sense of meaning "
                        "comes from connection and being needed."],
                ],
            },
            {
                "stem": (
                    "Under sustained stress you are most likely to become:"
                ),
                "options": [
                    [1, "Withdrawn and darkly self-critical, dwelling on "
                        "everything I've done wrong or failed to be."],
                    [2, "Clingy or manipulative, intensifying my efforts "
                        "to get people to acknowledge how much I've given."],
                ],
            },
            {
                "stem": (
                    "Complete this sentence honestly: "
                    "\"At my core, I see myself primarily as...\""
                ),
                "options": [
                    [1, "...someone with high standards who is trying to "
                        "live rightly and improve what is broken."],
                    [2, "...someone who loves deeply and whose greatest "
                        "gift is caring for and supporting others."],
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    (1, 8): {
        "title": "Type 1 or Type 8?",
        "intro": (
            "Both Type 1 and Type 8 live in the Body triad and share a "
            "complicated relationship with anger — but the relationship "
            "looks almost opposite from the inside.  The behavioral "
            "questions about control, directness, and high standards can "
            "describe either type.  The real split is what you *do* with "
            "anger: Type 1 turns it inward, converting it into resentment "
            "and perfectionism under strict internal rules; Type 8 expresses "
            "it outward, then moves on, operating by rules of their own "
            "making.  Under pressure the types also diverge sharply — "
            "1s spiral into moody self-criticism (toward Type 4), "
            "while 8s go cold and fortress-like (toward Type 5)."
        ),
        "questions": [
            {
                "stem": (
                    "When you get genuinely angry with someone, what "
                    "typically happens inside you next?"
                ),
                "options": [
                    [1, "I suppress the anger and redirect it inward — "
                        "critiquing myself for losing composure or "
                        "rehearsing how the situation *should* have gone."],
                    [8, "I express it or act on it, and once it's out, "
                        "it's largely gone — I don't usually hold grudges."],
                ],
            },
            {
                "stem": (
                    "Which statement about rules feels more true for you?"
                ),
                "options": [
                    [1, "Rules and principles matter because fairness and "
                        "integrity require consistency — I hold myself to "
                        "them even when no one is watching."],
                    [8, "I respect rules I've decided make sense, but I "
                        "won't be constrained by rules imposed on me that "
                        "I haven't chosen to accept."],
                ],
            },
            {
                "stem": (
                    "Your core fear — the thing that feels most "
                    "existentially threatening — is closest to:"
                ),
                "options": [
                    [1, "Being corrupt, wrong, or deeply flawed in a "
                        "way I can't correct."],
                    [8, "Being controlled, violated, or left vulnerable "
                        "to someone else's agenda."],
                ],
            },
            {
                "stem": (
                    "When everything is going badly and you are at your "
                    "worst, you are most likely to:"
                ),
                "options": [
                    [1, "Withdraw into brooding, self-pity, and a sense "
                        "of being irreparably inadequate."],
                    [8, "Cut off emotionally, pull away from everyone, "
                        "and rely entirely on my own resources."],
                ],
            },
            {
                "stem": (
                    "What drives your desire to improve the world "
                    "around you?"
                ),
                "options": [
                    [1, "Things should be done correctly; disorder and "
                        "wrongdoing are genuinely painful to me and I "
                        "feel responsible for fixing them."],
                    [8, "I want to protect people I care about and "
                        "stamp out injustice — power used wrongly is "
                        "something I physically cannot ignore."],
                ],
            },
            {
                "stem": (
                    "Complete this sentence honestly: "
                    "\"At my core, I see myself primarily as...\""
                ),
                "options": [
                    [1, "...a person of principle who is always working "
                        "to be better and to hold the line against "
                        "what is wrong."],
                    [8, "...a strong person who protects what matters "
                        "and refuses to be dominated or deceived."],
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    (1, 9): {
        "title": "Type 1 or Type 9?",
        "intro": (
            "Types 1 and 9 are neighbors in the Body triad and can look "
            "remarkably alike on the surface: both value stability, both "
            "can come across as calm and principled.  The RHETI questions "
            "around order, patience, and avoiding conflict didn't cleanly "
            "separate you.  The real divide is in your *relationship to "
            "anger and action*: Type 1 is an active reformer driven by a "
            "persistent inner critic — anger gets converted into "
            "improvement-seeking energy.  Type 9 numbs anger almost "
            "entirely, choosing peace over engagement; the risk isn't "
            "perfectionism but inertia."
        ),
        "questions": [
            {
                "stem": (
                    "Something is clearly wrong in a shared space — "
                    "a bad policy, an unfair situation.  Your gut response is:"
                ),
                "options": [
                    [1, "Address it, even if it causes discomfort — "
                        "ignoring something wrong feels like complicity."],
                    [9, "Weigh whether the disruption of speaking up "
                        "is worth it; often peace seems more valuable "
                        "than the fight."],
                ],
            },
            {
                "stem": (
                    "How would you describe your inner mental life on "
                    "a typical day?"
                ),
                "options": [
                    [1, "Active and evaluative — I'm often noticing what "
                        "could be better and feeling a low hum of "
                        "urgency about it."],
                    [9, "Relatively quiet and diffuse — I can easily "
                        "lose track of my own priorities while attending "
                        "to other things."],
                ],
            },
            {
                "stem": (
                    "When you feel genuine anger, what happens to it?"
                ),
                "options": [
                    [1, "It gets redirected — into critique, into effort, "
                        "into a tightened resolve to do things right."],
                    [9, "It tends to disappear or get buried; I often "
                        "don't fully register that I'm angry until "
                        "much later."],
                ],
            },
            {
                "stem": (
                    "Which statement about your deepest fear feels "
                    "more accurate?"
                ),
                "options": [
                    [1, "Being fundamentally bad, wrong, or corrupt — "
                        "someone who can't be trusted to do the right thing."],
                    [9, "Being in conflict, being separated from "
                        "connection, or losing the peace and wholeness "
                        "I've worked to maintain."],
                ],
            },
            {
                "stem": (
                    "You are under serious, prolonged pressure.  "
                    "Your most likely response is:"
                ),
                "options": [
                    [1, "I become more critical — of myself first, "
                        "then of others — and my mood darkens."],
                    [9, "I check out: I focus on low-stakes comfort "
                        "activities and become harder to reach or mobilize."],
                ],
            },
            {
                "stem": (
                    "Complete this sentence honestly: "
                    "\"At my core, I see myself primarily as...\""
                ),
                "options": [
                    [1, "...someone who holds high standards and keeps "
                        "working to make things right."],
                    [9, "...someone who keeps the peace, holds space "
                        "for everyone, and tries not to make things worse."],
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    (2, 3): {
        "title": "Type 2 or Type 3?",
        "intro": (
            "Types 2 and 3 are neighbors in the Heart triad and share a "
            "polished, people-pleasing surface.  The RHETI questions around "
            "relationships, achievement, and image-consciousness weren't "
            "diagnostic enough to separate you clearly.  The real "
            "difference is *what you are performing for*: Type 2 shapes "
            "themselves around what others need in order to be loved and "
            "indispensable; Type 3 shapes themselves around whatever image "
            "will make them look successful and admirable.  The deepest "
            "shame for a 2 is feeling unwanted; for a 3 it is being "
            "exposed as a failure."
        ),
        "questions": [
            {
                "stem": (
                    "When you are working hard on something, your "
                    "primary motivation is closer to:"
                ),
                "options": [
                    [2, "Being genuinely useful and caring to the "
                        "people involved — their gratitude and need "
                        "for me matters most."],
                    [3, "Achieving something impressive and being "
                        "recognized as capable and successful."],
                ],
            },
            {
                "stem": (
                    "In a new social environment, you're most likely to:"
                ),
                "options": [
                    [2, "Tune in to what others need and find ways to "
                        "provide it — making people feel cared for "
                        "gives me energy."],
                    [3, "Read the room to understand what kind of "
                        "person will be admired here and present "
                        "that version of myself."],
                ],
            },
            {
                "stem": (
                    "When someone you care about doesn't seem to need "
                    "you anymore, you typically feel:"
                ),
                "options": [
                    [2, "Quietly devastated — being needed is fundamental "
                        "to how I experience my own value."],
                    [3, "Slightly relieved or indifferent — my self-worth "
                        "doesn't depend heavily on any one relationship."],
                ],
            },
            {
                "stem": (
                    "You fail at something important and publicly visible.  "
                    "Your most immediate internal experience is:"
                ),
                "options": [
                    [2, "Anxiety about how people are now seeing me — "
                        "do they still want me around?"],
                    [3, "A fierce urgency to reframe, recover, or "
                        "demonstrate that this doesn't define me."],
                ],
            },
            {
                "stem": (
                    "Which of these is a more accurate description of "
                    "how you relate to your own emotional life?"
                ),
                "options": [
                    [2, "I'm very aware of feelings — mine and everyone "
                        "else's — though I sometimes suppress my own "
                        "needs to keep others comfortable."],
                    [3, "I tend to set feelings aside in favor of "
                        "staying focused on goals; I process emotions "
                        "later, if at all."],
                ],
            },
            {
                "stem": (
                    "Complete this sentence honestly: "
                    "\"At my core, I see myself primarily as...\""
                ),
                "options": [
                    [2, "...someone whose purpose is to love and support "
                        "others — that is where my identity lives."],
                    [3, "...someone capable and effective who makes "
                        "things happen and earns their place."],
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    (3, 4): {
        "title": "Type 3 or Type 4?",
        "intro": (
            "Types 3 and 4 are neighbors in the Heart triad and both care "
            "deeply about identity and how they're perceived — but from "
            "opposite angles.  The RHETI questions around self-presentation, "
            "emotion, and uniqueness weren't sharp enough to separate you. "
            "The fundamental difference is what each type does with shame: "
            "Type 3 bypasses it by achieving and adapting so effectively "
            "that the question of inherent worth never has to be faced; "
            "Type 4 faces shame directly (often obsessively), and builds "
            "an identity *around* the search for authentic self.  3s "
            "sidestep feelings to succeed; 4s make feelings the center "
            "of their life."
        ),
        "questions": [
            {
                "stem": (
                    "When a strong painful emotion arises in the middle "
                    "of an important project, you are most likely to:"
                ),
                "options": [
                    [3, "Acknowledge it briefly and set it aside — "
                        "there will be time to process later, and right "
                        "now I need to perform."],
                    [4, "Sit with it, even at the cost of the project — "
                        "my emotional truth feels more real than "
                        "external demands."],
                ],
            },
            {
                "stem": (
                    "Your deepest fear is closest to:"
                ),
                "options": [
                    [3, "Being exposed as worthless or mediocre — "
                        "failing so visibly that people see I'm "
                        "not as capable as I appeared."],
                    [4, "Being fundamentally ordinary, or having no "
                        "real identity — that beneath the surface "
                        "there is nothing distinctive or meaningful."],
                ],
            },
            {
                "stem": (
                    "How much do you adapt your personality and style "
                    "based on the audience you're with?"
                ),
                "options": [
                    [3, "Quite a bit — I read the room and naturally "
                        "present the version of myself that will land best."],
                    [4, "Very little — adapting feels like a betrayal "
                        "of authenticity; I'd rather be rejected for "
                        "who I actually am."],
                ],
            },
            {
                "stem": (
                    "When you reflect on your life's arc, which question "
                    "feels more pressing?"
                ),
                "options": [
                    [3, "Have I accomplished enough?  Am I building "
                        "something that demonstrates real capability?"],
                    [4, "Have I been truly myself?  Has my life expressed "
                        "something genuine and meaningful?"],
                ],
            },
            {
                "stem": (
                    "Under significant stress you are most likely to:"
                ),
                "options": [
                    [3, "Work harder and become more competitive, "
                        "doubling down on achievement to quiet the anxiety."],
                    [4, "Become moody and self-absorbed, withdrawing into "
                        "an intensified search for what is missing in me."],
                ],
            },
            {
                "stem": (
                    "Complete this sentence honestly: "
                    "\"At my core, I see myself primarily as...\""
                ),
                "options": [
                    [3, "...a capable, effective person who earns "
                        "their place in the world through results."],
                    [4, "...a unique individual on an ongoing quest "
                        "to understand and express who I truly am."],
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    (4, 5): {
        "title": "Type 4 or Type 5?",
        "intro": (
            "Types 4 and 5 are neighbors and both tend to be introspective, "
            "creative, and somewhat withdrawn from the mainstream — which "
            "is exactly why the RHETI questions didn't clearly separate you. "
            "The real divide is in your relationship to emotion and "
            "connection: Type 4 is emotionally expressive, wants to be "
            "deeply *known*, and pursues meaning through feeling and "
            "self-revelation.  Type 5 is emotionally private, wants to "
            "be deeply *capable*, and pursues meaning through understanding "
            "and mastery.  For 4, the fear is of having no identity; "
            "for 5, the fear is of being incompetent or depleted."
        ),
        "questions": [
            {
                "stem": (
                    "When you create something — art, writing, research, "
                    "a system — what are you most hoping to achieve?"
                ),
                "options": [
                    [4, "To express something true and personal — to "
                        "make my inner world visible and have it recognized."],
                    [5, "To understand something deeply and demonstrate "
                        "mastery — to produce work that is genuinely "
                        "rigorous and complete."],
                ],
            },
            {
                "stem": (
                    "In a close relationship, what do you find yourself "
                    "most wanting from the other person?"
                ),
                "options": [
                    [4, "To be truly seen — to have someone know my "
                        "depths, my contradictions, my emotional interior."],
                    [5, "To be given space — to share ideas and interests "
                        "without feeling drained or encroached upon."],
                ],
            },
            {
                "stem": (
                    "When your emotional reserves are low, you tend to:"
                ),
                "options": [
                    [4, "Intensify — sink deeper into feeling, longing, "
                        "or melancholy, searching for what is missing."],
                    [5, "Retreat — cut social contact and replenish "
                        "through solitude, reading, or thinking."],
                ],
            },
            {
                "stem": (
                    "Your deepest fear is closest to:"
                ),
                "options": [
                    [4, "Being without a meaningful identity — that "
                        "I am hollow, ordinary, or fundamentally defective."],
                    [5, "Being incapable or overwhelmed — that I won't "
                        "have enough knowledge, energy, or resources "
                        "to cope."],
                ],
            },
            {
                "stem": (
                    "How comfortable are you sharing your emotional "
                    "inner life with people you know well?"
                ),
                "options": [
                    [4, "Very — emotional honesty and depth feel essential; "
                        "surface-level connection isn't enough."],
                    [5, "Selectively and carefully — I share ideas freely "
                        "but my emotional life feels private and guarded."],
                ],
            },
            {
                "stem": (
                    "Complete this sentence honestly: "
                    "\"At my core, I see myself primarily as...\""
                ),
                "options": [
                    [4, "...a unique, feeling person searching for "
                        "authentic self-expression and deep connection."],
                    [5, "...an independent thinker building competence "
                        "and understanding so I can stand on my own."],
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    (5, 6): {
        "title": "Type 5 or Type 6?",
        "intro": (
            "Types 5 and 6 are neighbors in the Head triad and both lead "
            "with careful, analytical thinking — which is why the "
            "behavioral questions around preparation, caution, and "
            "skepticism weren't diagnostic.  The real split is in *where "
            "you go for security*: Type 5 trusts their own mind almost "
            "exclusively and withdraws to think things through alone; "
            "Type 6 doubts their own judgment and seeks external anchors "
            "— trusted people, systems, or authorities — to compensate. "
            "5s fear being incompetent; 6s fear being without support "
            "or guidance in a dangerous world."
        ),
        "questions": [
            {
                "stem": (
                    "When facing an important decision, your typical "
                    "process is:"
                ),
                "options": [
                    [5, "Gather information alone, think it through "
                        "thoroughly on my own, and trust my analysis — "
                        "external input often complicates more than it helps."],
                    [6, "Test my thinking against trusted others — "
                        "I want to know what people I respect think, "
                        "and I'm alert to what I might be missing."],
                ],
            },
            {
                "stem": (
                    "When an authority figure or institution you've "
                    "relied on proves unreliable, your reaction is:"
                ),
                "options": [
                    [5, "Confirmation that self-reliance is the only "
                        "sound approach — I'm better off depending "
                        "on my own competence."],
                    [6, "Disorienting and destabilizing — finding out "
                        "who and what I can actually trust becomes urgent."],
                ],
            },
            {
                "stem": (
                    "Your deepest fear is closest to:"
                ),
                "options": [
                    [5, "Being overwhelmed or exposed as incompetent — "
                        "not having enough inner resources to manage "
                        "what the world demands."],
                    [6, "Being without support or guidance in a world "
                        "that is genuinely dangerous — being alone "
                        "when something goes wrong."],
                ],
            },
            {
                "stem": (
                    "When anxiety spikes, your first instinct is to:"
                ),
                "options": [
                    [5, "Withdraw into my own mental space to analyze "
                        "the threat and think my way through it."],
                    [6, "Reach out to check in with someone I trust "
                        "or look for reassurance that things are okay."],
                ],
            },
            {
                "stem": (
                    "How do you relate to commitment in groups, "
                    "teams, or close relationships?"
                ),
                "options": [
                    [5, "I hold commitments carefully and somewhat "
                        "minimally — too much obligation feels depleting "
                        "and I guard my independence."],
                    [6, "I take loyalty and commitment seriously — "
                        "once I trust a person or group, I'm genuinely "
                        "devoted and expect the same in return."],
                ],
            },
            {
                "stem": (
                    "Complete this sentence honestly: "
                    "\"At my core, I see myself primarily as...\""
                ),
                "options": [
                    [5, "...an independent thinker who builds competence "
                        "and self-sufficiency as the foundation for "
                        "navigating the world."],
                    [6, "...someone who is alert to risk and committed "
                        "to the people and systems that keep the world "
                        "reliable and safe."],
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    (6, 7): {
        "title": "Type 6 or Type 7?",
        "intro": (
            "Types 6 and 7 are neighbors in the Head triad and both carry "
            "a background hum of anxiety — but they respond to it in "
            "opposite ways, which is exactly what the RHETI questions "
            "didn't capture cleanly.  Type 6 runs *toward* the anxiety, "
            "scanning for what could go wrong and seeking security "
            "structures; Type 7 runs *away* from anxiety, filling the "
            "future with positive plans and keeping options open so "
            "discomfort can't catch up.  Under stress, 6s push into "
            "anxious overperforming; 7s become uncharacteristically "
            "rigid and critical."
        ),
        "questions": [
            {
                "stem": (
                    "When you think about the future, your mind "
                    "gravitates most naturally toward:"
                ),
                "options": [
                    [6, "What could go wrong — the contingencies I "
                        "should prepare for so I'm not caught off guard."],
                    [7, "What could be amazing — the possibilities, "
                        "adventures, and experiences I want to pursue."],
                ],
            },
            {
                "stem": (
                    "When something genuinely painful or frightening "
                    "is happening to you, your instinct is:"
                ),
                "options": [
                    [6, "Face it directly, even though it's hard — "
                        "I want to understand the threat clearly "
                        "so I can deal with it."],
                    [7, "Reframe it, move past it, or find the "
                        "silver lining quickly — dwelling on pain "
                        "feels intolerable."],
                ],
            },
            {
                "stem": (
                    "Your deepest fear is closest to:"
                ),
                "options": [
                    [6, "Being without support or guidance — being "
                        "alone, abandoned, or unprepared when the "
                        "dangerous thing arrives."],
                    [7, "Being trapped in pain or deprivation — "
                        "missing out on life's fullness or being "
                        "stuck in an experience I can't escape."],
                ],
            },
            {
                "stem": (
                    "How do you relate to commitment — to a job, "
                    "a relationship, a long project?"
                ),
                "options": [
                    [6, "Once I trust something or someone, I'm "
                        "deeply loyal and consistent — reliability "
                        "is something I both offer and require."],
                    [7, "I appreciate openness — I commit, but I'm "
                        "alert to whether I'm being limited, and I "
                        "need to feel the choice remains mine."],
                ],
            },
            {
                "stem": (
                    "Under serious sustained pressure you are "
                    "most likely to become:"
                ),
                "options": [
                    [6, "Anxiously performing — working harder to "
                        "demonstrate my value and hoping that effort "
                        "will make things safer."],
                    [7, "Uncharacteristically harsh and impatient — "
                        "snapping at imperfection in myself and others "
                        "as my usual optimism breaks down."],
                ],
            },
            {
                "stem": (
                    "Complete this sentence honestly: "
                    "\"At my core, I see myself primarily as...\""
                ),
                "options": [
                    [6, "...a loyal, responsible person who takes "
                        "seriously what is at stake and works hard "
                        "to keep people and systems safe."],
                    [7, "...a curious, enthusiastic person who wants "
                        "to experience everything life offers and "
                        "keep possibilities alive."],
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    (7, 8): {
        "title": "Type 7 or Type 8?",
        "intro": (
            "Types 7 and 8 are neighbors and both project energy, "
            "confidence, and a refusal to be constrained — which confused "
            "the RHETI questions around assertiveness and enthusiasm.  "
            "The core difference is *what they are protecting themselves "
            "from*: Type 7 avoids inner pain and limitation by keeping "
            "life stimulating, options open, and attention future-facing; "
            "Type 8 avoids vulnerability and loss of control by staying "
            "strong, dominant, and direct.  7s are scattered and expansive; "
            "8s are focused and intense."
        ),
        "questions": [
            {
                "stem": (
                    "When something painful — grief, fear, boredom, "
                    "helplessness — threatens to take hold of you, "
                    "your response is:"
                ),
                "options": [
                    [7, "Move.  Find something stimulating, plan "
                        "something exciting, shift my attention — "
                        "keeping the feeling from landing."],
                    [8, "Push through it or push back against whatever "
                        "is causing it — weakness is something to "
                        "be overpowered, not escaped."],
                ],
            },
            {
                "stem": (
                    "Your deepest fear is closest to:"
                ),
                "options": [
                    [7, "Being trapped in deprivation or pain — "
                        "missing out, getting stuck, or losing access "
                        "to what makes life feel worthwhile."],
                    [8, "Being controlled or betrayed — having someone "
                        "else's will imposed on me, or being left "
                        "exposed and vulnerable to harm."],
                ],
            },
            {
                "stem": (
                    "In a conflict, your instinct is:"
                ),
                "options": [
                    [7, "Find a way to reframe it or move past it — "
                        "prolonged confrontation feels like unnecessary "
                        "heaviness."],
                    [8, "Engage it directly and fully — conflict is "
                        "clarifying, and backing down feels like defeat."],
                ],
            },
            {
                "stem": (
                    "When you think about vulnerability — being seen "
                    "in your weakness or uncertainty — you feel:"
                ),
                "options": [
                    [7, "Uncomfortable, but mostly I just don't stop "
                        "long enough for it to be a problem."],
                    [8, "Actively resistant — vulnerability feels like "
                        "an opening for people to use against me, "
                        "so I avoid it carefully."],
                ],
            },
            {
                "stem": (
                    "How would you describe your relationship to "
                    "focus and depth?"
                ),
                "options": [
                    [7, "I'm naturally drawn to breadth — many "
                        "interests, many projects, many conversations.  "
                        "Going very deep in one place can feel limiting."],
                    [8, "When I care about something, I go fully in — "
                        "I'm not scattered; I'm intensely focused "
                        "on what matters to me."],
                ],
            },
            {
                "stem": (
                    "Complete this sentence honestly: "
                    "\"At my core, I see myself primarily as...\""
                ),
                "options": [
                    [7, "...an adventurous, curious person who wants "
                        "to experience life fully and keep possibilities open."],
                    [8, "...a strong, direct person who protects what "
                        "matters and refuses to be dominated or deceived."],
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    (8, 9): {
        "title": "Type 8 or Type 9?",
        "intro": (
            "Types 8 and 9 are the final neighbors in the Body triad — "
            "and on the surface both can seem calm, protective, and "
            "steadying.  The RHETI questions around conflict, decisiveness, "
            "and wanting peace weren't able to tell you apart.  The real "
            "difference is in how each type *relates to power and conflict*: "
            "Type 8 moves toward it — assertive, direct, immediately felt "
            "in any room.  Type 9 moves away from it — receptive, "
            "accommodating, easy to overlook.  Both can be deeply "
            "protective, but 8 protects through strength and 9 through "
            "presence and steadiness."
        ),
        "questions": [
            {
                "stem": (
                    "When there is open conflict around you, your "
                    "natural response is:"
                ),
                "options": [
                    [8, "Engage — I move toward conflict, say what "
                        "needs to be said, and work to resolve it "
                        "on my terms."],
                    [9, "Mediate or withdraw — I feel the conflict "
                        "as physical discomfort and work to smooth "
                        "things over or get away."],
                ],
            },
            {
                "stem": (
                    "In a group, what do people typically experience "
                    "from you?"
                ),
                "options": [
                    [8, "Presence and force — people know I'm there; "
                        "I have opinions and I'm not shy about them."],
                    [9, "Steadiness and warmth — I blend in and hold "
                        "space; people often feel calm around me."],
                ],
            },
            {
                "stem": (
                    "Your deepest fear is closest to:"
                ),
                "options": [
                    [8, "Being controlled, violated, or betrayed — "
                        "having my autonomy taken or being left "
                        "exposed and vulnerable."],
                    [9, "Separation and conflict — losing connection, "
                        "disrupting the peace, or being the cause "
                        "of fragmentation."],
                ],
            },
            {
                "stem": (
                    "When someone challenges you or pushes you "
                    "on something you believe, you typically:"
                ),
                "options": [
                    [8, "Push back — I engage the challenge directly "
                        "and I'm energized by the friction."],
                    [9, "Consider their view, perhaps too generously — "
                        "I can lose track of my own position while "
                        "trying to see theirs."],
                ],
            },
            {
                "stem": (
                    "How aware are you of what you want in a "
                    "given moment?"
                ),
                "options": [
                    [8, "Very — my desires and preferences are clear "
                        "to me and I pursue them directly."],
                    [9, "Not always — I can find myself deferring or "
                        "going along, and realize only later that "
                        "I had a preference I didn't voice."],
                ],
            },
            {
                "stem": (
                    "Complete this sentence honestly: "
                    "\"At my core, I see myself primarily as...\""
                ),
                "options": [
                    [8, "...a strong, direct person who protects "
                        "what matters and won't be dominated or deceived."],
                    [9, "...a steady, accepting person who holds space "
                        "for everyone and tries to keep things whole."],
                ],
            },
        ],
    },

}

# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def get_differentiator(a: int, b: int) -> dict | None:
    """Return the differentiator entry for the pair (a, b), or None.

    The lookup is order-independent: get_differentiator(8, 1) and
    get_differentiator(1, 8) both return the same entry.
    """
    key = (min(a, b), max(a, b))
    return PAIRS.get(key)
