import os
import unittest
from pylit.app import create_app

DIR_NAME = os.path.abspath(os.path.dirname(__file__))
LOG_DIR = os.path.abspath(os.path.join(DIR_NAME,'../logs'))

from flask import current_app

class Test_app(unittest.TestCase):

    def setUp(self):
        app = create_app()
        self.app = app.test_client()
 
    def test_entry(self):
        resp = self.app.get('/')
        self.assertTrue('ACC Website' in resp.get_data(as_text=True))

    def test_site_map(self):
        resp = self.app.get('/sitemap')
        self.assertTrue('Site Map' in resp.get_data(as_text=True))

    def test_logging_file(self):
        resp = self.app.get('/')
        try:
            try:
                os.makedirs(LOG_DIR)
            except:
                pass
            log_filename = os.path.join(LOG_DIR, 'pylit.log')
            logfile = open(log_filename)
            isopen = True
        except:
            isopen = False
        self.assertTrue(isopen)

    def test_home_template_dir(self):
        """Check the  template was rendered"""
        resp = self.app.get('/')
        self.assertTrue('ACC Website' in resp.get_data(as_text=True))

    def test_sitemap_template_dir(self):
        """Check the  template was rendered"""
        resp = self.app.get('/sitemap')
        self.assertTrue('Site Map' in resp.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
