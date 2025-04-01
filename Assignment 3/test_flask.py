import unittest
import os
import time
from subprocess import Popen
import requests

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.flask_process = Popen(['python', 'app.py'])
        time.sleep(2)

    def tearDown(self):
        self.flask_process.terminate()

    def test_flask_response(self):
        url = "http://127.0.0.1:5000/score"
        data = {'text': 'Sample text', 'threshold': 0.5}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIn('prediction', result)
        self.assertIn('propensity', result)

if __name__ == '__main__':
    unittest.main()
