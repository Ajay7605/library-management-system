import unittest
from app import app

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_book(self):
        response = self.app.post('/books', json={
            "title": "Test Book",
            "author": "Author",
            "published_date": "2024-01-01"
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
