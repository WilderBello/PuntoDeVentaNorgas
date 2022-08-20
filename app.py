from flask import Flask, request, flash, render_template, url_for, redirect, session
from forms import Usuarios, Crear, Buscar
from settings.config import configuracion
import basededatos as db
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(configuracion)
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        session.pop('username')
    form = Usuarios()
    if request.method =='GET':
        return render_template('login.html', form = form)
    elif request.method == 'POST':
        Correo = request.form["Correo"]
        Password = request.form["Password"]
        
        valor = db.sql_login(Correo, Password)
        
        if valor == False:
            flash('Correo y/o Password incorrect.')
            return redirect(url_for('login'))
        else:
            session['username'] = valor[3]
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
        
        pw_hash = bcrypt.generate_password_hash(password=Password).decode('utf8')
        
        data = db.sql_signup(Correo, Username, pw_hash)
        
        if data == 'signup':
            flash(f"El usuario {Username} fue creado correctamente.")
            return redirect(url_for('signup'))
        else:
            flash('Error, el usuario {Username} ya existe.')
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

@app.route('/search', methods=['GET'])
def search():
    form = Buscar()
    if 'username' in session:
        datos = [('Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null')]
        return render_template('search.html', form = form, DatosUsuario = datos)
    else:
        flash('Error, debe iniciar sesión.')
        return redirect(url_for('login'))

@app.route('/create', methods=['GET'])
def create():
    form = Crear()
    if 'username' in session:
        return render_template('create.html', form = form)
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

@app.route('/search', methods=['POST'])
def search_post():
    form = Buscar()
    Usuario = request.form["Cliente"]
    datos = db.sql_select_usuario(Usuario)
    print(datos)
    if datos == []:
        flash('Error, usuario no encontrado.')
        datos = [('Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null')]
        return redirect(url_for('search'))
    else: 
        flash('Usuario encontrado correctamente')
        return render_template('search.html', form = form, DatosUsuario = datos)

@app.route('/create', methods=['POST'])
def create_post():
    form = Crear()
    
    nombre_vendedor = ''
    if 'username' in session:
        nombre_vendedor = session['username']
        
    id_cliente = request.form["Documento"]
    nombre_completo = request.form["Nombre"]
    telefono = request.form["Telefono"]
    direccion = request.form["Direccion"]
    referencia_producto = form.Referencia.data
    fecha_pedido = form.Fecha.data
    num_producto = form.Numero.data
    estado_producto = form.Estado.data
    deuda = request.form["Deuda"]
    anotaciones = request.form["Anotaciones"]
    
    id_pedido = db.sql_pedido(fecha_pedido, referencia_producto)
    id_pedido = id_pedido[0]
    
    db.sql_agregar_pedido(id_cliente, nombre_completo, telefono, direccion, referencia_producto, num_producto, estado_producto, deuda, anotaciones, id_pedido, nombre_vendedor, fecha_pedido)
    flash('Pedido registrado correctamente')
    return redirect(url_for('create'))

if __name__=='__main__':
    app.run(debug=True)