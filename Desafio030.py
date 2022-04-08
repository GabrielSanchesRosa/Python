# Crie um programa que leia um número interio e diga se ele é PAR ou ÍMPAR.

numero = int(input("Me diga um número qualquer: "))
resultado = numero % 2

if resultado == 0:
  print(f"O número {numero} é PAR.")
else:
  print(f"O número {numero} é ÍMPAR.")
