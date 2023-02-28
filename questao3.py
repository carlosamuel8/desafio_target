

# OBS: não encontrei o arquivo xml ou json em questão, então fiz com uma lista de valores aleatórios, 
# onde os dias de final de semana terão faturamento igual a zero.

from random import randint


faturamento_Mensal = [0 if i % 7 == 0 or i % 7 == 6 else randint(1000, 5000) for i in range(31)]

print(faturamento_Mensal)


# calcular a media ignorando os zeros
if 0 in faturamento_Mensal:
    faturamento_Mensal.remove(0)
media = sum(faturamento_Mensal) / len(faturamento_Mensal)

# calcular o menor valor, ignorando os zeros
menor = min(faturamento_Mensal)

# calcular o maior valor, ignorando os zeros
maior = max(faturamento_Mensal)

# contar os valores maiores que a média, ignorando os zeros
quantidade_de_dias = 0
for valor in faturamento_Mensal:
    if valor > media:
        quantidade_de_dias += 1


print(f"O menor valor de faturamento ocorrido em um dia do mês foi de R$ {menor}")
print(f"O maior valor de faturamento ocorrido em um dia do mês foi de R$ {maior}")
print(f"O número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi de {quantidade_de_dias} dias")



