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
        test_page = self.client.get('/missing-page')
        self.assertEqual(test_page.status_code, 404)

    def test_page_not_found_data(self):
        test_page = self.client.get('/missing-page')
        self.assertIn(b'Page not found', test_page.data)
