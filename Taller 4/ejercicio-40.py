cantidad = int(input("Cantidad de productos: "))
productos = []

print("\nProductos:")
for _ in range(cantidad):
    productos.append(input())

print("\nLista de compras:\n")
for indice, producto in enumerate(productos, start=1):
    print(f"{indice}. {producto}")
