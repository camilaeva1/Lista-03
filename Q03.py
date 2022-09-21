#Lista 03 - Questão 03: Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são: 1, 2, 3, 4 - Votos para os respectivos candidatos Voto Nulo
Voto em Branco.
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato; O total de votos nulos; O total de votos em branco; A percentagem de votos nulos sobre o total de votos; A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
branco = 0
nulo = 0
eleitores = int(input("Digite o número de eleitores: "))
for i in range(0, eleitores):
  voto = input("Escolha entre o candidato 1, candidato 2, candidato 3, candidato 4, nulo, branco : ")
  if voto == "1":
    candidato1 = candidato1 + 1
  elif voto == "2":
    candidato2 = candidato2 + 1
  elif voto == "3":
    candidato3 = candidato3 + 1
  elif voto == "4":
    candidato4 = candidato4 + 1
  elif voto == "branco":
    branco = branco + 1
  elif voto == "nulo":
    nulo = nulo + 1
porcnulo = (eleitores*nulo)/100
porcbranco = (eleitores*branco)/100
print("O Candidato 1 obteve {} votos, já o Candidato 2 obteve {}, o Candidato 3 {}, o Candidato 4 {}, foram {} brancos, a porcentagem de brancos foi de {}%, {} nulos, a porcentagem de nulos foi de {} %".format(candidato1, candidato2, candidato3, candidato4, branco, porcbranco, nulo, porcnulo))

