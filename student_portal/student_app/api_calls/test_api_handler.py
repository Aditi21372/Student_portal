import unittest
from .api_handler import APIHandler

class TestAPIHandler(unittest.TestCase):
    def setUp(self):
        self.api_handler = APIHandler("https://jsonplaceholder.typicode.com")  # Example base URL

    def test_get(self):
        response = self.api_handler.get("posts/1")
        self.assertIsNotNone(response)
        self.assertEqual(response['id'], 1)

    def test_post(self):
        data = {"title": "foo", "body": "bar", "userId": 1}
        response = self.api_handler.post("posts", data)
        self.assertIsNotNone(response)
        self.assertEqual(response['title'], "foo")

if __name__ == "__main__":
    unittest.main()
