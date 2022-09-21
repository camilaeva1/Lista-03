#Lista 03 - Questão 04: Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#Maior e Menor Acerto; Total de Alunos que utilizaram o sistema; A Média das Notas da Turma
maiornota = 0  
alunos = 0   
menornota = 0   
alunoatual = 0     
media = 0          

#   media = total_notas / alunos
total_notas = 0
responses = []

header = """
###############################
#          GABARITO           #
###############################"""
print(header)
for position in range(1, 11):
    # Entre com as respostas de cada pergunta
    response = input("digite a resposta da pergunta %s: " % position)
    # Iserimos na lista que guarda o gabarito da prova em lower case!
    responses.append(response.lower())

header = """
###############################
#            ALUNO            #
###############################"""
while True: 
    print(header)
    for position, question in enumerate(responses, 1):
        response = input("digite a resposta da pergunta %s: " % position)
        if response.lower() == question:
            alunoatual += 1  
    alunos += 1
    if alunoatual > maiornota:
       maiornota = alunoatual
    if alunoatual < menornota or menornota == 0:
        menornota = alunoatual
    total_notas += alunoatual
    answer = input("\nFazer a prova novamente: [S/n]: ")
    if answer.lower() == '' or answer.lower() == 's':  
        alunoatual = 0
        continue   

    break 

media = total_notas // alunos  
print("Maior acerto: %s" % maiornota)
print("Menor acerto: %s" % menornota)
print("Total de alunos: %s" % alunos)
print("Média das notas: %s" % media)


gabarito = ''
gabarito2 = ''
count = total_acertos = total = count2 = maior = menor = 0
for e in range(1,11):
    gabarito = input(f"{e} - Digite o gabarito das notas: ").strip().upper()[0]
    gabarito2 += (gabarito)

print("-="*30)
continuar = ' '
while continuar not in 'N':
    total_acertos = 0
    for c in range(1,11):
        resposta = input(f"{c} - Resposta da questao: ").strip().upper()[0]
        if c == 1 and resposta == gabarito2[0]:
            count += 1
            total_acertos += 1
        elif c == 2 and resposta == gabarito2[1]:
            count += 1
            total_acertos += 1
        elif c == 3 and resposta == gabarito2[2]:
            count += 1
            total_acertos += 1
        elif c == 4 and resposta == gabarito2[3]:
            count += 1
            total_acertos += 1
        elif c == 5 and resposta == gabarito2[4]:
            count += 1
            total_acertos += 1
        elif c == 6 and resposta == gabarito2[5]:
            count += 1
            total_acertos += 1
        elif c == 7 and resposta == gabarito2[6]:
            count += 1
            total_acertos += 1
        elif c == 8 and resposta == gabarito2[7]:
            count += 1
            total_acertos += 1
        elif c == 9 and resposta == gabarito2[8]:
            count += 1
            total_acertos += 1
        elif c == 10 and resposta == gabarito2[9]:
            count += 1
            total_acertos += 1
                
        if c == 10:
            print("-="*30)
            continuar = input("[N] Para sair ").strip().upper()[0]
            total+=1

        if total_acertos > maior:
            maior = total_acertos
        if total_acertos < menor or total_acertos == 1:
            menor = total_acertos

print("-="*30)
print("Gabarito das respostas")
for d in gabarito2:
    count2+=1
    print(f"{count2} - {d}")
print("-="*30)

print(f"Total de acertos: {count}")
print(f"Pontos recebidos: {count}")
print(f"Maior acerto {maior}")
print(f"Menor acerto: {menor}")
print(f"Total de alunos a utilizar o sistema: {total}")