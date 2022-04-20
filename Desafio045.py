# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input("Qual é a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-=" * 11)
print(f"Computador jogou {itens[computador]}.")
print(f"jogador jogou {itens[jogador]}.")
print("-=" * 11)

if computador == 0: # Computador jogou pedra
  if jogador == 0:
    print("EMPATE!")
  elif jogador == 1:
    print("JOGADOR VENCE!")
  elif jogador == 2:
    print("COMPUTADOR VENCE!")
  else:
    print("JOGADA INVÁLIDA")

if computador == 1: # Computador jogou papel
  if jogador == 0:
    print("COMPUTADOR VENCE!")
  elif jogador == 1:
    print("EMPATE!")
  elif jogador == 2:
    print("JOGADOR VENCE!")
  else:
    print("JOGADA INVÁLIDA")
if computador == 2: # COmputador jogou tesoura
  if jogador == 0:
    print("JOGADOR VENCE!")
  elif jogador == 1:
    print("COMPUTADOR VENCE!")
  elif jogador == 2:
    print("EMPATE!")
  else:
    print("JOGADA INVÁLIDA")
