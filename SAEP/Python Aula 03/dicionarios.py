lista = []
dicionario = {}

girias_br = {
    "gambiarra": "solução improvisada",
    "treta": "confusão"
}
alimentos = dict(
    goiaba="fruta", abobora="legume", grao="feijao")

capitais = {
    "Brasil": "Brasília",
    "Rússia": "Moscou",
    "Itália": "Roma"
}
print(capitais["Brasil"])
# adicionar
capitais["China"] = "Xangai"
# Alterar
capitais["China"] = "Pequim"
# imprimir tudo
print(capitais)
# remover
del capitais["Itália"]
capitais["India"] = "Nova Delhi"
print(capitais)
# item inexistente
print(capitais.get("Indonesia"))
# listas
paises = capitais.keys()
cidades = capitais.values()
print(paises)
print(cidades)
# iterar - percorrer
for pais in capitais:
    print("Bem vindo a ", pais)
for pais, cidade in capitais.items():
    print(cidade, " é a capital de ", pais)
# dicionários aninhados
npc = {
    "nome": "Ferreiro",
    "fala": "Precisa de arma ou escudo?",
    "itens": {
        "espada": 100,
        "escudo": 80,
        "adaga": 95
    }
}
# Crie um dicionário contendo sua ficha de personagem, 
# com nome, raça, classe, nível, arma, ouro
# O dicionário deve ter um subdicionário com seus atributos:
# vida, magia, defesa, ataque e sorte
# cada atributo terá um valor de 1 a 5 
# mas o total deve ser no máximo 18 pontos
personagem = {
    "Nome": "Zephyr",
    "Raça": "Humano",
    "Classe": "Druida",
    "Nível": 120,
    "Arma": "Machado",
    "Ouro": 5,
    "atributos": {
        "vida": 4,
        "magia": 5,
        "defesa": 4,
        "ataque": 0,
        "sorte": 5
    }
}