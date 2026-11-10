import unittest
from kirilli_logic import ARCHETYPES, DOMAINS, demo_answers, score_answers, suggest_pathways, strongest_dimensions


class LogicTests(unittest.TestCase):
    def test_fictional_example(self):
        scores = score_answers(demo_answers("Daughter"))
        self.assertEqual(len(scores), 5)
        self.assertEqual(suggest_pathways(scores), ["autonomy"])
        self.assertEqual(ARCHETYPES["autonomy"]["name"], "The Loving Guides")

    def test_mother_example(self):
        scores = score_answers(demo_answers("Mother / caregiver"))
        self.assertEqual(suggest_pathways(scores), ["autonomy"])

    def test_equal_scores_give_multiple_pathways(self):
        answers = {f"{d['key']}_{i}": 3 for d in DOMAINS for i in range(3)}
        scores = score_answers(answers)
        self.assertEqual(len(suggest_pathways(scores)), 5)
        self.assertEqual(len(strongest_dimensions(scores)), 5)

    def test_missing_rejected(self):
        with self.assertRaises(ValueError):
            score_answers({})

    def test_invalid_rejected(self):
        a = demo_answers("Daughter")
        a["joy_0"] = 5
        with self.assertRaises(ValueError):
            score_answers(a)

    def test_all_pathways_have_three_activities(self):
        for p in ARCHETYPES.values():
            self.assertEqual(len(p["activities"]), 3)
            for activity in p["activities"]:
                self.assertEqual(len(activity["steps"]), 3)

if __name__ == "__main__":
    unittest.main()
