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

def listar_atracoes_by_status():
    """
    Busca e lista atrações pelo Status
    """
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        # Funcionando, Manutenção, Interditado, Auditoria
        status_busca = input("Digite o status:")
        # Consulta sql
        sql = "SELECT nome, status FROM atracoes WHERE status = %s"
        dados = (status_busca,)
        try:
            cursor.execute(sql,dados)
            resultados = cursor.fetchall()
            if not resultados:
                print(f"Nenhuma atração com este status")
            else:
                for atracao in resultados:
                    print(f"Atração: {atracao[0]}")
        except Error as erro:
            print(f"Erro ao buscar: {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_bilheteria():
    pass # ATIVIDADE

def apagar_atracao():
    """Apagar uma atração pelo nome"""
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        nome_atracao = input("Digite o nome da Atração:")
        sql = "DELETE FROM atracoes WHERE nome = %s"
        dados = (nome_atracao,) # colocando na tupla
        try:
            cursor.execute(sql, dados)
            # rowcount retorna quantas linhas foram apagadas
            registros_apagados = cursor.rowcount
            if registros_apagados == 0:
                print(f"não há registro com nome {nome_atracao}")
            else:
                confirmacao = input("Tem certeza? s/n")
                if confirmacao == 's':
                    conexao.commit() # executa de fato a ação
                    print(f"{nome_atracao} excluída.")
                else:
                    conexao.rollback() # desfazer a ação
                    print("Ação cancelada")
        except Error as erro:
            print(f"Erro ao apagar: {erro}")
        finally:
            cursor.close()
            conexao.close()
            

while True:
    opcao = input("Escolha uma Opção:")
    match opcao:
        case '1': # cadastrar atração
            cadastrar_atracao()
        case '2': # cadastrar bilhete
            cadastrar_bilheteria() # ATIVIDADE
        case '3': # listar todos
            listar_atracoes()
        case '4': # listar por status
            listar_atracoes_by_status()
        case '5': # listar bilheteria
            listar_bilheteria() # ATIVIDADE
        case '6': # apagar atração
            apagar_atracao()
        case '7': # apagar bilheteria por pessoa
            apagar_bilheteria() # ATIVIDADE DE AGORA
        case '8': 
            lucro_total() # PONTO EXTRA - CALCULAR GANHO
        case '0': # sair
            break
