# condicionais 
# ou estruturas de controle
idade = 18
if idade >= 18:
    print("Maior de idade!")
else:
    print("Menor de idade!")
# operadores lógicos: E OU
if idade > 18 or idade == 18:
    print("verdadeiro")

nota = 60
pc_presenca = 75
if nota >= 60 and pc_presenca >= 75:
    print("Aprovado")
elif nota >= 50 and pc_presenca >= 75:
    print("Recuperação")
else:
    print("Reprovado")

compra_rs = 250.00
assinante_premium = False
reside_interior = False
# SE COMPRA ACIMA DE 200 REAIS OU ASSINANTE PREMIUM
# O FRETE É GRÁTIS, EXCETO SE RESIDIR NO INTERIOR.
if (not reside_interior 
    and (assinante_premium or compra_rs > 200)):
    print("frete grátis")