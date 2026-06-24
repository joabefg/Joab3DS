# Alunos: Classe Locadora/Cinema
# Professor: Classe Bibioteca
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo):
        if not titulo:
            raise ValueError("Título inválido")
        self.livros.append(titulo)

    def emprestar_livro(self, titulo):
        if titulo not in self.livros:
            raise ValueError("Livro não encontrado")
        self.livros.remove(titulo)

    def quantidade_livros(self):
        return len(self.livros)