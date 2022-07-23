from unicodedata import name
from flask import Blueprint, redirect, render_template,url_for, flash
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

@main.route('/create', methods=['POST'])
def create_post():
    flash('Pedido registrado correctamente')
    return redirect(url_for('main.create'))

@main.route('/search', methods=['POST'])
def search_post():
    flash('Usuario encontrado correctamente')
    return redirect(url_for('main.search'))