# Exercício de Testes em Python com Assert, Pytest, Fixture, Parametrize e Cobertura

## Objetivo

Neste exercício teremos dois cenários muito parecidos:

* **Projeto A (Biblioteca)** → Demonstrado pelo professor.
* **Projeto B (Locadora de Filmes)** → Desenvolvido pelos alunos.

Cada cenário possui:

* Teste com `assert`
* Teste com `try/except`
* Teste com `pytest`
* Teste com `fixture`
* Teste com `parametrize`
* Casos de sucesso e erro

---

# Estrutura de Pastas

```text
projeto_testes/
│
├── biblioteca.py
├── locadora.py
│
├── test_biblioteca.py
└── test_locadora.py
```

---

# biblioteca.py (Projeto A)

```python
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo):
        if not titulo:
            raise ValueError("Título inválido")

        self.livros.append(titulo)

    def remover_livro(self, titulo):
        if titulo not in self.livros:
            raise ValueError("Livro não encontrado")

        self.livros.remove(titulo)

    def quantidade_livros(self):
        return len(self.livros)
```

---

# locadora.py (Projeto B)

```python
class Locadora:
    def __init__(self):
        self.filmes = []

    def adicionar_filme(self, titulo):
        if not titulo:
            raise ValueError("Título inválido")

        self.filmes.append(titulo)

    def remover_filme(self, titulo):
        if titulo not in self.filmes:
            raise ValueError("Filme não encontrado")

        self.filmes.remove(titulo)

    def quantidade_filmes(self):
        return len(self.filmes)
```

---

# test_biblioteca.py

## 1. Testes apenas com Assert

```python
from biblioteca import Biblioteca


def test_adicionar_livro_assert():
    bib = Biblioteca()

    bib.adicionar_livro("Python")

    assert bib.quantidade_livros() == 1


def test_remover_livro_assert():
    bib = Biblioteca()

    bib.adicionar_livro("Python")
    bib.remover_livro("Python")

    assert bib.quantidade_livros() == 0
```

---

## 2. Testes usando Try/Except

```python
from biblioteca import Biblioteca


def test_adicionar_livro_vazio_try_except():
    bib = Biblioteca()

    try:
        bib.adicionar_livro("")
        assert False
    except ValueError:
        assert True


def test_remover_livro_inexistente_try_except():
    bib = Biblioteca()

    try:
        bib.remover_livro("Java")
        assert False
    except ValueError:
        assert True
```

---

## 3. Testes usando Pytest

```python
import pytest
from biblioteca import Biblioteca


def test_adicionar_livro_pytest():
    bib = Biblioteca()

    bib.adicionar_livro("Python")

    assert bib.quantidade_livros() == 1


def test_remover_livro_inexistente_pytest():
    bib = Biblioteca()

    with pytest.raises(ValueError):
        bib.remover_livro("Java")
```

---

## 4. Testes usando Fixture

```python
import pytest
from biblioteca import Biblioteca


@pytest.fixture
def biblioteca():
    bib = Biblioteca()
    bib.adicionar_livro("Python")
    return bib


def test_fixture_sucesso(biblioteca):
    assert biblioteca.quantidade_livros() == 1


def test_fixture_remover(biblioteca):
    biblioteca.remover_livro("Python")

    assert biblioteca.quantidade_livros() == 0
```

---

## 5. Testes Parametrizados

```python
import pytest
from biblioteca import Biblioteca


@pytest.mark.parametrize(
    "titulo",
    [
        "Python",
        "Java",
        "C#",
        "JavaScript"
    ]
)
def test_parametrizado_sucesso(titulo):
    bib = Biblioteca()

    bib.adicionar_livro(titulo)

    assert bib.quantidade_livros() == 1


@pytest.mark.parametrize(
    "titulo",
    [
        "",
        None
    ]
)
def test_parametrizado_erro(titulo):
    bib = Biblioteca()

    with pytest.raises(ValueError):
        bib.adicionar_livro(titulo)
```

---

# test_locadora.py

Os alunos deverão reproduzir a mesma lógica.

