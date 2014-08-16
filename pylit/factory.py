# -*- coding: utf-8 -*-
"""
    pylit.factory
    =============

    PyLit application factory
"""

from flask import Flask

def create_app(package_name):
    app = Flask(package_name)
    app.debug = True

    @app.route('/')
    def index():
        return "Hello, World"

    @app.route('/sitemap')
    def site_map():
        links = app.url_map
        return str(links)

    return app
