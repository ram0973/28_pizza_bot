from app import create_app
import unittest


class ErrorTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_page_not_found_status_code(self):
        result = self.client.get('/missing-page')
        self.assertEqual(result.status_code, 404)

    def test_page_not_found_data(self):
        result = self.client.get('/missing-page')
        self.assertIn(b'Page not found', result.data)

