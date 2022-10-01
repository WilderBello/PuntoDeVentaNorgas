from __future__ import print_function
from flask import Flask, request, flash, render_template, url_for, redirect, session, g
from forms import Borrar, Usuarios, Crear, Buscar, Modificar
from settings.config import configuracion
import basededatos as db
from flask_bcrypt import Bcrypt

from POO.Vendedor import Vendedor
from POO.Cliente import Cliente

app = Flask(__name__)
app.config.from_object(configuracion)
bcrypt = Bcrypt(app)

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
            return redirect(url_for('login'))
        else:
            nombre = valor[3]
            
            global Datos_Vendedor
            Datos_Vendedor = Vendedor(nombre, Correo)
            
            session['username'] = nombre
            session['email'] = Correo
            
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
    session.clear()
    return redirect(url_for('login'))

@app.route('/home')
def home():
    if 'username' in session:
        user = session['username']
        return render_template('home.html', username = user)
    else:
        flash('Error, debe iniciar sesion.')
        return redirect(url_for('login'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method =='GET':
        if 'username' in session:
            form = Buscar()
            datos = [('Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null')]
            return render_template('search.html', form = form, DatosUsuario = datos, usuario_existe = False)
        else:
            flash('Error, debe iniciar sesión.')
            return redirect(url_for('login'))
        
    elif request.method == 'POST':
        Usuario = request.form["Cliente"]
        datos = db.sql_select_usuario(Usuario)
        print(datos)
        if datos == []:
            flash('Error, usuario no encontrado.')
            datos = [('Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null','Null')]
            
            return redirect(url_for('search'))
        else: 
            form = Buscar()
            
            i = (len(datos)) - 1
            
            global Datos_Cliente 
            Datos_Cliente = Cliente(datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5], datos[i][7], datos[i][8], datos[i][9], datos[i][10], datos[i][12], datos[i][13])
            print(Datos_Cliente)
            flash('Usuario encontrado correctamente')
            
            return render_template('search.html', form = form, DatosUsuario = datos, usuario_existe = True)

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = Crear()
    if request.method =='GET':
        if 'username' in session:
            return render_template('create.html', form = form)
        else:
            flash('Error, debe iniciar sesión.')
            return redirect(url_for('login'))
        
    elif request.method == 'POST':
        nombre_vendedor = Datos_Vendedor.get_name()
        print(nombre_vendedor)
        
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
        
        db.sql_crear_pedido(fecha_pedido, referencia_producto)
        id_pedido_data = db.sql_select_id(fecha_pedido)
        id_pedido = id_pedido_data[len(id_pedido_data)-1][0]
        
        datos = db.sql_select_usuario(id_cliente)
        if datos == []:
            db.sql_agregar_cliente(id_cliente, nombre_completo, telefono, direccion)
        
        db.sql_agregar_pedido(id_cliente, nombre_completo, telefono, direccion, referencia_producto, num_producto, estado_producto, deuda, anotaciones, id_pedido, nombre_vendedor, fecha_pedido)
        
        flash('Pedido registrado correctamente')
        return redirect(url_for('create'))

@app.route('/about')
def about():
    if 'username' in session:
        return render_template('about.html')
    else:
        flash('Error, debe iniciar sesión.')
        return redirect(url_for('login'))

@app.route('/modify', methods=['GET', 'POST'])
def modificar():
    form = Modificar()
    if request.method =='GET':
        if 'username' in session:
            usuario = [Datos_Cliente.get_id_pedido(), Datos_Cliente.get_document(), Datos_Cliente.get_name(), Datos_Cliente.get_telf(), Datos_Cliente.get_direccion(), Datos_Cliente.get_ref(), Datos_Cliente.get_fecha_pedido(), Datos_Cliente.get_estado(), Datos_Cliente.get_deuda(), Datos_Cliente.get_anotacion()]
            print(usuario)
            return render_template('modify.html', form = form, datos = usuario)
        else:
            flash('Error, debe iniciar sesión.')
            return redirect(url_for('login'))
        
    if request.method == 'POST':
        
        nombre_vendedor = Datos_Vendedor.get_name()
        id_pedido = request.form["Id_pedido"]
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
        
        db.sql_update(id_cliente, nombre_completo, telefono, direccion, referencia_producto, num_producto, estado_producto, deuda, anotaciones, id_pedido, nombre_vendedor, fecha_pedido)
        
        flash('Pedido modificado correctamente')
        return redirect(url_for('search'))

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = Borrar()
    pedido = Datos_Cliente.get_id_pedido()
    if request.method =='GET':
        return render_template('delete.html', form=form, id_pedido=pedido)
    
    if request.method == 'POST':
        db.sql_delete(pedido)
        flash('Pedido eliminado correctamente')
        return redirect(url_for('search'))


if __name__=='__main__':
    app.run(debug=True)
    
def api():
    pass