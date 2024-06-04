import unittest
from unittest.mock import patch
from main import app

class MainTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.client = app.test_client()

    @patch('main.requests.get')
    def test_index(self, mock_get):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    @patch('main.requests.get')
    def test_posts(self, mock_get):
        mock_get.return_value.json.return_value = [
            {'id': 1, 'title': 'Test Post', 'body': 'This is a test post.'}
        ]
        response = self.client.post('/posts', data={
            'num_posts': 1,
            'num_comments': 1,
            'max_chars': 100
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Post', response.data)
        self.assertIn(b'This is a test post.', response.data)

    @patch('main.requests.get')
    def test_post_detail(self, mock_get):
        mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: {'id': 1, 'title': 'Test Post', 'body': 'This is a test post.'}),
            unittest.mock.Mock(json=lambda: [{'id': 1, 'body': 'Test Comment'}])
        ]
        response = self.client.get('/posts/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Post', response.data)
        self.assertIn(b'This is a test post.', response.data)
        self.assertIn(b'Test Comment', response.data)

    @patch('main.requests.get')
    def test_albums(self, mock_get):
        mock_get.return_value.json.return_value = [
            {'id': 1, 'title': 'Test Album'}
        ]
        response = self.client.post('/albums', data={
            'num_albums': 1,
            'num_photos': 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Album', response.data)

    @patch('main.requests.get')
    def test_album_detail(self, mock_get):
        mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: {'id': 1, 'title': 'Test Album'}),
            unittest.mock.Mock(json=lambda: [{'id': 1, 'title': 'Test Photo', 'url': 'http://example.com/photo.jpg'}])
        ]
        response = self.client.get('/albums/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Album', response.data)
        self.assertIn(b'Test Photo', response.data)

    @patch('main.requests.get')
    def test_posts_error(self, mock_get):
        mock_get.side_effect = Exception("API error")
        response = self.client.post('/posts', data={
            'num_posts': 1,
            'num_comments': 1,
            'max_chars': 100
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error fetching posts', response.data)

    @patch('main.requests.get')
    def test_albums_error(self, mock_get):
        mock_get.side_effect = Exception("API error")
        response = self.client.post('/albums', data={
            'num_albums': 1,
            'num_photos': 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error fetching albums', response.data)

    @patch('main.requests.get')
    def test_post_detail_error(self, mock_get):
        mock_get.side_effect = Exception("API error")
        response = self.client.get('/posts/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error fetching post detail', response.data)

    @patch('main.requests.get')
    def test_album_detail_error(self, mock_get):
        mock_get.side_effect = Exception("API error")
        response = self.client.get('/albums/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error fetching album detail', response.data)

if __name__ == '__main__':
    unittest.main()
