# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
# - Até 9 Anos: MIRIM
# - Até 14 Anos: INFANTIL
# - Até 19 Anos: JUNIOR 
# - Até 25 Anos: SÊNIOR
# - Acima: MASTER

from datetime import date

atual = date.today().year
nascimento = int(input("Ano de Nascimento: "))
idade = atual - nascimento

print(f"O atleta tem {idade} anos.")

if idade <= 9:
  print("Classificação: MIRIM")
if idade <= 14:
  print("Classificação: INFANTIL")
if idade <= 19:
  print("Classificação: JUNIOR")
if idade <= 25:
  print("Classificação: SÊNIOR")
else:
  print("Classificação: MASTER")
