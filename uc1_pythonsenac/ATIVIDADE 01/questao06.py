dolar_no_cofre = float(input("Informe o valor em dolares guardados no cofre: "))
cotacao_dolar_do_dia = float(input("Informe a cotação do dolar do dia: "))
valor_dolares_em_real = dolar_no_cofre * cotacao_dolar_do_dia
print(f"Valor em reais do dolar guardado: {valor_dolares_em_real:.2f}")
