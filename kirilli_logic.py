"""Kirilli demo content and transparent, non-clinical scoring logic.

Educational prototype only. Questions and archetypes are not validated scales.
"""

DOMAINS = [
    {"key": "closeness", "name": "Closeness & personal space", "icon": "🪺",
     "daughter": ["I enjoy spending time with my mother or caregiver.",
                  "We can spend time apart without either of us feeling upset.",
                  "My need for privacy is respected."],
     "mother": ["I enjoy spending time with my daughter.",
                "I am comfortable when my daughter wants time to herself.",
                "I respect my daughter's growing need for privacy."]},
    {"key": "conflict", "name": "Disagreement & repair", "icon": "🌦️",
     "daughter": ["We try to listen to each other when we disagree.",
                  "After an argument, we can reconnect.",
                  "I feel able to disagree respectfully without fearing the reaction."],
     "mother": ["I try to listen when my daughter disagrees with me.",
                "After an argument, I make an effort to reconnect.",
                "I help make it safe for my daughter to disagree respectfully."]},
    {"key": "openness", "name": "Emotional openness", "icon": "💬",
     "daughter": ["I can tell my mother or caregiver when something is bothering me.",
                  "I feel that my feelings are taken seriously.",
                  "I can ask my mother or caregiver for support when I need it."],
     "mother": ["I try to make it easy for my daughter to tell me what is bothering her.",
                "I take my daughter's feelings seriously, even when we disagree.",
                "I try to listen before jumping in with advice."]},
    {"key": "autonomy", "name": "Trust & growing independence", "icon": "🪽",
     "daughter": ["I can make choices that fit my age.",
                  "My opinion matters in decisions that affect me.",
                  "I feel trusted to try things and learn from mistakes."],
     "mother": ["I offer my daughter age-appropriate choices.",
                "I ask for her opinion about decisions that affect her.",
                "I allow safe opportunities for her to try and learn from mistakes."]},
    {"key": "joy", "name": "Shared time & enjoyment", "icon": "☀️",
     "daughter": ["We enjoy doing things together.",
                  "We have fun without focusing only on chores or schoolwork.",
                  "We show appreciation for each other."],
     "mother": ["We enjoy doing things together.",
                "I make space for time together beyond responsibilities.",
                "I show appreciation for the person my daughter is becoming."]},
]

