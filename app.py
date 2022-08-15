from flask import Flask, request, flash, render_template, url_for, redirect, g, session
from forms import Usuarios
from settings.config import configuracion
import basededatos as db

app = Flask(__name__)
app.config.from_object(configuracion)
app.secret_key = 'asdsfsfwre'

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Usuarios()
    if request.method =='GET':
        return render_template('login.html', form = form)
    elif request.method == 'POST':
        Correo = request.form["Correo"]
        Password = request.form["Password"]
        
        valor = db.sql_login(Correo, Password)
        
        if valor == False:
            flash('Correo y/o Password incorrect.')
            return render_template('login.html', form = form)
        else:
            name = valor[0]
            usuario = name[0]
            session['username'] = usuario
            return redirect(url_for('home'))
        
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Usuarios()
    if request.method =='GET':
        return render_template('signup.html', form = form)
    elif request.method == 'POST':
        Correo = request.form["Correo"]
        Username = request.form["Username"]
        Password = request.form["Password"]
        
        data = db.sql_signup(Correo, Username, Password)
        
        if data == 'signup':
            flash('Usuario creado correctamente.')
            return redirect(url_for('signup'))
        else:
            flash('Error, el usuario ya existe.')
            return redirect(url_for('signup'))

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

@app.route('/home')
def home():
    if 'username' in session:
        user = session['username']
        return render_template('home.html', username = user)
    else:
        flash('Error, debe iniciar sesion.')
        return redirect(url_for('login'))

@app.route('/search')
def search():
    if 'username' in session:
        return render_template('search.html')
    else:
        flash('Error, debe iniciar sesión.')
        return redirect(url_for('login'))

@app.route('/create')
def create():
    if 'username' in session:
        return render_template('create.html')
    else:
        flash('Error, debe iniciar sesión.')
        return redirect(url_for('login'))
    

@app.route('/about')
def about():
    if 'username' in session:
        return render_template('about.html')
    else:
        flash('Error, debe iniciar sesión.')
        return redirect(url_for('login'))
    

@app.route('/create', methods=['POST'])
def create_post():
    flash('Pedido registrado correctamente')
    return redirect(url_for('create'))

@app.route('/search', methods=['POST'])
def search_post():
    flash('Usuario encontrado correctamente')
    return redirect(url_for('search'))

if __name__=='__main__':
    app.run(debug=True)