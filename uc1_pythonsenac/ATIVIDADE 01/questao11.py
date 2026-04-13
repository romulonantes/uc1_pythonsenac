valor_de_custo = float(input("Informe o valor de custo do produto : "))
valor_com_margem = valor_de_custo * 1.4
salario_liquido = valor_de_custo + valor_com_margem
print(f"Valor da venda: {valor_com_margem:.2f}")