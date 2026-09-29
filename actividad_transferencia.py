print("  SISTEMA DE FACTURACIÓN VETERINARIA")

propietario = input("Nombre del propietario: ")
mascota = input("Nombre de la mascota: ")
tipo_mascota = input("Tipo de mascota (Perro, Gato, etc.): ")

valor_consulta = float(input("Valor base de la consulta: $"))
costos_adicionales = float(input("Costos adicionales (Medicamentos/Exámenes): $"))
porcentaje_descuento = float(input("Porcentaje de descuento a aplicar (0-100): "))
porcentaje_iva = float(input("Porcentaje de IVA (ej. 19 o 16): "))

subtotal = valor_consulta + costos_adicionales
monto_descuento = subtotal * (porcentaje_descuento / 100)
base_imponible = subtotal - monto_descuento
monto_iva = base_imponible * (porcentaje_iva / 100)
total_neto = base_imponible + monto_iva

print("\n" + "="*38)
print("           FACTURA DE ATENCIÓN")
print("="*38)
print(f"Propietario:        {propietario}")
print(f"Paciente:           {mascota} ({tipo_mascota})")
print("-"*38)
print(f"Valor Consulta:      ${valor_consulta:,.2f}")
print(f"Costos Adicionales:  ${costos_adicionales:,.2f}")
print(f"Subtotal:            ${subtotal:,.2f}")
print(f"Descuento ({porcentaje_descuento}%):  -${monto_descuento:,.2f}")
print(f"IVA ({porcentaje_iva}%):        ${monto_iva:,.2f}")
print("-"*38)
print(f"TOTAL A PAGAR:       ${total_neto:,.2f}")
print("="*38)
print("       ¡Gracias por su confianza!")
