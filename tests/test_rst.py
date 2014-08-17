import os
import unittest
from pylit.app import create_app

DIR_NAME = os.path.abspath(os.path.dirname(__file__))
LOG_DIR = os.path.abspath(os.path.join(DIR_NAME,'../docs'))

class Test_rst(unittest.TestCase):

    def setUp(self):
        app = create_app()
        self.app = app.test_client()
 
    def test_toc(self):
        """Test TOC generation"""
        resp = self.app.get('/docs')
        self.assertTrue('Table of Contents' in resp.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
