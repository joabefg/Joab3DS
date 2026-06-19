import random
itens = [
    "espada", "poção",
    "escudo", "cajado",
    "mapa", "armadura", 
    "tesouro","nada", 
    "é um mímico", "poção duvidosa"
]
random.shuffle(itens)
num = int(input("Escolha um número 1 - 10:"))
num -= 1
print(itens[num])   