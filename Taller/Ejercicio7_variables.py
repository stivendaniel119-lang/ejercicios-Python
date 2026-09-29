precio_original = int(input("Precio: "))
porcentaje_descuento = int(input("Descuento: "))

valor_descuento = int((precio_original * porcentaje_descuento) / 100)
precio_final = precio_original - valor_descuento

print("\nSalida esperada")
print(f"Precio original: ${precio_original}")
print(f"Descuento aplicado: ${valor_descuento}")
print(f"Precio final: ${precio_final}")