
print("  SISTEMA DE FACTURACIÓN VETERINARIA")


# 1. Recopilación de datos (Entradas)
propietario = input("Nombre del propietario: ")
mascota = input("Nombre de la mascota: ")
tipo_mascota = input("Tipo de mascota (Perro, Gato, etc.): ")

valor_consulta = float(input("Valor base de la consulta: $"))
costos_adicionales = float(input("Costos adicionales (Medicamentos/Exámenes): $"))
porcentaje_descuento = float(input("Porcentaje de descuento a aplicar (0-100): "))
porcentaje_iva = float(input("Porcentaje de IVA (ej. 19 o 16): "))

# 2. Procesamiento y Cálculos
subtotal = valor_consulta + costos_adicionales
monto_descuento = subtotal * (porcentaje_descuento / 100)
base_imponible = subtotal - monto_descuento
monto_iva = base_imponible * (porcentaje_iva / 100)
total_neto = base_imponible + monto_iva

# 3. Presentación de Resultados (Salidas / Factura)
print("           FACTURA DE ATENCIÓN")
print("Propietario:" {propietario})
print("Paciente:"    {mascota} ({tipo_mascota}))
print("Valor Consulta:"       ${valor_consulta:,.2f})
print("Costos Adicionales:"   ${costos_adicionales:,.2f})
print("Subtotal:"             ${subtotal:,.2f})
print("Descuento ({porcentaje_descuento}%):"   -${monto_descuento:,.2f})
print("IVA ({porcentaje_descuento}%):"           ${monto_iva:,.2f})
print("TOTAL A PAGAR:"        ${total_neto:,.2f})

print("       ¡Gracias por su confianza!")
