# Enquanto: While
count = 1
while count <= 5:
    print(count)
    count += 1 

# break: para a repetição
while True:
    aluno = input("Digite o nome do Aluno, [s para sair]:")
    if aluno == "s":
        break
    print(aluno.capitalize())

# continue: pular para a próxima iteração
while True:
    texto = input("Digite um número [s para sair]:")
    if texto == "s":
        break
    numero = int(texto)
    if numero % 2 == 0: # numero / 2 = 2 resto 1
        continue
    print(numero, " é ímpar seu quadrado é ", numero * numero)

# iteração - for
palavra = 'paralelepípedo' # 14
for letra in palavra:
    if letra == "d":
        break
    if letra == "p":
        continue
    print(letra)

# repetir x vezes - for range
for x in range(0,10):
    print(x)

# ATIVIDADE
# SIMULE O LANÇAMENTO DE 3 DADOS
# SE SOMA < 6 IMPRIME FALHA
# SE SOMA ENTRE 6 E 12 IMPRIME SUCESSO
# SE SOMA > 12 IMPRIME CRÍTICO

