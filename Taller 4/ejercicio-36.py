cantidad = int(input("Cantidad de números: "))
lista = []

print("\nLista:")
for _ in range(cantidad):
    lista.append(int(input()))

sin_repetidos = []
for num in lista:
    if num not in sin_repetidos:
        sin_repetidos.append(num)

print("\nLista sin elementos repetidos:\n")
for num in sin_repetidos:
    print(num)
