import unittest
from unittest.mock import patch
from main import app

class ContractTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.client = app.test_client()

    @patch('main.requests.get')
    def test_posts_contract(self, mock_get):
        mock_get.return_value.json.return_value = [
            {'id': 1, 'title': 'Test Post', 'body': 'This is a test post.'}
        ]
        response = self.client.post('/posts', data={
            'num_posts': 1,
            'num_comments': 1,
            'max_chars': 100
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('posts', data)
        self.assertIsInstance(data['posts'], list)
        self.assertEqual(len(data['posts']), 1)
        self.assertIn('id', data['posts'][0])
        self.assertIn('title', data['posts'][0])
        self.assertIn('body', data['posts'][0])

    @patch('main.requests.get')
    def test_albums_contract(self, mock_get):
        mock_get.return_value.json.return_value = [
            {'id': 1, 'title': 'Test Album'}
        ]
        response = self.client.post('/albums', data={
            'num_albums': 1,
            'num_photos': 1
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('albums', data)
        self.assertIsInstance(data['albums'], list)
        self.assertEqual(len(data['albums']), 1)
        self.assertIn('id', data['albums'][0])
        self.assertIn('title', data['albums'][0])
        self.assertIn('photos', data['albums'][0])
        self.assertIsInstance(data['albums'][0]['photos'], list)

if __name__ == '__main__':
    unittest.main()
