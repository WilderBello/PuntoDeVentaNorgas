import sqlite3 as sql
from sqlite3 import Error
from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

def sql_connection():
    try:
        con = sql.connect('DataBase.db')
        return con
    except Error:
        print(Error)

def sql_login(correo, password):
    str_sql = f"SELECT * FROM Credenciales WHERE correo = '{correo}';"
    print(str_sql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(str_sql)
    
    datos = cursor_Obj.fetchall()
    
    if datos != []:
        if bcrypt.check_password_hash(datos[0][2], password) == True:
            print("Welcome")
            con.close()
            return datos[0]
        else:
            return False
    else:
        print("Login failed")
        con.close()
        return False

def sql_signup(Correo, Username, Password):
    str_sql = f"INSERT INTO Credenciales(correo, password, username) VALUES('{Correo}', '{Password}', '{Username}');"
    print(str_sql)
    
    try:
        con = sql_connection()
        cursor_Obj = con.cursor()
        cursor_Obj.execute(str_sql)
        con.commit()
        con.close()
        return 'signup'
    except Error:
        print(Error)
        return 'Error'
    
def sql_select_usuario(usuario):
    str_sql = f"SELECT * FROM BaseDeDatos WHERE id_cliente='{usuario}'"
    print(str_sql)
    
    try:
        con = sql_connection()
        cursor_Obj = con.cursor()
        cursor_Obj.execute(str_sql)
        datos = cursor_Obj.fetchall()
        con.close()
        return datos
    except Error:
        print(Error)
        return 'Error'
    
def sql_agregar_pedido(id_cliente, nombre_completo, telefono, direccion, referencia_producto, num_producto, estado_producto, deuda, anotaciones, id_pedido, nombre_vendedor, fecha_pedido):
    
    sql_agregar_cliente(id_cliente, nombre_completo, telefono, direccion)
    sql_update_cantidad(referencia_producto, num_producto)
    id_departamento = 1010
    id_emp = sql_emp()
    sql_venta(id_emp, id_departamento, id_cliente)
    # id_pedido id_departamento
    str_sql = f"INSERT INTO BaseDeDatos (id_cliente, nombre_completo, telefono, direccion, referencia_producto, num_producto, estado_producto, deuda, anotaciones, nombre_vendedor, id_departamento, id_pedido, fecha_pedido) VALUES ('{id_cliente}', '{nombre_completo}', '{telefono}', '{direccion}','{referencia_producto}', '{num_producto}', '{estado_producto}', '{deuda}', '{anotaciones}', '{nombre_vendedor}', '{id_departamento}', '{id_pedido}', '{fecha_pedido}');"
    try:
        con = sql_connection()
        cursor_Obj = con.cursor()
        cursor_Obj.execute(str_sql)
        con.commit()
        con.close()
    except Error:
        return 'Error'

def sql_agregar_cliente(id_cliente, nombre_completo, telefono, direccion):
    str_sql = f"INSERT INTO Cliente (id_cli, nombre_cli, telefono_cli, direccion_cli) values ('{id_cliente}', '{nombre_completo}', '{telefono}', '{direccion}');"
    try:
        con = sql_connection()
        cursor_Obj = con.cursor()
        cursor_Obj.execute(str_sql)
        con.commit()
        con.close()
    except Error:
        return 'Error'

def sql_update_cantidad(referencia_producto, num_producto):
    pass

def sql_pedido(fecha_pedido, referencia_producto):
    str_sql = f"INSERT INTO Pedido (fecha_pedido_now, referencia_producto) VALUES ({fecha_pedido}, {referencia_producto});"
    str_sql_id = f"SELECT id_pedido_now FROM Pedido WHERE id_pedido_now=(SELECT max(id_pedido_now) FROM Pedido);"
    
    try:
        con = sql_connection()
        cursor_Obj = con.cursor()
        cursor_Obj.execute(str_sql)
        con.commit()
        con.close()
        
        con = sql_connection()
        cursor_Obj = con.cursor()
        cursor_Obj.execute(str_sql_id)
        datos = cursor_Obj.fetchall()
        con.close()
        return datos[0]
    except Error:
        return 'Error'


def sql_emp():
    pass

def sql_venta(id_emp, id_departamento, id_cliente):
    pass