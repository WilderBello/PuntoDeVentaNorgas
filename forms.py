from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, EmailField, SelectField, SearchField, RadioField
from wtforms.validators import DataRequired

class Usuarios(FlaskForm):
    Correo = EmailField('Correo', validators=[DataRequired()], id="user")
    Username = StringField('Username', validators=[DataRequired()], id="name")
    Password = StringField('Password', validators=[DataRequired()], id="password")
    iniciar = SubmitField('Iniciar Sesión')
    enviar = SubmitField('Registrarse')
    
class Crear(FlaskForm):
    Documento = StringField('Documento cliente:', validators=[DataRequired()], id="id_cliente")
    Nombre = StringField('Nombre de cliente:', validators=[DataRequired()], id="name_cliente")
    Telefono = StringField('Teléfono:', validators=[DataRequired()], id="telefone_cliente")
    Direccion = StringField('Dirección de cliente:', validators=[DataRequired()], id="direccion_cliente")
    Referencia = SelectField('Referencia:', validate_choice=True, choices=['60LB','80LB','100LB'], id="referencia_producto")   
    Fecha = DateField('Fecha:', validators=[DataRequired()], id="fecha_pedido")
    Numero = SelectField('Numero de productos:', validate_choice=True, choices=[1,2,3,4,5], coerce=int, id="num_productos")
    Estado = SelectField('Estado del producto:', validate_choice=True, choices=[('Tiene'), ('No Tiene')], id="estado_producto")
    Deuda = StringField('Deuda:', validators=[DataRequired()], id="deuda")
    Anotaciones = StringField('Anotaciones:', id="anotaciones")
    Crear = SubmitField('Crear Pedido')
    
class Buscar(FlaskForm):
    Cliente = SearchField('Documento:', validators=[DataRequired()], id="buscar_cliente_bd")
    Buscar = SubmitField('Buscar')
class Modificar(FlaskForm):
    Id_pedido = SelectField('Modificar Pedido Número:', validate_choice=True, choices=[], id="Id_pedido")   
    Documento = StringField('Documento cliente:', validators=[DataRequired()], id="id_cliente")
    Nombre = StringField('Nombre de cliente:', validators=[DataRequired()], id="name_cliente")
    Telefono = StringField('Teléfono:', validators=[DataRequired()], id="telefone_cliente")
    Direccion = StringField('Dirección de cliente:', validators=[DataRequired()], id="direccion_cliente")
    Referencia = SelectField('Referencia:', validate_choice=True, choices=['60LB','80LB','100LB'], id="referencia_producto")   
    Fecha = DateField('Fecha:', validators=[DataRequired()], id="fecha_pedido")
    Numero = SelectField('Numero de productos:', validate_choice=True, choices=[1,2,3,4,5], coerce=int, id="num_productos")
    Estado = SelectField('Estado del producto:', validate_choice=True, choices=[('Tiene'), ('No Tiene')], id="estado_producto")
    Deuda = StringField('Deuda:', validators=[DataRequired()], id="deuda")
    Anotaciones = StringField('Anotaciones:', id="anotaciones")
    Modificar = SubmitField('Modificar Pedido')

class Borrar(FlaskForm):
    Delete = SubmitField('Eliminar definitivamente.')