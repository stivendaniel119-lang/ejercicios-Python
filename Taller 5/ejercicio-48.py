cantidad = int(input("Cantidad de libros: "))
biblioteca = {}

for _ in range(cantidad):
    codigo = input("\nCódigo: ")
    titulo = input("Título: ")
    biblioteca[codigo] = titulo

consultar = input("\nConsultar código: ")

print("\nLibro encontrado:\n")
if consultar in biblioteca:
    print(f"{consultar} -> {biblioteca[consultar]}")
else:
    print("Código no registrado.")
