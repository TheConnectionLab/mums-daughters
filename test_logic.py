import unittest
from logic import ARCHETYPES, score_answers, suggest, profile

class TestLogic(unittest.TestCase):
    def test_scores(self):
        self.assertEqual(score_answers([4]*15), [4.0]*5)
    def test_archetype(self):
        p=profile([3,2.67,3.67,2.33,2.33])
        self.assertEqual(p['archetype']['name'], 'The Loving Guides')
        self.assertEqual(p['growth_indices'], [1,3,4])
    def test_invalid(self):
        with self.assertRaises(ValueError):
            score_answers([0]*15)
    def test_all_archetypes_have_three_activities(self):
        self.assertTrue(all(len(a['activities']) == 3 for a in ARCHETYPES))
if __name__ == '__main__': unittest.main()
