"""Illustrative, deterministic relationship learning pathways. Not validated or diagnostic."""
DOMAINS = [
    ("Closeness & space", ["I enjoy spending time with my mum or caregiver.", "We can spend time apart without feeling upset.", "My need for privacy is respected."]),
    ("Disagreement & repair", ["We listen to each other when we disagree.", "After an argument, we can reconnect.", "I can disagree without feeling afraid."]),
    ("Emotional openness", ["I can talk about difficult feelings.", "My feelings are taken seriously.", "I can ask for support when I need it."]),
    ("Trust & independence", ["I can make choices that fit my age.", "My opinion matters in decisions that affect me.", "I am trusted to learn from mistakes."]),
    ("Time & enjoyment", ["We enjoy spending time together.", "We have fun without focusing on chores or schoolwork.", "We show appreciation for each other."]),
]

ARCHETYPES = [
    {
        "name": "The Close Companions", "tagline": "Making space to grow, while staying close",
        "strength": "Affection and togetherness can provide a strong foundation for connection.",
        "pattern": "You may enjoy closeness while also needing to negotiate privacy and time apart. Both needs can matter.",
        "skill": "Balancing connection with healthy personal space",
        "activities": [
            ("Together and Apart", "Each choose one activity you enjoy doing together and one you like doing independently. Make room for both this week."),
            ("The Privacy Conversation", "Use a low-stakes example to discuss what privacy means, what still needs parental guidance, and how to ask respectfully."),
            ("Reconnect Ritual", "Agree on one small way to reconnect after spending time separately, such as a shared snack or evening check-in."),
        ],
    },
    {
        "name": "The Strong-Willed Duo", "tagline": "Learning to disagree and reconnect",
        "strength": "Having opinions and caring about what matters can be positive qualities.",
        "pattern": "Disagreements may sometimes become more intense than either person intended. Repair is a skill you can practise.",
        "skill": "Listening, calming down, and making repairs after conflict",
        "activities": [
            ("Pause, Hear, Respond", "Choose a small disagreement. Take turns speaking for one minute. First repeat what you heard before responding."),
            ("Our Pause Signal", "Agree on a respectful way to request a short break during tension and a specific way to return to the conversation."),
            ("Repair in Three Steps", "Try: 'What happened for me…', 'I see how that affected you…', and 'Next time I'll try…'."),
        ],
    },
    {
        "name": "The Quiet Protectors", "tagline": "Making feelings easier to share",
        "strength": "Being considerate and thoughtful can help relationships feel gentle and respectful.",
        "pattern": "Some feelings or needs may be harder to talk about. You can build openness in small, safe steps.",
        "skill": "Sharing feelings and listening without immediately fixing",
        "activities": [
            ("Feelings Without Fixing", "Ask: 'Would you like me to listen, help you think, or offer advice?' Practise listening first."),
            ("One Small Truth", "Each share a small everyday feeling, starting with 'I felt… when…'. Neither person needs to share anything private."),
            ("The Feeling Menu", "Write or draw a few emotions from the week. Choose one you would like the other to understand better."),
        ],
    },
    {
        "name": "The Loving Guides", "tagline": "Growing trust and independence together",
        "strength": "Care, guidance and a desire to support growth can be a strong foundation.",
        "pattern": "You may see age-appropriate independence differently. Negotiating choices can help both people feel respected.",
        "skill": "Autonomy-supportive communication and collaborative decisions",
        "activities": [
            ("The Choice Exchange", "Pick one safe, age-appropriate decision. The daughter explains her preference and the caregiver shares practical concerns; agree on one trial."),
            ("Listen Before Advising", "Before giving advice, ask: 'Would you like me to listen, help you think, or offer a suggestion?'"),
            ("The Trust Ladder", "Choose one small responsibility, decide what support is needed, and review together how it went without blame."),
        ],
    },
    {
        "name": "The Busy but Loving Pair", "tagline": "Making room for moments that matter",
        "strength": "Reliability, care and everyday support often show love in practical ways.",
        "pattern": "Busy routines may leave less time to enjoy each other's company without an agenda.",
        "skill": "Shared attention, joy and appreciation",
        "activities": [
            ("Ten Minutes of Us", "Take turns choosing a ten-minute activity, with phones put away and no schoolwork or chores talk."),
            ("Three Things I Notice", "Each share three specific things you appreciate about the other, however small."),
            ("Our Weekly Ritual", "Choose one enjoyable, realistic repeatable ritual: a walk, recipe, game or music session."),
        ],
    },
]

# Backwards compatible with the original example and tests.
PATHWAYS = [(a["activities"][0][0], a["activities"][0][1]) for a in ARCHETYPES]

def score_answers(answers):
    if len(answers) != 15 or any(type(x) is not int or x not in (1, 2, 3, 4) for x in answers):
        raise ValueError("Expected 15 integer answers from 1 to 4")
    return [round(sum(answers[i*3:i*3+3]) / 3, 2) for i in range(5)]

def suggest(scores):
    if len(scores) != 5 or any(not isinstance(s, (int, float)) or not 1 <= s <= 4 for s in scores):
        raise ValueError("Expected five domain scores between 1 and 4")
    # Ties are resolved in questionnaire order, then displayed as multiple growth areas.
    return min(range(5), key=lambda i: scores[i])

def profile(scores):
    primary = suggest(scores)
    low = min(scores)
    high = max(scores)
    growth = [i for i, val in enumerate(scores) if val <= low + 0.34]
    strengths = [i for i, val in enumerate(scores) if val >= high - 0.34]
    return {"archetype": ARCHETYPES[primary], "primary_index": primary,
            "growth_indices": growth, "strength_indices": strengths,
            "close_scores": len(growth) > 1}
