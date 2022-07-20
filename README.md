# Use_Python_Flask

Para ejecutar el proyecto es necesario tener instalado:
- flask
- flask-login
- flask-sqlalchemy

Comandos:
  - .\env\Scripts\activate
  - flask run
  - 
Generar base de datos con python:
- from project import db, create_app, models
- db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
