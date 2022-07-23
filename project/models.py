from unicodedata import name
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)# primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True, nullable=False) 
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000), nullable=False)
    conexion = db.relationship('Prueba', backref='user', lazy=True)
    
class Prueba(db.Model):
    id_prueba = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)