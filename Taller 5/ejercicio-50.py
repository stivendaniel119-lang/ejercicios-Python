cantidad = int(input("Cantidad de estudiantes: "))
gestion_estudiantes = {}

for _ in range(cantidad):
    codigo = input("\nCódigo: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    carrera = input("Carrera: ")
    promedio = float(input("Promedio: "))
    
    gestion_estudiantes[codigo] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "promedio": promedio
    }

mejor_codigo = None
mejor_promedio = -1.0

for codigo, datos in gestion_estudiantes.items():
    if datos["promedio"] > mejor_promedio:
        mejor_promedio = datos["promedio"]
        mejor_codigo = codigo

print("\nMejor estudiante\n")
print(f"Código: {mejor_codigo}")
print(f"Nombre: {gestion_estudiantes[mejor_codigo]['nombre']}")
print(f"Edad: {gestion_estudiantes[mejor_codigo]['edad']}")
print(f"Carrera: {gestion_estudiantes[mejor_codigo]['carrera']}")
print(f"Promedio: {gestion_estudiantes[mejor_codigo]['promedio']}")
