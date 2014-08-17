# -*- coding: utf-8 -*-
"""
    pylit.app
    =========

    Main PyLit application module
"""

import os
import config

TPL_PATH = os.path.abspath(os.path.join(config.BASE_DIR, 'pylit/frontend/templates'))
STATIC_PATH = os.path.abspath(os.path.join(config.BASE_DIR, 'pylit/frontend/static'))
LOG_DIR = os.path.abspath(os.path.join(config.BASE_DIR,'logs'))

from flask import Flask, request
import pylit.frontend.views

class PyLit(Flask):

    def __init__(self, name='pylit', config_file=None, *args, **kw):
        super(PyLit, self).__init__(name, *args, **kw)

        # add configuration data
        self.config.from_pyfile(config.DEFAULT_CONF_PATH)
        if 'PYLIT_CONFIG' in os.environ:
                self.config.from_pyfile(os.environ['PYLIT_CONFIG'])

    def add_logging_handlers(self):
        import logging
        from logging import Formatter
        from logging.handlers import RotatingFileHandler, SMTPHandler

        # Set general log level
        self.logger.setLevel(logging.INFO)

        # Add log file handler (if configured)
        logfile = self.config.get('LOG_FILE')
        path = os.path.abspath(os.path.join(LOG_DIR,logfile))
        print path
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
            template_folder = TPL_PATH,
            static_folder = STATIC_PATH,
            *args, **kw)
    pylit.frontend.views.register(app)
    app.config.update(dict(DEBUG=True))
    
    # add logging to app
    try:
        os.makedirs(LOG_DIR)
    except:
        pass

    app.add_logging_handlers()
    app.logger.info("App created")

    return app

