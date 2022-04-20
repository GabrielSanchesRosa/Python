# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print(f"{' LOJAS GUANABARA ':=^40}")

preço = float(input("Preço das compras: R$"))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista denheiro/ cheque
[ 2 ] à vista cartão
[ 3 ] 2x cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input("Qual a forma de pagamento? "))

if opcao == 1:
  total = preço - (preço * 10 / 100)
elif opcao == 2:
  total = preço - (preço * 5 / 100)
elif opcao == 3:
  total = preço
  parcela = total / 2
  print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.")
elif opcao == 4:
  total = preço + (preço * 20 / 100)
  totparc = int(input("Quantas parcelas? "))
  parcela = total / totparc
  print(f"Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM 20% DE JUROS.")
else:
  total = 0
  print("OPÇÃO INVÁLIDA de pagamento. Tente novamente!")

print(f"Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.")
