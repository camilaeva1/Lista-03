#Lista 03 - Quest?o 06: Em uma competi??o de gin?stica, cada atleta recebe votos de sete jurados. A melhor e a pior nota s?o eliminadas. A sua nota fica sendo a m?dia dos votos restantes. Voc? deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcan?adas pelo atleta em sua apresenta??o e depois informe a sua m?dia, conforme a descri??o acima informada (retirar o melhor e o pior salto e depois calcular a m?dia com as notas restantes).
As notas n?o s?o informados ordenadas.
import time
nome_atleta = True
n_atleta = 1
while nome_atleta != '':
    notas = []
    print("\n" * 5)
    print("Atleta n?", n_atleta)
    nome_atleta = input("Digite o nome do atleta: ")
    if nome_atleta == '':
        break
    else:
        n_jurado = 1
        print("\n" * 3)
        for i in range(7):
            print("Jurado n? ", n_jurado)
            nota = float(input("Digite a nota: "))
            notas.append(nota)
            n_jurado += 1
        print("Atleta: ", nome_atleta)
        n_jurado = 1
        count = 0
        for i in range(7):
            print(n_jurado, "? Jurado : ", notas[count])
            n_jurado += 1
            count += 1
        print("Resultado Final:")
        print("Nome do atleta: ", nome_atleta)
        print("Melhor nota: ", max(notas))
        print("Pior nota: ", min(notas))
        notas.remove(max(notas))
        notas.remove(min(notas))
        media = sum(notas) / len(notas)
        print("Media: ", round(media, 2))
        n_atleta += 1
        print("Reiniciando em 5 segundos")
        time.sleep(5)