```python
import pytest
from locadora import Locadora


# ASSERT

def test_adicionar_filme_assert():
    loc = Locadora()

    loc.adicionar_filme("Matrix")

    assert loc.quantidade_filmes() == 1


def test_remover_filme_assert():
    loc = Locadora()

    loc.adicionar_filme("Matrix")
    loc.remover_filme("Matrix")

    assert loc.quantidade_filmes() == 0


# TRY/EXCEPT

def test_filme_vazio_try_except():
    loc = Locadora()

    try:
        loc.adicionar_filme("")
        assert False
    except ValueError:
        assert True


def test_filme_inexistente_try_except():
    loc = Locadora()

    try:
        loc.remover_filme("Avatar")
        assert False
    except ValueError:
        assert True


# PYTEST

def test_pytest_sucesso():
    loc = Locadora()

    loc.adicionar_filme("Matrix")

    assert loc.quantidade_filmes() == 1


def test_pytest_erro():
    loc = Locadora()

    with pytest.raises(ValueError):
        loc.remover_filme("Avatar")


# FIXTURE

@pytest.fixture
def locadora():
    loc = Locadora()
    loc.adicionar_filme("Matrix")
    return loc


def test_fixture_sucesso(locadora):
    assert locadora.quantidade_filmes() == 1


def test_fixture_remover(locadora):
    locadora.remover_filme("Matrix")

    assert locadora.quantidade_filmes() == 0


# PARAMETRIZAÇÃO

@pytest.mark.parametrize(
    "titulo",
    [
        "Matrix",
        "Avatar",
        "Vingadores",
        "Batman"
    ]
)
def test_param_sucesso(titulo):
    loc = Locadora()

    loc.adicionar_filme(titulo)

    assert loc.quantidade_filmes() == 1


@pytest.mark.parametrize(
    "titulo",
    [
        "",
        None
    ]
)
def test_param_erro(titulo):
    loc = Locadora()

    with pytest.raises(ValueError):
        loc.adicionar_filme(titulo)
```

---

# Instalação das Dependências

```bash
pip install pytest
pip install pytest-cov
```

---

# Executar os Testes

```bash
pytest
```

---

# Executar com Cobertura de Testes

```bash
pytest --cov=.
```

Saída esperada:

```text
Name                 Stmts   Miss Cover
----------------------------------------
biblioteca.py           12      0   100%
locadora.py             12      0   100%
----------------------------------------
TOTAL                   24      0   100%
```

---

# Gerar Relatório HTML

```bash
pytest --cov=. --cov-report=html
```

Será criada a pasta:

```text
htmlcov/
```

Abra o arquivo:

```text
htmlcov/index.html
```

---

# Exemplo Simplificado do Relatório HTML

```html
Coverage report

biblioteca.py
✔ Linha 5 executada
✔ Linha 8 executada
✔ Linha 12 executada

Cobertura: 100%

locadora.py
✔ Linha 5 executada
✔ Linha 8 executada
✔ Linha 12 executada

Cobertura: 100%

TOTAL: 100%
```

---

# Estratégia da Aula

| Professor (Projeto A) | Alunos (Projeto B)  |
| --------------------- | ------------------- |
| Biblioteca            | Locadora            |
| Livro                 | Filme               |
| adicionar_livro()     | adicionar_filme()   |
| remover_livro()       | remover_filme()     |
| quantidade_livros()   | quantidade_filmes() |
| Testes com assert     | Replicar            |
| Testes com try/except | Replicar            |
| Testes com pytest     | Replicar            |
| Fixture               | Replicar            |
| Parametrize           | Replicar            |
| pytest-cov            | Replicar            |

## Resultado Esperado

Ao final da atividade, os alunos deverão ser capazes de:

1. Criar testes utilizando apenas `assert`.
2. Validar exceções usando `try/except`.
3. Utilizar `pytest.raises()`.
4. Criar e utilizar `fixtures`.
5. Criar testes parametrizados com `@pytest.mark.parametrize`.
6. Gerar relatórios de cobertura utilizando `pytest-cov`.
7. Interpretar relatórios de cobertura de testes em HTML.
