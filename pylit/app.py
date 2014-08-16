import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
LOG_DIR = os.path.abspath(os.path.join(BASEDIR, '../logs'))

from flask import Flask, request
import pylit.frontend.views

class PyLit(Flask):

    def __init__(self, name='pylit', config_file=None, *args, **kw):
        super(PyLit, self).__init__(name, *args, **kw)

    def add_logging_handlers(self):
        import logging
        from logging import Formatter
        from logging.handlers import RotatingFileHandler, SMTPHandler

        # Set general log level
        self.logger.setLevel(logging.INFO)

        # Add log file handler (if configured)
        path = self.config.get('LOGGING_FILE')
        if path:
            file_handler = RotatingFileHandler(path, 'a', 10000, 4)
            file_handler.setLevel(logging.INFO)

            file_formatter = Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
            file_handler.setFormatter(file_formatter)

            self.logger.addHandler(file_handler)
        

def create_app(*args, **kw):
    """Development Application Factory"""
    app = PyLit(
            *args, **kw)
    pylit.frontend.views.register(app)
    app.config.update(dict(DEBUG=True))
    app.config.update(dict(LOGGING_FILE='%s/%s' % (LOG_DIR, 'pylit.log')))
    app.add_logging_handlers()

    app.logger.info("App created")

    return app

