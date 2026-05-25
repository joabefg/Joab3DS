 # Lista
dias_semana = ["domingo","segunda","terça","quarta","quinta","sexta","sabado"]
gato = list('gato')
print(gato)
dia_mes_ano = '22/05/2026'.split('/')
print(dia_mes_ano)
frutas_separadas = 'mamao,morango,maça'.split(',')
print(frutas_separadas)

# listas possuem índice
print(dias_semana[-1])
print(dias_semana[1:6]) # dias úteis
# dias_semana.sort()
print(sorted(dias_semana))

# iteração
for dia in dias_semana:
    print(dia.capitalize())