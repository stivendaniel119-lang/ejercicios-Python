cantidad_prod = int(input("Cantidad de productos: "))
inventario = {}

for _ in range(cantidad_prod):
    producto = input("\nProducto: ")
    cantidad = int(input("Cantidad: "))
    inventario[producto] = cantidad

consultar = input("\nConsultar producto: ")

if consultar in inventario:
    print(f"\nCantidad disponible de {consultar}: {inventario[consultar]}")
else:
    print("\nProducto no registrado.")
