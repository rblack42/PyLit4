from flask import Blueprint

home_blueprint = Blueprint('home', 'pylit')

HOME_PAGE_TPL = '<html><body><h1>ACC Website</h1><p><a href="/sitemap">Site Map</a></p></body</html>'

@home_blueprint.route('/')
def home():
    return HOME_PAGE_TPL
