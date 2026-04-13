soma = 0 

for numeros in range(85, 907):
    if numeros % 2 == 0:
        print(numeros)
        soma += numeros 

print("A soma dos numéros pares é: ", soma)