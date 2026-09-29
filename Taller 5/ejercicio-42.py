cantidad = int(input("Cantidad de contactos: "))
agenda = {}

for _ in range(cantidad):
    nombre = input("\nNombre: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono

buscar = input("\nBuscar contacto: ")

if buscar in agenda:
    print(f"\nTeléfono de {buscar}: {agenda[buscar]}")
else:
    print("\nContacto no encontrado.")
