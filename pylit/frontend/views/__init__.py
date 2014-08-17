# -*- coding: utf-8 -*-
"""
    pylit.frontend.views
    ====================

    Blueprints for main view logic
"""

from .home import home_blueprint
from .sitemap import sitemap_blueprint
from .contents import docs_blueprint

def register(app):

    app.register_blueprint(home_blueprint)
    app.register_blueprint(sitemap_blueprint)
    app.register_blueprint(docs_blueprint)
