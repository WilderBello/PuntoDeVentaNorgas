import sqlite3 as sql
from sqlite3 import Error

def sql_connection():
    try:
        con = sql.connect('DataBase.db')
        return con
    except Error:
        print(Error)

def sql_login(correo, password):
    str_sql = f"SELECT username FROM Credenciales WHERE correo = '{correo}' AND password = '{password}';"
    print(str_sql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(str_sql)
    
    datos = cursor_Obj.fetchall()
    
    if not datos:  # An empty result evaluates to False.
        print("Login failed")
        con.close()
        return False
    else:
        print("Welcome")
        con.close()
        return datos

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