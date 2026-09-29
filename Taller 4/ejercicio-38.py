cantidad = int(input("Cantidad de elementos: "))
lista1 = []
lista2 = []

print("\nLista 1:")
for _ in range(cantidad):
    lista1.append(int(input()))

print("\nLista 2:")
for _ in range(cantidad):
    lista2.append(int(input()))

lista_combinada = []
for num in lista1:
    lista_combinada.append(num)
for num in lista2:
    lista_combinada.append(num)

print("\nLista combinada:\n")
for num in lista_combinada:
    print(num)
