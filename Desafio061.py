# Rafaça o Desafio051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão unsando a estrutura while.

print("Gerador de PA")
print("-=" * 10)

primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão da PA: "))

termo = primeiro
cont = 1

while cont <= 10:
  print(f"{termo} -> ", end="")
  termo += razao
  cont += 1

print("FIM")