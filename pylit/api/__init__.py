# -*- coding: utf-8 -*-
"""
    pylit.api
    =========

    PyLit4 application programm interface
"""

from .. import factory

def create_app():

    app = factory.create_app(__name__)

    return app
