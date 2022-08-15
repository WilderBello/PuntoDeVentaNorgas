from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Usuarios(FlaskForm):
    Id = StringField('Id', validators=[DataRequired()])
    Nombres = StringField('Nombres', validators=[DataRequired()])
    Apellidos = StringField('Apellidos', validators=[DataRequired()])
    Celular = StringField('Celular', validators=[DataRequired()])
    Correo = StringField('Correo', validators=[DataRequired()], id="user")
    Username = StringField('Username', validators=[DataRequired()], id="name")
    Password = StringField('Password', validators=[DataRequired()], id="password")
    iniciar = SubmitField('Iniciar Sesión')
    enviar = SubmitField('Registrarse')