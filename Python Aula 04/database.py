# pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error

def conectar_banco():
    """Estabelece Conexão"""
    try: # tenta conectar
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="parque_diversoes"
        )
        if conexao.is_connected():
            print("conectou")
            return conexao
    except Error as erro:
        print(f"Erro ao conectar: {erro}")
        return None
    
def cadastrar_atracao():
    """Inserir novas atrações  no parque"""
    conexao_aberta = conectar_banco()
    if conexao_aberta:
        cursor = conexao_aberta.cursor()
        nome = input("Nome da Atração:")
        status = input("Status (Funcionando/Manutenção)")
        sql = "INSERT INTO atracoes (nome, status) VALUES (%s, %s)"
        dados = (nome, status)
        try:
            cursor.execute(sql, dados)
            conexao_aberta.commit()
            print(f"{nome} cadastrado com sucesso!")
        except Error as erro:
            print(f"Erro ao cadastrar: {erro}")
        finally:
            cursor.close()
            conexao_aberta.close()

def cadastrar_bilheteria():
    # ATIVIDADE: CRIAR LÓGICA DE CADASTRAR BILHETERIA
    # COM BASE NO CADASTRAR ATRAÇÃO
    pass

def listar_atracoes():
    """Listar as atrações"""
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        sql = "SELECT nome, status FROM atracoes"
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            if not resultados:
                print("Nenhum resultado encontrado")
            else:
                for atracao in resultados:
                    print(f"{atracao[0]} - {atracao[1]}")
        except Error as erro:
            print(f"Erro ao consultar: {erro}")
cadastrar_atracao()
listar_atracoes()
