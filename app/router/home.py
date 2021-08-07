from flask import Blueprint, render_template
from config import template_folder

bp = Blueprint('home', __name__, template_folder=template_folder)


@bp.route('/')
def render():
    return render_template('home.html', title='Home')
    # return '<h1>Hello, world!</h1>'
