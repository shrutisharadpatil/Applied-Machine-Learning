import unittest
import joblib
from score import score

class TestScoreFunction(unittest.TestCase):
    def setUp(self):
        self.model = joblib.load('model.pkl')

    def test_score_smoke(self):
        result = score("Sample text", self.model, 0.5)
        self.assertIsInstance(result, tuple)

    def test_score_format(self):
        result = score("Sample text", self.model, 0.5)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], float)

    def test_prediction_value(self):
        result = score("Sample text", self.model, 0.5)
        self.assertIn(result[0], [0, 1])

    def test_propensity_range(self):
        result = score("Sample text", self.model, 0.5)
        self.assertGreaterEqual(result[1], 0)
        self.assertLessEqual(result[1], 1)

    def test_threshold_behavior(self):
        result_0 = score("Sample text", self.model, 0)
        result_1 = score("Sample text", self.model, 1)
        self.assertEqual(result_0[0], 1)
        self.assertEqual(result_1[0], 0)

    def test_obvious_spam(self):
        result = score("Congratulations, you've won a lottery!", self.model, 0.5)
        self.assertEqual(result[0], 1)

    def test_obvious_non_spam(self):
        result = score("Meeting at 2 PM tomorrow.", self.model, 0.5)
        self.assertEqual(result[0], 0)

if __name__ == '__main__':
    unittest.main()
