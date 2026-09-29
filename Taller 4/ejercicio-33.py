cantidad = int(input("Cantidad de números: "))
numeros = []
pares = 0
impares = 0

print("\nNúmeros:")
for _ in range(cantidad):
    numeros.append(int(input()))

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nPares: {pares}")
print(f"Impares: {impares}")
