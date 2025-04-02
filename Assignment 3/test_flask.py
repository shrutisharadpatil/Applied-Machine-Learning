import unittest
import os
import time
from subprocess import Popen
import requests

class TestFlaskApp(unittest.TestCase):
    import time
from subprocess import Popen
import requests

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.flask_process = Popen(['python3', 'app.py'])
        time.sleep(2)  # Wait for Flask server to start

    def tearDown(self):
        self.flask_process.terminate()

    def test_flask_response(self):
        response = requests.post('http://127.0.0.1:5000/score', json={"text": "test"})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
