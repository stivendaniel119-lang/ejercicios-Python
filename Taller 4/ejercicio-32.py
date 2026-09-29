cantidad = int(input("Cantidad de números: "))
numeros = []

print("\nNúmeros:")
for _ in range(cantidad):
    numeros.append(int(input()))

mayor = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

print(f"\nMayor: {mayor}")
print(f"Menor: {menor}")
