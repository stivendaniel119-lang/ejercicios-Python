cantidad = int(input("Cantidad de estudiantes: "))
estudiantes = {}

for _ in range(cantidad):
    codigo = input("\nCódigo: ")
    nombre = input("Nombre: ")
    estudiantes[codigo] = nombre

print("\nListado de estudiantes\n")
for codigo, nombre in estudiantes.items():
    print(f"{codigo} -> {nombre}")
