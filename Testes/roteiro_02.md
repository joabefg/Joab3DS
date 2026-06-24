# Atividade Prática — Testes Unitários com PyTest

## Objetivo

Aprender a criar testes unitários utilizando:

* `assert`
* `pytest`
* `pytest.raises()`
* Casos de sucesso
* Casos de erro
* Organização de testes

---

# Cenário 1 (Eu)

## Sistema Bancário

Você possui uma função que realiza saques em uma conta.

### Código

```python
def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError("Valor inválido")

    if valor > saldo:
        raise ValueError("Saldo insuficiente")

    return saldo - valor
```

---

## Passo 1 - Identificar os cenários

Pergunta:

> O que pode acontecer quando alguém tenta sacar dinheiro?

Respostas esperadas:

1. Saque válido
2. Saque maior que o saldo
3. Saque com valor negativo
4. Saque com valor zero

---

## Passo 2 - Criar os testes

### Teste 1 - Saque válido

```python
def test_saque_valido():
    assert sacar(100, 20) == 80
```

### Teste 2 - Saldo insuficiente

```python
import pytest

def test_saque_maior_que_saldo():
    with pytest.raises(ValueError):
        sacar(100, 150)
```

### Teste 3 - Valor negativo

```python
def test_saque_negativo():
    with pytest.raises(ValueError):
        sacar(100, -10)
```

### Teste 4 - Valor zero

```python
def test_saque_zero():
    with pytest.raises(ValueError):
        sacar(100, 0)
```

---

## Discussão

Responda:

* Cada teste verifica apenas uma regra?
* Os testes são independentes?
* É fácil identificar qual regra falhou?

---

# Cenário 2 (Alunos)

## Sistema de Loja

Uma loja oferece desconto para compras acima de R$100.

### Código

```python
def calcular_desconto(valor):
    if valor < 0:
        raise ValueError("Valor inválido")

    if valor >= 100:
        return valor * 0.9

    return valor
```

---

## Desafio

Crie os testes para verificar:

### Caso 1

Compra de R$200.

Resultado esperado:

```python
180
```

### Caso 2

Compra de R$100.

Resultado esperado:

```python
90
```

### Caso 3

Compra de R$50.

Resultado esperado:

```python
50
```

### Caso 4

Compra negativa.

Deve gerar:

```python
ValueError
```

---

## Regras

* Criar um teste para cada situação.
* Utilizar `assert`.
* Utilizar `pytest.raises()` quando necessário.
* Nomear os testes corretamente.

---

# Desafio Extra (Para quem terminar primeiro)

Crie uma função:

```python
def frete_gratis(valor):
    pass
```

### Regras

* Acima de R$150 → retorna `True`
* Até R$150 → retorna `False`
* Valor negativo → gera `ValueError`

---

## Sua tarefa

1. Criar todos os testes primeiro.
2. Depois implementar a função.
3. Fazer todos os testes passarem.

> Aplicando o conceito de **TDD (Test Driven Development)**.

---

# Gabarito (Professor)

> Não consultar antes de terminar a atividade.

```python
import pytest

def test_desconto_200():
    assert calcular_desconto(200) == 180

def test_desconto_100():
    assert calcular_desconto(100) == 90

def test_sem_desconto():
    assert calcular_desconto(50) == 50

def test_valor_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(-10)
```

---

# Critérios de Avaliação

| Critério                         | Pontos |
| -------------------------------- | ------ |
| Uso correto de `assert`          | 2      |
| Uso correto de `pytest.raises()` | 2      |
| Um teste por regra de negócio    | 2      |
| Nomes adequados para os testes   | 2      |
| Código organizado e legível      | 2      |

**Total: 10 pontos**
