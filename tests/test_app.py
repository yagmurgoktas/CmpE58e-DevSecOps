import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        response = self.client.get("/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, DevSecOps!"})
    
    def test_bye(self):
        response = self.client.get("/bye")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Bye, DevSecOps!"})

if __name__ == "__main__":
    unittest.main()

