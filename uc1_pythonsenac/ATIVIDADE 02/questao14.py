nome = input("Informe seu nome: ")
ndiaria = int(input("Indorme o número de dias da estádia: "))
diaria = 80

if ndiaria < 15:
    valor_diaria = ndiaria * (diaria + 8)
elif ndiaria == 15:
    valor_diaria = ndiaria * (diaria + 6)
else:
    valor_diaria = ndiaria * (diaria + 5.50)

print("O valor da diária de ", nome, "é", valor_diaria)