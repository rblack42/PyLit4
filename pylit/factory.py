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
        links = []
        reply = '<html><body>Site Map<br>========<br>'
        for rule in app.url_map.iter_rules():
            endpoint = rule.endpoint
            reply += '%s -> %s<br>' % (str(rule), endpoint)
        reply += '<br></body></html>'
        return reply

    return app
