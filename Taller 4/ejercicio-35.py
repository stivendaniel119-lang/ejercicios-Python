cantidad = int(input("Cantidad de palabras: "))
palabras = []

print("\nPalabras:")
for _ in range(cantidad):
    palabras.append(input())

print("\nLista invertida:\n")
for i in range(len(palabras) - 1, -1, -1):
    print(palabras[i])
