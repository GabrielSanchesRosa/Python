# Crie um programa que leia dois valores e mostre um meno como o a baixo na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input("Primeiro Valor: "))
n2 = int(input("Segundo Valor: "))

opção = 0

while opção != 5:
  print('''  [ 1 ] Somar
  [ 2 ] Multiplicar
  [ 3 ] Maior
  [ 4 ] Novos Números
  [ 5 ] Sair do programa''')

  opção = int(input(">>>>> Qual é a sua opção? "))

  if opção == 1:
    soma = n1 + n2
    print(f"A soma entre {n1} + {n2} é {soma}.")
  elif opção == 2:
    produto = n1 * n2
    print(f"O resultado de {n1} X {n2} é {produto}.")
  elif opção == 3:
    if n1 > n2:
      maior = n1
    else:
      maior = n2
    print(f"Entre {n1} e {n2} o maior valor é {maior}.")
  elif opção == 4:
    print("Informe os números novamente: ")
    n1 = int(input("Primeiro Valor: "))
    n2 = int(input("Segundo Valor: "))
  elif opção == 5:
    print("Finalizando...")
  else:
    print("Opção inválida. Tente Novamente.")
  print("=-=" * 10)
  sleep(1)
print("Fim do programa! Volte Sempre!")
