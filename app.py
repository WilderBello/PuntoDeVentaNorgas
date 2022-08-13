from flask import Flask, request, flash, render_template, url_for
from forms import Usuarios
from settings.config import configuracion

app = Flask(__name__)
app.config.from_object(configuracion)

@app.route('/')
@app.route('/login')
def login():
    if request.method =='GET':
        form = Usuarios()
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        Username = request.form["Username"]
        Password = request.form["Passsword"]
        return render_template('login.html')

@app.route('/signup')
def signup():
    if request.method =='GET':
        form = Usuarios()
        return render_template('signup.html', form=form)
    elif request.method == 'POST':
        Username = request.form["Username"]
        Password = request.form["Passsword"]
        return render_template('signup.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create', methods=['POST'])
def create_post():
    flash('Pedido registrado correctamente')
    return redirect(url_for('main.create'))

@app.route('/search', methods=['POST'])
def search_post():
    flash('Usuario encontrado correctamente')
    return redirect(url_for('main.search'))