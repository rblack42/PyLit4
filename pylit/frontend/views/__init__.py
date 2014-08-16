# -*- coding: utf-8 -*-
"""
    pylit.frontend.views
    ====================

    Blueprints for main view logic
"""

from .home import home_blueprint
from .sitemap import sitemap_blueprint

def register(app):

    app.register_blueprint(home_blueprint, prefix='home')
    app.register_blueprint(sitemap_blueprint, prefix='sitemap')
