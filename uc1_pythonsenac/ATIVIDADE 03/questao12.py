# contadores de clubes
figueirense = 0
marcilio = 0
outros = 0

# soma de salários do Figueirense
soma_salario_fig = 0

# contador de pessoas do Figueirense (para média)
cont_fig_salario = 0

# condição específica
nasceu_floripa_marcilio = 0
outras_cidades_figueirense = 0

while True:
    clube = int(input("Clube (1-Figueirense, 2-Marcílio, 3-Outros, 0-sair): "))
    
    if clube == 0:
        break

    salario = float(input("Informe seu salário: "))
    nascimento = int(input("Informe seu local de nascimento (1-Florianópolis, 2-Outras): "))

    if clube == 1:
        figueirense += 1
        soma_salario_fig += salario
        cont_fig_salario += 1

        if nascimento == 2:  # outras cidades
            outras_cidades_figueirense += 1

    elif clube == 2:
        marcilio += 1

        if nascimento == 1:  # Florianópolis
            nasceu_floripa_marcilio += 1

    elif clube == 3:
        outros += 1

# cálculo da média
if cont_fig_salario > 0:
    media = soma_salario_fig / cont_fig_salario
else:
    media = 0

# saída
print("Torcedores Figueirense:", figueirense)
print("Torcedores Marcílio:", marcilio)
print("Outros:", outros)

print("Média salarial Figueirense:", media)

print("Floripa + Marcílio:", nasceu_floripa_marcilio)
print("Outras cidades + Figueirense:", outras_cidades_figueirense)

                                                                                                                                                                                                                                                      