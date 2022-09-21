#Lista 03 - Questão 01: Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

lista1 = []
lista2 = []
lista3 = []
lista4 = []
n = 0
while 0 <= n <= 100:
    n = int(input("Digite um número: " ))
    if 0 <= n <= 25:
        lista1.append(n)
    elif 26 <= n <= 50:
        lista2.append(n)
    elif 51 <= n <= 75:
        lista3.append(n)
    elif 76 <= n <= 100:
        lista4.append(n)
    else:
        break
print("Há ",len(lista1),"números entre votos 0 e 25." )
print("Há ",len(lista2),"números entre votos 26 e 50." )
print("Há ",len(lista3),"números entre votos 51 e 75." )
print("Há ",len(lista4),"números entre votos 76 e 100." )

