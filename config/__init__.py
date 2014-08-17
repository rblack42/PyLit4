# -*- coding: utf-8 -*-
"""
    config
    ======

    Basic configuration module for PyLit
"""

import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))

PRODUCTION_CONF_PATH = '/etc/pylit/production.py'
DEFAULT_CONF_PATH = os.path.join(BASE_DIR, 'config', 'default.py')
TESTING_CONF_PATH = os.path.join(BASE_DIR, 'config', 'testing.py')

def to_envvar(path=None):
    """
    Loads the application configuration from a file.
    Returns the configuration or None if no configuration could be found.
    """

    if path:
        path = os.path.abspath(path)
        if not os.path.exists(path):
            return
    elif os.path.exists(PRODUCTION_CONF_PATH):
        path = PRODUCTION_CONFIGURATION_PATH
    else:
        return True

    os.environ['PYLIT_CONFIG'] = path
    return True
