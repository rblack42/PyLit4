import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

from flask import Flask
import pylit.frontend.views

class PyLit(Flask):

    def __init__(self, name='pylit', config_file=None, *args, **kw):
        super(PyLit, self).__init__(name, *args, **kw)

def create_app(*args, **kw):
    """Development Application Factory"""
    app = PyLit(
            *args, **kw)
    pylit.frontend.views.register(app)
    app.config.update(dict(DEBUG=True))
    app.config.update(dict(LOGGING_FILE='%s/%s' % (BASEDIR, 'pylit.log')))

    return app

