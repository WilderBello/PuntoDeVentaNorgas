from unicodedata import name
from flask import Blueprint, render_template
from flask_login import current_user, login_required
from . import db

main = Blueprint('main', __name__)

@main.route('/home')
@login_required
def home():
    return render_template('home.html', name=current_user.name)

@main.route('/search')
@login_required
def search():
    return render_template('search.html')

@main.route('/create')
@login_required
def create():
    return render_template('create.html')

@main.route('/about')
@login_required
def about():
    return render_template('about.html')