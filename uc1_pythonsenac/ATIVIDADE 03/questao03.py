# Inicialização das variáveis
soma_positivos = 0
quantidade_negativos = 0

# Loop para ler 50 valores
for i in range(1, 51):
    valor = int(input(f"Digite o {i}º valor inteiro: "))
    
    if valor > 0:
        soma_positivos += valor
    elif valor < 0:
        quantidade_negativos += 1

# Mostrar os resultados
print(f"\nSoma dos valores positivos: {soma_positivos}")
print(f"Quantidade de valores negativos: {quantidade_negativos}")