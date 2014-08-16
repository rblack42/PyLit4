#!_venv/bin/python
# -*- coding: utf-8 -*-
"""
    manager
    =======

    Manager script for pylit
"""

from flask.ext.script import Manager

from pylit.api import create_app

manager = Manager(create_app())

if __name__ == '__main__':
    manager.run() 
