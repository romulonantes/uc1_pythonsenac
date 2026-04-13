salario_bruto = float (input("Informe o valor do salário: "))

if 0 <= salario_bruto <= 500:
    desconto = 0
    
elif 500.01 <= salario_bruto <= 1500:
    desconto = salario_bruto * 0.10
    
elif 1500.01 <= salario_bruto <= 2500:
    desconto = salario_bruto * 0.15

if 2500.01 <= salario_bruto:
    desconto = salario_bruto * 0.20

print("O valor do desconto é: ", desconto)