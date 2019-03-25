import MySQLdb
import sqlite3
import mysql.connector
from flask import request

class DBhelper():
     def __init__(self):
        pass
        dato = {              
        'host':'127.0.0.1',    # tu host, usualmente localhost
        'user':'root',         # tu usuario
        'password':'',           # tu password
        'database':'proyecto'}       # el nombre de la base de datos

        conexion = mysql.connector.connect(** dato)
        cursor = conexion.cursor()
        def insertar(usuario, contrasenia):
            conexion = mysql.connector.connect(** dato)
            cursor = conexion.cursor()
            valores ="INSERT INTO login(usuario, contrasenia)VALUES(usuario = "request.form[usu]", contraseni = "request.form[contra]")"
            try:
                cursor.execute(valores)
                conexion.commit()
            except:
                print("nell")
            conexion.close()