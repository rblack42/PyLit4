# -*- coding: utf-8 -*-
"""
    config
    ======

    PyLit configuration package
"""

import sys
from flask.ext.script import Manager

from pylit.app import create_app
from config import to_envvar

def _create_app(config):
    if not to_envvar(config):
        print 'Config file "{}" not found.'.format(config)
        sys.exit(1)
    return create_app()

manager  = Manager(_create_app)
manager.add_option('-c', '--config', dest='config', required=False)
