# Faça um program que leia três números e mostre qual é o maior e qual é o menor.

a = int(input("Primeiro Valor: "))
b = int(input("Segundo Valor: "))
c = int(input("Terceiro Valor: "))

# Verificando que é menor

menor = a
if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = c

# Verificando que é maior

maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c

print(f"O maior valor digitado foi {maior}.")
print(f"O menor valor digitado foi {menor}.")

