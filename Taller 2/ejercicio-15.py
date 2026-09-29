valor_compra = float(input("Valor de la compra: "))

descuento = 0.0

# Verificar si aplica el descuento del 10%
if valor_compra > 500000:
    descuento = valor_compra * 0.10

total_pagar = valor_compra - descuento

print(f"Descuento: ${descuento:.0f}")
print(f"Total a pagar: ${total_pagar:.0f}")