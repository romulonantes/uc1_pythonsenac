ano_de_nascimento = float(input("Informe seu ano de nascimento: "))
ano_atual = float(input("Informe o ano atual: "))
idade = ano_atual - ano_de_nascimento
idade_em_2028 = idade + 3 
print(f"Idade atual: {idade:.2f}")
print(f"Idade em 2028: {idade_em_2028:.2f}")

