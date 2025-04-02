import unittest
import pickle
import requests
import os
import time
from score import score

class TestScore(unittest.TestCase):
    def setUp(self):
        with open("model.pkl", "rb") as f:
            self.model = pickle.load(f)
        self.threshold = 0.5

    def test_smoke(self):
        text = "This is a test text."
        try:
            prediction, propensity = score(text, self.model, self.threshold)
        except Exception as e:
            self.fail(f"score() crashed: {e}")
        self.assertIsNotNone(prediction)
        self.assertIsNotNone(propensity)

    def test_format(self):
        text = "This is a test text."
        prediction, propensity = score(text, self.model, self.threshold)
        self.assertIsInstance(prediction, int)
        self.assertIsInstance(propensity, float)

    def test_prediction_range(self):
        text = "This is a test text."
        prediction, propensity = score(text, self.model, self.threshold)
        self.assertIn(prediction, [0, 1])
        self.assertGreaterEqual(propensity, 0)
        self.assertLessEqual(propensity, 1)

    def test_threshold_0(self):
        text = "This is a test text."
        prediction, _ = score(text, self.model, 0)
        self.assertEqual(prediction, 1)

    def test_threshold_1(self):
        text = "This is a test text."
        prediction, _ = score(text, self.model, 1)
        self.assertEqual(prediction, 0)

class TestFlask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.system("python3 app.py &")
        time.sleep(5)

    def test_flask(self):
        url = "http://127.0.0.1:5000/score"
        data = {"text": "This is a test message."}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertIn("prediction", json_response)
        self.assertIn("propensity", json_response)

    @classmethod
    def tearDownClass(cls):
        os.system("pkill -f 'python3 app.py'")

if __name__ == "__main__":
    unittest.main()

