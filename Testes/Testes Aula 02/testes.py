
# Retorna True se o número for par
def eh_par(numero):
    return numero % 2 == 0

# 01. Número Par
def test_numero_par():
    assert eh_par(4) == True

# 02. Número ímpar
def test_numero_impar():
    assert eh_par(3) == False

# 03. 0 é par?
def test_zero_par():
    assert eh_par(0) == True
    
# 04. negativo é par?
def test_negativo_par():
    assert eh_par(-8) == True

# Chamadas de teste
test_numero_par()
test_numero_impar()
test_zero_par()
test_negativo_par()