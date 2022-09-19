"""
Este ano tem Copa do Mundo! O país inteiro se prepara para torcer para a equipe canarinho conquistar mais um título, tornando-se hexacampeã.

Na Copa do Mundo, depois de uma fase de grupos, dezesseis equipes disputam a Fase final, composta de quinze jogos eliminatórios.
A figura abaixo mostra a tabela de jogos da Fase final:

Na tabela de jogos, as dezesseis equipes finalistas são representadas por letras maiúsculas (de A a P), e os jogos são numerados de 1 a 15.
Por exemplo, o jogo 3 é entre as equipes identificadas por E e F; o vencedor desse jogo enfrentará o vencedor do jogo 4, e o perdedor será eliminado.
A equipe que vencer os quatro jogos da Fase final será a campeã (por exemplo, para a equipe K ser campeã ela deve vencer os jogos 6, 11, 14 e 15.

Dados os resultados dos quinze jogos da Fase final, escreva um programa que determine a equipe campeã.

Entrada A entrada é composta de quinze linhas, cada uma contendo o resultado de um jogo. A primeira linha contém o resultado do jogo de número 1,
a segunda linha o resultado do jogo de número 2, e assim por diante. O resultado de um jogo é representado por dois números inteiros M e N separados
por um espaço em branco, indicando respectivamente o número de gols da equipe representada à esquerda e à direita na tabela de jogos
(0 ≤ M ≤ 20, 0 ≤ N ≤ 20 e M ≠ N).

Saída Seu programa deve imprimir uma única linha, contendo a letra identificadora da equipe campeã.

Exemplos de Entrada
4 1
1 0
0 4
3 1
2 3
1 2
2 0
0 2
1 2
4 3
0 1
3 2
3 4
1 4
1 0

Exemplos de Saída
F
"""
import string
lista_letras16 = list(string.ascii_uppercase[:16])
lista_letras8 = []
lista_letras4 = []
lista_letras2 = []

for num in range(0, 16, 2):
  pontos = input().split(' ', 2)
  if int(pontos[0]) > int(pontos[1]):
    lista_letras8.append( lista_letras16[num])
  else:
    lista_letras8.append(lista_letras16[num+1])

#4x
for num in range(0, 8, 2):
  pontos = input().split(' ', 2)
  if int(pontos[0]) > int(pontos[1]):
    lista_letras4.append( lista_letras8[num])
  else:
    lista_letras4.append(lista_letras8[num+1])

#2x
for num in range(0, 4, 2):
  pontos = input().split(' ', 2)
  if int(pontos[0]) > int(pontos[1]):
    lista_letras2.append( lista_letras4[num])
  else:
    lista_letras2.append(lista_letras4[num+1])

pontos = input().split(' ', 2)
if int(pontos[0]) > int(pontos[1]):
  print(lista_letras2[0])
else:
  print(lista_letras2[1])