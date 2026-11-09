import unittest
from logic import score_answers, suggest

class TestLogic(unittest.TestCase):
    def test_all_four(self):
        self.assertEqual(score_answers([4]*15), [4.0]*5)
    def test_recommendation(self):
        self.assertEqual(suggest([4,3,2,4,4]), 2)
    def test_invalid(self):
        with self.assertRaises(ValueError):
            score_answers([0]*15)
if __name__ == '__main__':
    unittest.main()
