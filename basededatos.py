import sqlite3 as sql
from sqlite3 import Error

def sql_connection():
    try:
        con = sql.connect('DataBase.db')
        return con
    except Error:
        print(Error)

def sql_login(correo, password):
    str_sql = f"SELECT * from Credenciales WHERE correo = '{correo}' AND password = '{password}';"
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(str_sql)
    
    if not cursor_Obj.fetchone():  # An empty result evaluates to False.
        print("Login failed")
        # con.close()
        return False
    else:
        print("Welcome")
        # con.close()
        return True

def sql_signup():
    return print('signup')