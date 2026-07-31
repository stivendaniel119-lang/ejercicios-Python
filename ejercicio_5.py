comensales = int(input("Número de comensales: "))

# 200g por persona = 200 * comensales gramos de patatas
patatas_g = 200 * comensales
patatas_kg = patatas_g / 1000

# Por cada kilo: 5 huevos y 300g de cebolla
huevos = patatas_kg * 5
cebolla_g = patatas_kg * 300

print("Patatas necesarias:" {patatas_g} gramos)
print("Huevos necesarios:" {huevos:.1f})
print("Cebolla necesaria:" {cebolla_g} gramos)