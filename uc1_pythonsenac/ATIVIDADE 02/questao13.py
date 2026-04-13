valor = int(input("Informe um valor inteiro: "))

if valor <= 100:
    faixa = "A"
elif 100 <= valor <= 150:
    faixa = "B"
elif 151 <= valor <= 300:
    faixa = "C"
else:
    faixa = "X"
print("A faixa que o valor se encontra é: ", faixa)