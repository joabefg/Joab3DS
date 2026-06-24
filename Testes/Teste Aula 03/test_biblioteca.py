from biblioteca import Biblioteca

class Livro:
    def __init__(self):
        self.titulo
        self.autor
        self.editora

def test_adicionar_livro():
    bn = Biblioteca()
    alquimita = Livro("O Alquimista","Paulo Coelho","Editra X")
    hobbit = Livro("O Hobbit","J.R.R. Tolkien","Editora Y")
    bn.adicionar_livro("O Alquimista - Paulo Coelho")
    assert bn.quantidade_livros() == 1

def test_emprestar_livro():
    bn = Biblioteca()
    bn.adicionar_livro("O Hobbit - J.R.R. Tolkien")
    bn.emprestar_livro("O Hobbit - J.R.R. Tolkien")
    assert bn.quantidade_livros() == 0

test_adicionar_livro()
test_emprestar_livro()