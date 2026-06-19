import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

# --- MESMA FUNÇÃO DE CONEXÃO QUE ELES JÁ CONHECEM ---
def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",        
            password="root",    
            database="parque_diversoes"
        )
        return conexao
    except Error as e:
        messagebox.showerror("Erro de Conexão", f"Não foi possível conectar ao banco:\n{e}")
        return None

# --- FUNÇÃO QUE O BOTÃO VAI CHAMAR ---
def acao_botao_cadastrar():
    # 1. Pegar o texto que o usuário digitou nos campos da janela (.get())
    nome = campo_nome.get()
    status = campo_status.get()

    # Validação simples: não deixar cadastrar em branco
    if nome == "" or status == "":
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return

    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        comando_sql = "INSERT INTO atracoes (nome, status) VALUES (%s, %s)"
        dados = (nome, status)

        try:
            cursor.execute(comando_sql, dados)
            conexao.commit()
            
            # FEEDBACK VISUAL: Uma caixinha de sucesso na tela!
            messagebox.showinfo("Sucesso!", f"A atração '{nome}' foi cadastrada!")
            
            # Limpa os campos depois de cadastrar
            campo_nome.delete(0, tk.END)
            campo_status.delete(0, tk.END)
            
        except Error as e:
            messagebox.showerror("Erro no SQL", f"Erro ao salvar no banco: {e}")
        finally:
            cursor.close()
            conexao.close()


# --- 🏛️ CONSTRUINDO A INTERFACE GRÁFICA (GUI) ---

# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Controle do Parque - SENAI")
janela.geometry("400x250") # Largura x Altura
janela.configure(bg="#2c3e50") # Cor de fundo bem "gamer/dark mode"

# 2. Título do Sistema na Janela
titulo = tk.Label(janela, text="CADASTRO DE ATRAÇÕES", font=("Arial", 14, "bold"), bg="#2c3e50", fg="white")
titulo.pack(pady=15) # O pack() joga o elemento na tela. pady é o espaçamento interno.

# 3. Campo: Nome da Atração
texto_nome = tk.Label(janela, text="Nome da Atração:", bg="#2c3e50", fg="white", font=("Arial", 10))
texto_nome.pack()
campo_nome = tk.Entry(janela, width=30, font=("Arial", 10)) # O input visual
campo_nome.pack(pady=5)

# 4. Campo: Status
texto_status = tk.Label(janela, text="Status (Funcionando/Manutenção):", bg="#2c3e50", fg="white", font=("Arial", 10))
texto_status.pack()
campo_status = tk.Entry(janela, width=30, font=("Arial", 10))
campo_status.pack(pady=5)

# 5. O Botão Mágico
# O segredo está no 'command=acao_botao_cadastrar', que liga o clique do mouse à nossa função
botao = tk.Button(janela, text="🎰 CADASTRAR NO BANCO", font=("Arial", 10, "bold"), bg="#2ecc71", fg="white", command=acao_botao_cadastrar)
botao.pack(pady=20)

# 6. Manter a janela aberta (O loop da interface)
janela.mainloop()