ARCHETYPES = {
    "closeness": {
        "name": "The Close Companions", "subtitle": "Closeness with room to grow",
        "strength": "You may already have moments of togetherness to build on. As girls grow, connection and personal space can coexist.",
        "insight": "One possible area to explore is how to stay close while making room for new interests, friendships and privacy.",
        "skill": "Respecting boundaries and welcoming independence",
        "activities": [
            {"title": "Together & Apart", "time": "10 minutes", "supplies": "Paper and pencils",
             "steps": ["Each make two lists: things we enjoy together, and things we enjoy independently.", "Choose one shared activity for this week and one independent activity to support.", "Afterwards, ask: What made each choice feel comfortable?"],
             "prompt": "How can I give you space while still showing I'm here for you?"},
            {"title": "Our Connection Signal", "time": "5 minutes", "supplies": "None",
             "steps": ["Invent a small signal that means ‘I'd like some time together’.", "Agree on a friendly reply when the other person needs a little space.", "Try both signals during the week."],
             "prompt": "What helps you know I care even when we're doing different things?"},
            {"title": "The Choice Walk", "time": "15 minutes", "supplies": "A place to walk",
             "steps": ["Take a short walk and let the daughter choose the route within safe limits.", "Talk about one thing you each want to learn or explore.", "Celebrate a difference rather than trying to make your interests match."],
             "prompt": "What is something about you that I am still getting to know?"},
        ],
    },
    "conflict": {
        "name": "The Strong-Willed Duo", "subtitle": "Disagree without disconnecting",
        "strength": "Having your own opinions can be a strength. The aim is to make disagreements feel respectful and repair possible.",
        "insight": "Practising short pauses, reflective listening and meaningful repair can make everyday disagreements easier to navigate.",
        "skill": "Calm disagreement, listening and repair",
        "activities": [
            {"title": "Pause, Hear, Respond", "time": "10 minutes", "supplies": "A timer",
             "steps": ["Choose a light, everyday disagreement—not a painful or unsafe topic.", "One person speaks for one minute; the other reflects what they heard.", "Swap roles, then name one small next step you could both try."],
             "prompt": "What did you wish I had understood before I responded?"},
            {"title": "Our Repair Words", "time": "10 minutes", "supplies": "Paper",
             "steps": ["Separately finish: ‘When we disagree, it helps me when…’", "Share only what feels comfortable.", "Write down two repair phrases you can use after a difficult moment."],
             "prompt": "What does a meaningful apology sound like to you?"},
            {"title": "The Reset Ritual", "time": "5 minutes", "supplies": "None",
             "steps": ["Agree on an optional pause phrase such as ‘Can we reset?’", "Decide how each person can take a brief break while remaining safe.", "Practise with a pretend disagreement."],
             "prompt": "What helps us come back to each other after an argument?"},
        ],
    },
    "openness": {
        "name": "The Quiet Protectors", "subtitle": "Make room for feelings and needs",
        "strength": "Gentleness and thoughtfulness can help relationships feel caring. Difficult emotions deserve room too.",
        "insight": "The next step may be practising honest, low-pressure conversations without needing to solve everything immediately.",
        "skill": "Naming feelings and listening without judgement",
        "activities": [
            {"title": "Weather Report", "time": "7 minutes", "supplies": "Paper or none",
             "steps": ["Each describe your day as weather: sunny, cloudy, stormy or mixed.", "If you wish, explain one reason for your weather.", "The listener responds with curiosity, not solutions."],
             "prompt": "Would you like listening, company or help?"},
            {"title": "One Thing I'd Like You to Know", "time": "10 minutes", "supplies": "Optional note cards",
             "steps": ["Choose a small topic, such as a favourite activity or a stressful school morning.", "Complete: ‘One thing I'd like you to know is…’", "Reflect back what you heard; sharing can be skipped."],
             "prompt": "What helps you feel comfortable telling me things?"},
            {"title": "The Feelings Palette", "time": "15 minutes", "supplies": "Coloured pencils",
             "steps": ["Choose colours for three feelings you experienced this week.", "Draw shapes or patterns for them—no artistic skill needed.", "Share only the parts you want to explain."],
             "prompt": "Can two people feel differently about the same moment?"},
        ],
    },
    "autonomy": {
        "name": "The Loving Guides", "subtitle": "Guide with trust",
        "strength": "Support and guidance are valuable. Growing independence offers new ways to show confidence in each other.",
        "insight": "You might explore when advice is welcome, when listening matters most, and which decisions can be shared.",
        "skill": "Age-appropriate choices, trust and listening before advice",
        "activities": [
            {"title": "The Choice Exchange", "time": "15 minutes", "supplies": "Paper",
             "steps": ["Choose a low-stakes decision such as a weekend activity or outfit.", "The daughter shares what choice she would like and why.", "The mother shares practical considerations; agree on a safe option to try."],
             "prompt": "What would help you feel both trusted and supported?"},
            {"title": "Listen, Help or Advise?", "time": "5 minutes", "supplies": "None",
             "steps": ["The daughter raises a fictional everyday problem.", "The mother asks: ‘Would you like me to listen, help you think, or offer advice?’", "Swap roles using another made-up scenario."],
             "prompt": "When does advice feel helpful, and when does it feel like too much?"},
            {"title": "The Independence Ladder", "time": "15 minutes", "supplies": "Paper and pencils",
             "steps": ["Draw three rungs: choices I make, choices we make together, adult responsibilities.", "Add examples appropriate to your daughter's age.", "Choose one small rung to revisit next week."],
             "prompt": "Which new responsibility would you like to practise?"},
        ],
    },
    "joy": {
        "name": "The Busy but Loving Pair", "subtitle": "More moments of ‘us’",
        "strength": "Everyday care often shows up in practical ways. A few playful moments can add another kind of connection.",
        "insight": "Finding short pockets of shared enjoyment can help your relationship feel like more than schedules and tasks.",
        "skill": "Shared attention, appreciation and play",
        "activities": [
            {"title": "Ten Minutes of Us", "time": "10 minutes", "supplies": "Anything you already enjoy",
             "steps": ["The daughter chooses an easy shared activity.", "Put phones aside; avoid chores, schoolwork and corrections.", "Finish by naming one thing you enjoyed."],
             "prompt": "What is something simple we both look forward to?"},
            {"title": "Small Joy Hunt", "time": "15 minutes", "supplies": "Optional phone camera, used by an adult",
             "steps": ["Go for a walk or look around home for three small beautiful or funny things.", "Notice what each person spots.", "Share why you chose your favourite discovery."],
             "prompt": "What did you notice that I might have missed?"},
            {"title": "Our Weekly Ritual", "time": "10 minutes to plan", "supplies": "Calendar",
             "steps": ["Brainstorm five enjoyable things that cost little or nothing.", "Choose one 15-minute ritual for the coming week.", "Put it in the calendar and take turns choosing in future."],
             "prompt": "What could become ‘our thing’?"},
        ],
    },
}

LIKERT_LABELS = ["Not true", "A little true", "Mostly true", "Very true"]


def score_answers(answers):
    """Return per-domain mean from 1..4 responses, requiring all fifteen answers."""
    if not isinstance(answers, dict):
        raise ValueError("Answers must be a mapping")
    expected = {f"{d['key']}_{n}" for d in DOMAINS for n in range(3)}
    if set(answers) != expected:
        raise ValueError("Please answer all 15 questions")
    if any(type(v) is not int or v not in (1, 2, 3, 4) for v in answers.values()):
        raise ValueError("Answers must be integers between 1 and 4")
    return {d["key"]: sum(answers[f"{d['key']}_{n}"] for n in range(3)) / 3 for d in DOMAINS}


def suggest_pathways(scores):
    """Offer co-equal pathways on a low-score tie; no diagnostic classification."""
    if set(scores) != set(ARCHETYPES):
        raise ValueError("A score for each domain is required")
    minimum = min(scores.values())
    return [d["key"] for d in DOMAINS if abs(scores[d["key"]] - minimum) < 1e-8]


def strongest_dimensions(scores):
    maximum = max(scores.values())
    return [d["key"] for d in DOMAINS if abs(scores[d["key"]] - maximum) < 1e-8]


def demo_answers(perspective):
    """Fictional values for showing funders a walkthrough, not collected participant data."""
    if perspective == "Mother / caregiver":
        values = [[4, 3, 3], [3, 2, 3], [3, 3, 3], [2, 2, 2], [4, 3, 3]]
    else:
        values = [[4, 3, 3], [2, 3, 2], [4, 3, 3], [2, 2, 1], [3, 3, 2]]
    return {f"{domain['key']}_{idx}": val for domain, trio in zip(DOMAINS, values) for idx, val in enumerate(trio)}
