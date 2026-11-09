"""Deterministic, educational scoring. Not a diagnostic or validated measure."""
DOMAINS = [
    ("Closeness & space", ["I enjoy spending time with my mum or caregiver.", "We can spend time apart without feeling upset.", "My need for privacy is respected."]),
    ("Disagreement & repair", ["We listen to each other when we disagree.", "After an argument, we can reconnect.", "I can disagree without feeling afraid."]),
    ("Emotional openness", ["I can talk about difficult feelings.", "My feelings are taken seriously.", "I can ask for support when I need it."]),
    ("Trust & independence", ["I can make choices that fit my age.", "My opinion matters in decisions that affect me.", "I am trusted to learn from mistakes."]),
    ("Time & enjoyment", ["We enjoy spending time together.", "We have fun without focusing on chores or schoolwork.", "We show appreciation for each other."]),
]
PATHWAYS = [
    ("Together and Apart", "Choose one thing you enjoy together and one thing you each enjoy independently. Discuss how to make space for both."),
    ("Pause, Hear, Respond", "With a small everyday disagreement, each person speaks for one minute and the other first repeats what they heard."),
    ("Feelings Without Fixing", "Ask: 'Do you want me to listen, help you think, or offer advice?' Respond with curiosity first."),
    ("The Choice Exchange", "Identify an age-appropriate choice and discuss what freedom and responsibility could look like."),
    ("Ten Minutes of Us", "Choose a ten-minute activity together, with no phones, corrections or schoolwork talk."),
]

def score_answers(answers):
    if len(answers) != 15 or any(not isinstance(x, int) or x not in (1,2,3,4) for x in answers):
        raise ValueError('Expected 15 integer answers from 1 to 4')
    return [round(sum(answers[i*3:i*3+3])/3, 2) for i in range(5)]

def suggest(scores):
    if len(scores) != 5:
        raise ValueError('Five domain scores required')
    return min(range(5), key=lambda i: scores[i])
