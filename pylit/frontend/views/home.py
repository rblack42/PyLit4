from flask import Blueprint, render_template

home_blueprint = Blueprint('home', 'pylit')

@home_blueprint.route('/')
def home():
    return render_template('home.jinja', instructor = 'Roie Black')
