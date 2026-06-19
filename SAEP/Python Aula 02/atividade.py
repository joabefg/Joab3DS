import random
# ATIVIDADE
# SIMULE O LANÇAMENTO DE 3 DADOS
# SE SOMA < 6 IMPRIME FALHA
# SE SOMA ENTRE 6 E 12 IMPRIME SUCESSO
# SE SOMA > 12 IMPRIME CRÍTICO

soma = 0 # 3, 1, 3
for dado in range(0,3):
    soma += random.randint(1,6) # roda o dado de 1 a 6
    print(soma)
if soma < 6:
    print("falha")
# elif soma >= 6 and soma <= 12:
elif 6 <= soma <= 12:
    print("sucesso")
else:
    print("critico")