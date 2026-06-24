# pip install pytest
import pytest
from sistema_bancario import sacar

def test_saque_valido():
    assert sacar(100, 20) == 80

def test_saque_maior_que_saldo():
    with pytest.raises(ValueError):
        sacar(100, 150)

# ATIVIDADE: Escreva os dois testes abaixo
# Saque de valor negativo
def test_saque_valor_negativo():
    with pytest.raises(ValueError):
        sacar(200,-10)
# Saque de valor zero
def test_saque_valor_zero():
    with pytest.raises(ValueError):
        sacar(200,0)