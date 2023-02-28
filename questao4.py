
faturamento_SP = 67836.43
faturamento_RJ = 36678.66
faturamento_MG = 29229.88
faturamento_ES = 27165.48
faturamento_Outros = 19849.53

# calculo do faturamento mensal
faturamento_Mensal = faturamento_SP + faturamento_RJ + faturamento_MG + faturamento_ES + faturamento_Outros

# calculo dos percentuais de cada estado
percentual_SP = (faturamento_SP / faturamento_Mensal) * 100
percentual_RJ = (faturamento_RJ / faturamento_Mensal) * 100
percentual_MG = (faturamento_MG / faturamento_Mensal) * 100
percentual_ES = (faturamento_ES / faturamento_Mensal) * 100
percentual_Outros = (faturamento_Outros / faturamento_Mensal) * 100


print("Estado".ljust(10), "Faturamento".ljust(15), "Percentual")
print("SP".ljust(10), f"R$ {faturamento_SP}".ljust(15), f"{percentual_SP:.2f}%")
print("RJ".ljust(10), f"R$ {faturamento_RJ}".ljust(15), f"{percentual_RJ:.2f}%")
print("MG".ljust(10), f"R$ {faturamento_MG}".ljust(15), f"{percentual_MG:.2f}%")
print("ES".ljust(10), f"R$ {faturamento_ES}".ljust(15), f"{percentual_ES:.2f}%")
print("Outros".ljust(10), f"R$ {faturamento_Outros}".ljust(15), f"{percentual_Outros:.2f}%")
