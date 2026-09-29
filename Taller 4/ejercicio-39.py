cantidad = int(input("Cantidad de números: "))
lista = []

print("\nLista:")
for _ in range(cantidad):
    lista.append(int(input()))

mayor = float('-inf')
segundo_mayor = float('-inf')

for num in lista:
    if num > mayor:
        segundo_mayor = mayor
        mayor = num
    elif num > segundo_mayor and num != mayor:
        segundo_mayor = num

print(f"\nEl segundo número mayor es: {segundo_mayor}")
