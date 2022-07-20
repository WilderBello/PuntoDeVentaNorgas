from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
class Prueba(UserMixin, db.Model):
    id_prueba = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(1000))
    edad = db.Column(db.Integer, foreign_key=True, not_null=True)