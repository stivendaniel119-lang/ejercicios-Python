cantidad = int(input("Cantidad de estudiantes: "))
registro_notas = {}

print()
for _ in range(cantidad):
    entrada = input().split()
    nombre = entrada[0]
    nota = float(entrada[1])
    registro_notas[nombre] = nota

mejor_estudiante = None
nota_mas_alta = -1.0

for nombre, nota in registro_notas.items():
    if nota > nota_mas_alta:
        nota_mas_alta = nota
        mejor_estudiante = nombre

print("\nEl estudiante con la mejor nota es:\n")
print(f"{mejor_estudiante} -> {nota_mas_alta}")
