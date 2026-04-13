# Inicializando contadores
menos_de_10 = 0
entre_10_e_15 = 0
mais_de_15 = 0
total_alunos = 0

while True:
    # Pergunta quantas vezes o aluno foi ao restaurante
    vezes = input("Quantas vezes o aluno foi ao restaurante? (digite 'fim' para terminar) ")
    
    if vezes.lower() == "fim":  # se digitar "fim", o programa para
        break
    
    vezes = int(vezes)
    
    # Contando em cada categoria
    if vezes < 10:
        menos_de_10 += 1
    elif 10 <= vezes <= 15:
        entre_10_e_15 += 1
    else:
        mais_de_15 += 1
    
    total_alunos += 1  # conta o aluno registrado

# Calculando percentuais
if total_alunos > 0:
    percent_menos_10 = (menos_de_10 / total_alunos) * 100
    percent_10_15 = (entre_10_e_15 / total_alunos) * 100
    percent_mais_15 = (mais_de_15 / total_alunos) * 100

    # Mostrando resultados
    print(f"Percentual de alunos que foram menos de 10 vezes: {percent_menos_10:.2f}%")
    print(f"Percentual de alunos que foram entre 10 e 15 vezes: {percent_10_15:.2f}%")
    print(f"Percentual de alunos que foram mais de 15 vezes: {percent_mais_15:.2f}%")
else:
    print("Nenhum aluno foi registrado.")