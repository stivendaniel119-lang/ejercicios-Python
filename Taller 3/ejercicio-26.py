cantidad = int(input("Cantidad: "))
positivos = 0
negativos = 0
ceros = 0

print("\nNúmeros:")
for i in range(cantidad):
    num = float(input())
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1

print(f"\nPositivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")
