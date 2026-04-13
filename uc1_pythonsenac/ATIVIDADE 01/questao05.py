i = float(input("Informe a taxa de aplicação: "))
P = float(input("Informe a aplicação mensal: "))
n = float(input("Informe o número de meses: "))
valor_acumulado = P * ((1 + i)**n - 1) / i
print(f"Valor acumulado no perído: {valor_acumulado:.2f}")