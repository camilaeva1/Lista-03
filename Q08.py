#Lista 03 - Questão 08: Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. A disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

from collections import namedtuple
from operator import attrgetter

Carro = namedtuple('Carro', ('nome', 'rendimento'))

carros = [
  Carro(nome='Fusca', rendimento=7.0),
  Carro(nome='Gol', rendimento=10.0),
  Carro(nome='Uno', rendimento=12.5),
  Carro(nome='Vectra', rendimento=9.0),
  Carro(nome='Peugeout', rendimento=14.5)
]

carro_mais_economico = max(carros, key=attrgetter('rendimento'))

print('Mais econômico:', carro_mais_economico.nome)

for i, carro in enumerate(carros):
  consumo = 1000 / carro.rendimento
  gasto = 2.25 * consumo
  print(f'{i+1} - {carro.nome:<10} - {carro.rendimento:>5}  - {consumo: >6.2f} litros - R$ {gasto:.2f}')
