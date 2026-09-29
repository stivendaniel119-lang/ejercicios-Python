numero = int(input("Número: "))
suma_impares = 0

for i in range(1, numero + 1):
    if i % 2 != 0:
        suma_impares += i

print(f"La suma de los números impares es: {suma_impares}")
