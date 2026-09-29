cantidad = int(input("Cantidad de vendedores: "))
registro_ventas = {}

print()
for _ in range(cantidad):
    entrada = input().split()
    vendedor = entrada[0]
    total_vendido = int(entrada[1])
    registro_ventas[vendedor] = total_vendido

vendedor_mayor = None
max_venta = -1

for vendedor, venta in registro_ventas.items():
    if venta > max_venta:
        max_venta = venta
        vendedor_mayor = vendedor

print("\nMayor vendedor:\n")
print(f"{vendedor_mayor} -> ${max_venta}")
