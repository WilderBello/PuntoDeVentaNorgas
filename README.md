# Project_PuntoDeVenta_PythonFlask

Para ejecutar el proyecto es necesario tener instalado:
- flask
- flask-login
- flask-sqlalchemy

Comandos:

requerimientos: 
  - pip freeze > requirements.txt
  - pip install -r requirements.txt

Entorno Virtual: python3 -m venv ~nombre de la carpeta~

Windows:
  - .\env\Scripts\activate
  - set FLASK_APP=project
  - set FLASK_DEBUG=1
  - flask run
  - .\env\Scripts\deactivate

Linux:
  - source env_linux/bin/activate
  - export FLASK_APP=project
  - export FLASK_DEBUG=1
  - flask run
  - deactivate

Generar base de datos con python:
- from project import db, create_app, models
- db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.

Credenciales de prueba:
  - test@test.com
  - test
