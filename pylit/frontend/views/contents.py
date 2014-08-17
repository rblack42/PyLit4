import os
import config
from flask import Blueprint, current_app, render_template
from docutils.core import publish_string
from docutils.writers.html4css1 import Writer

basedir = config.BASE_DIR
DOC_DIR = os.path.abspath(os.path.join(basedir, 'docs'))

docs_blueprint = Blueprint('docs', 'pylit')

@docs_blueprint.route('/docs')
def table_of_contents():
    """Render doc TOC"""
    file_list = os.listdir(DOC_DIR)
    docs = []
    for file in file_list:
        if file.endswith('rst'):
            docs.append(file)
    return render_template('contents.jinja', docdir = basedir, docs=docs)

@docs_blueprint.route('/docs/<pagename>')
def render_page(pagename):
    """Render page with docutils"""
    path = os.path.abspath(os.path.join(DOC_DIR, pagename))
    print "rendering: %s" % path
    raw = open(path, 'r').read()
    html_writer = Writer()
    html = publish_string(raw, writer = html_writer)
    return render_template('page.jinja', pagename = pagename, html = html)

