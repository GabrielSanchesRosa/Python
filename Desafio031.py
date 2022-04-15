# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.

distancia = float(input('Qual é a distaância da sua viagem? '))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f"Você esá prestes a começar uma viagem de {distancia:.2f}Km.")
print(f"E o preço de sua passagem será de R${preço:.2f}")
