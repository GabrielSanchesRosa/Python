arr = [1,-2,3,4,5]

for n in arr:
  if n < 0:
    arr[n] = 0

if len(arr) == 5:
  soma = arr[0] + arr[1] + arr[2] + arr[3] + arr[4]
  print(soma)

print(arr)