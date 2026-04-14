N = int(input("Digite um número inteiro: "))
A = 0

for i in range(1, N+1):
    numerador = N - (i - 1)
    A += numerador / i

print("Valor de A:", A)
                     
