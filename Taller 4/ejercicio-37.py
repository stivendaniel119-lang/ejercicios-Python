cantidad = int(input("Cantidad de números: "))
lista = []

print("\nLista:")
for _ in range(cantidad):
    lista.append(int(input()))

n = len(lista)
for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print("\nLista ordenada:\n")
for num in lista:
    print(num)
