import unittest
import pylit
 
class Test_app(unittest.TestCase):

    def setUp(self):
        self.app = pylit.app.test_client()
 
    def test_entry(self):
        resp = self.app.get('/')
        self.assertTrue('Hello' in resp.get_data(as_text=True))
 
if __name__ == '__main__':
    unittest.main()
