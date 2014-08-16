import unittest
from pylit.app import create_app
 
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
            fout = open('debug','w')
            log_filename = '/Users/rblack/_projects/PyLit4/logs/pylit.log'
            logfile = open(log_filename)
            isopen = True
        except:
            isopen = False
        self.assertTrue(isopen)

if __name__ == '__main__':
    unittest.main()
