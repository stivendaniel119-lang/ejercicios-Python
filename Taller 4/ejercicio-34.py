cantidad = int(input("Cantidad de números: "))
lista = []

print("\nLista:")
for _ in range(cantidad):
    lista.append(int(input()))

buscado = int(input("\nNúmero a buscar: "))
posicion = -1

for i in range(len(lista)):
    if lista[i] == buscado:
        posicion = i
        break

if posicion != -1:
    print(f"\nEl número {buscado} se encuentra en la posición {posicion}.")
else:
    print(f"\nEl número {buscado} no se encuentra en la lista.")
