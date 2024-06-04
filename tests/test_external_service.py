import unittest
import requests
from unittest.mock import patch

class ExternalServiceTests(unittest.TestCase):

    @patch('requests.get')
    def test_jsonplaceholder_posts_contract(self, mock_get):
        mock_get.return_value.json.return_value = [
            {'userId': 1, 'id': 1, 'title': 'Post title', 'body': 'Post body'}
        ]
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertIn('userId', data[0])
        self.assertIn('id', data[0])
        self.assertIn('title', data[0])
        self.assertIn('body', data[0])

    @patch('requests.get')
    def test_jsonplaceholder_albums_contract(self, mock_get):
        mock_get.return_value.json.return_value = [
            {'userId': 1, 'id': 1, 'title': 'Album title'}
        ]
        response = requests.get('https://jsonplaceholder.typicode.com/albums')
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertIn('userId', data[0])
        self.assertIn('id', data[0])
        self.assertIn('title', data[0])

if __name__ == '__main__':
    unittest.main()
