nome = input("Informe seu nome: ")
ndiarias = int(input("Informe o números de diáras no hotel: "))
diaria = ndiarias * 150

if ndiarias > 15:
    taxa = 5
elif ndiarias == 15:
    taxa = 6.30
else:
    taxa = 8

taxa_final = (taxa * ndiarias) + diaria

print("Sr(a)" , nome, "o valor de sua conta é: ", taxa_final)
print("O ganho total do hotel é: ", taxa_final)