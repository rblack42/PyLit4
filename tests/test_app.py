import unittest
from pylit.api import create_app
 
class Test_app(unittest.TestCase):

    def setUp(self):
        app = create_app()
        self.app = app.test_client()
 
    def test_entry(self):
        resp = self.app.get('/')
        self.assertTrue('Hello' in resp.get_data(as_text=True))

    def test_site_map(self):
        resp = self.app.get('/sitemap')
        self.assertTrue('Site Map' in resp.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
