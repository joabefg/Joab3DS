# pip install mysql.connector.python
import mysql.connector
from mysql.connector import Error

def conectar_banco():
    try:
        # tenta conectar
        print("conectou")
    except Error as erro:
        print(f"Erro ao conectar: {erro}")