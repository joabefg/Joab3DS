Ensinar sobre Banco de dados
- Banco de dados
- SGBD
- Armazenamento e Backup
- Relacionais e NoSQL
- CRUD
Ensinar criar database parque_diversoes.
Atividade: Criar database parque_aquatico.

Ensinar sobre tabela e registros
Ensinar criar tabela atracoes (id, nome, status)
Atividade: Criar tabela bilheteria(id, visitante, valor)

Ensinar sobre driver
Instalar driver
Ensinar criar conexão (incluindo try/catch/except)
Atividade: Criar outro usuário do banco e alterar a conexão para o novo usuário/banco.

Ensinar sobre cursor e commit/rollback e porque tem que fechar conexão  
Ensinar cadastrar em atracoes
Desafio: cadastrar usando input e não hard coded
Atividade: cadastrar em bilheteria

Ensinar FetchAll
Ensinar buscar/listar atrações com status manutenção
Atividade: Mostrar total arrecadado

Desafio: criar menu de acesso.






















ATRACOES (
    id INT PK NN AI
    nome VARCHAR(100) NN
    status VARCHAR(45) 'Funcionando'
)
bilheteria (
    id INT PK NN AI
    visitante VARCHAR(100) NN
    valor DECIMAL(10, 2) NN
)
















resultados = [
    [ [roda gigante] [Funcionando] ]
    [ [montanha russa] [Manutenção] ]
]

# Loop Principal do Sistema (O Menu do Jogo)
while True:
    print("\n=======================================")
    print("      SISTEMA PARQUE DE DIVERSÕES      ")
    print("=======================================")
    print("1 - Cadastrar Nova Atração")
    print("2 - Buscar Atrações por Status 🔍")  # <--- Opção Atualizada
    print("3 - Emitir Ingresso (Bilheteria)")
    print("4 - Relatório Financeiro (Bilheteria)")
    print("5 - Sair do Sistema")
    
    opcao = input("\nEscolha uma opção (1-5): ")

    if opcao == '1':
        cadastrar_atracao()
    elif opcao == '2':
        listar_atracoes_by_status() # <--- Chamada da nova função
    elif opcao == '3':
        emitir_ingresso()
    elif opcao == '4':
        relatorio_bilheteria()
    elif opcao == '5':
        print("\nDesligando o sistema do parque... Até logo!")
        break
    else:
        print("❌ Opção inválida! Tente novamente.")

def listar_atracoes_by_status():
    """Busca e lista as atrações com base no status digitado pelo usuário (Bloco 3 - Desafio 3.3)"""
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        
        print("\n--- 🔍 BUSCADOR DE ATRAÇÕES POR STATUS ---")
        # Captura o que o usuário quer buscar (Ex: Funcionando, Manutenção, Interditado)
        status_busca = input("Digite o status que deseja buscar: ")

        # IMPORTANTE: Usamos o '%s' por segurança (evita SQL Injection)
        comando_sql = "SELECT nome, status FROM atracoes WHERE status = %s"
        dados = (status_busca,) # A vírgula é necessária porque o conector espera uma tupla

        try:
            cursor.execute(comando_sql, dados)
            resultados = cursor.fetchall()

            print(f"\n📋 RESULTADOS PARA STATUS: '{status_busca}'")
            print("-" * 40)
            
            if not resultados:
                print(f"❌ Nenhuma atração encontrada com o status '{status_busca}'.")
            else:
                for atracao in resultados:
                    print(f"🎢 Atração: {atracao[0]} | Status: {atracao[1]}")
                    
        except Error as e:
            print(f"❌ Erro ao realizar a busca: {e}")
        finally:
            cursor.close()
            conexao.close()


# Loop Principal do Sistema (O Menu do Jogo) com Match-Case
while True:
    print("\n=======================================")
    print("      SISTEMA PARQUE DE DIVERSÕES      ")
    print("=======================================")
    print("1 - Cadastrar Nova Atração")
    print("2 - Buscar Atrações por Status 🔍")
    print("3 - Emitir Ingresso (Bilheteria)")
    print("4 - Relatório Financeiro (Bilheteria)")
    print("5 - Sair do Sistema")
    
    opcao = input("\nEscolha uma opção (1-5): ")

    # A nova estrutura substitui o bloco de 'if/elif/else'
    match opcao:
        case '1':
            cadastrar_atracao()
        case '2':
            listar_atracoes_by_status()
        case '3':
            emitir_ingresso()
        case '4':
            relatorio_bilheteria()
        case '5':
            print("\nDesligando o sistema do parque... Até logo!")
            break
        case _: # O underline funciona como o 'else' (o padrão, se nenhuma opção bater)
            print("❌ Opção inválida! Tente novamente.")

def apagar_atracao_by_name():
    """Remove uma atração do banco de dados com base no nome digitado (Bloco 4 / Extra)"""
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        
        print("\n--- 🗑️ ZONA DE EXCLUSÃO DE ATRAÇÕES ---")
        nome_busca = input("Digite o nome EXATO da atração que deseja APAGAR: ")

        # Alerta visual para a turma focar no perigo do WHERE
        # IMPORTANTE: Usamos %s para segurança
        comando_sql = "DELETE FROM atracoes WHERE nome = %s"
        dados = (nome_busca,)

        try:
            # Executa o comando
            cursor.execute(comando_sql, dados)
            
            # O cursor.rowcount nos diz quantas linhas foram afetadas pelo comando
            linhas_afetadas = cursor.rowcount
            
            if linhas_afetadas == 0:
                print(f"⚠️ Nenhuma atração com o nome '{nome_busca}' foi encontrada. Nada foi apagado.")
            else:
                # Pergunta de segurança (Simulação de sistema real)
                confirmacao = input(f"❗ Tem certeza que deseja apagar '{nome_busca}' permanentemente? (S/N): ").upper()
                
                if confirmacao == 'S':
                    conexao.commit() # Salva a exclusão no banco
                    print(f"🗑️ Sucesso: A atração '{nome_busca}' foi removida do sistema!")
                else:
                    conexao.rollback() # Cancela a operação e finge que nada aconteceu
                    print("❌ Operação cancelada pelo usuário. Os dados estão salvos.")
                    
        except Error as e:
            print(f"❌ Erro ao tentar apagar: {e}")
        finally:
            cursor.close()
            conexao.close()

