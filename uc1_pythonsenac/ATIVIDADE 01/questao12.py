custo_fabrica = float(input(" Informe o valor de custo de fábrica do veículo? "))
porcentagem_distribuidor = custo_fabrica * 0.28
impostos = custo_fabrica * 0.45
custo_final = custo_fabrica + porcentagem_distribuidor + impostos
print(f"Valor final do veículo: {custo_final:.2f}")