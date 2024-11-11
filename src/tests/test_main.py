# src/tests/test_main.py
import unittest
from main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, Jenkins CD!")

if __name__ == '__main__':
    unittest.main()
