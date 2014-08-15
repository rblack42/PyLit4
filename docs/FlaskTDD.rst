Test Driven Flask Development
#############################

..  _TravisCI:  http://travis-ci.org/
..  _Github:    http://github.com/

Starting up a new project is always an interesting time. You need to create an
environment for your new project that can be tested immediately. In this note,
we will set up a Python Flask project that can be tested continuously using
TravisCI, a free testing service for projects on Github_.

Creating a Base Flask Project
*****************************

The simplest Flask_ project looks like this:

..  code-block:: python

    from flask import Flask

    app = Flask(__name__)
 
    @app.route('/')
    def index():
        return "Hello, World"

    if __name__ == '__main__':
        app.run(debug=True)

This application does not generate any HTML output, but the application will run and generate output we can see using a web browser.

To run this application, do this:

..  code-block:: text

    (_venv)$ python pylit.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader

Now, point your web browser at http://127.0.0.1:5000 and you should see "Hello,
World" displayed on the screen.

Setting up the Initial Test
***************************

Assuming :program:`nose` is installed, we can test this application by setting
up a simple test script that will run the application and fetch the HTML output
from the server. Create a `tests` directory under the project root, and create
`test_app.py`:

..  code-block:: python

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

Running the Tests
=================

:program:`nose` provides a tool (:program:`nosetests`) that will search for
test scripts (with names beginning with the string "test") and run them. Here
is what you should see:

..  code-block:: text

    (_venv$ nosetests
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.075s

    OK

With this setup, we are ready to begin development using :term:`TDD`. 
