def test_validar_idade():
    try:
        assert validar_idade(18) == "Maior de idade", "Err: 18 anos"
        assert validar_idade(19) == "Maior de idade", "Err: 19 anos"
        assert validar_idade(17) == "Menor de idade", "Err: 17 anos"
        assert isinstance(inserir_idade(), int), "Err: idade não é int"
        print("Todos os testes passaram",)
    except AssertionError as erro:
        print(erro)

def inserir_idade():
    idade = input("Idade:")
    return idade

def validar_idade(idade):
    # idade = int(input("Idade: "))
    if idade < 18:
        return "Menor de idade"
    else:
        return "Maior de idade"
    
test_validar_idade()