total = 0

for i in range(10):
    
    nome = input("Informe seu nome: ")
    compra = float(input("Informe o valor da compra: "))
   
    if compra >= 250:
        desconto = compra * 0.20
    else: 
        desconto = compra * 0.15
       
    valor_final = compra - desconto
    total += valor_final
    
    print(nome)
    print("Valor da compra:", compra)
    print("Desconto:", desconto)
    print("Valor a pagar:", valor_final)

print("Total arrecadado:", total)
       
   