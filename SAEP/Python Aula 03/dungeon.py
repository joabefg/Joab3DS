import random
# Tabuleiro
mapa = {
    1: "monstro",
    2: "saida",
    3: "tesouro",
    4: "espada",
    5: "cura",
    6: "armadura"
}
inventario = []
portas = [0, 0, 0]
while True:
    # Definir portas e opções
    # 0: Inventário, 1: Direita, 2: Esquerda
    portas[1] = random.randint(1,6)
    portas[2] = random.randint(1,6)
    escolha = int(input("Escolha 1, 2 ou 0:"))
    print(portas)
    # Ver o inventário: Opção 0
    if (escolha == 0):
        print(inventario)
        continue
    # Entrou na sala do Monstro
    if (portas[escolha] == 1): 
        print("Você encontrou um monstro Lv. 20")
        if ("espada" in inventario or
            "cura" in inventario or
            "armadura" in inventario):
            print("Você Sobreviveu.")
            inventario.append("tesouro")
        else:
            print("GAME OVER: Sem itens para se defender")
            break
    elif (portas[escolha] == 2): 
        print("VOCÊ VENCEU! TESOUROS: ")
        print(inventario.count("tesouro"))
        break
    else: # achou item
        sala = portas[escolha]
        item = mapa[sala]
        print("Você encontrou:",item)
        inventario.append(item)
        continue
