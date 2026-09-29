cantidad = int(input("Cantidad de empleados: "))
empleados = {}
suma_salarios = 0

print()
for _ in range(cantidad):
    entrada = input().split()
    identificacion = entrada[0]
    salario = float(entrada[1])
    empleados[identificacion] = salario
    suma_salarios += salario

promedio = suma_salarios / cantidad
print(f"\nSalario promedio: ${promedio:.2f}")
