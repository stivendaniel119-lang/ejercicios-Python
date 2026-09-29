estudiantes = []
notas = []

def menu():
    print('\n--- MENÚ DE OPCIONES ---')
    print('1. Registrar nuevo estudiante')
    print('2. Mostrar estudiantes')
    print('3. Buscar estudiante') 
    print('4. Promedio general')
    print('5. Salir')   

def opcion1():
    nombre = input('Ingrese nombre del estudiante: ')
    nota = float(input('Ingrese la nota del estudiante: '))
    estudiantes.append(nombre)
    notas.append(nota)
    print(f'¡Estudiante {nombre} registrado con éxito!')

def opcion2():
    if len(estudiantes) == 0:
        print('No hay estudiantes registrados.')
    else:
        print('\n--- Lista de Estudiantes ---')
        for i in range(len(estudiantes)):
            print(f'Estudiante: {estudiantes[i]} | Nota: {notas[i]}')

def opcion3():
    if len(estudiantes) == 0:
        print('No hay estudiantes registrados para buscar.')
        return
        
    buscar = input('Ingrese el nombre del estudiante a buscar: ')
    encontrado = False
    
    # Usamos un ciclo para recorrer con índice sin borrar la lista global
    for i in range(len(estudiantes)):
        if buscar.lower() == estudiantes[i].lower(): # .lower() evita problemas con mayúsculas
            print(f'El estudiante "{buscar}" está en la posición {i+1} y su nota es: {notas[i]}')
            encontrado = True
            break # Detiene la búsqueda al encontrarlo
            
    if not encontrado:
        print('Estudiante no encontrado.')

def opcion4():
    if len(notas) == 0:
        print('No hay notas registradas para calcular el promedio.')
        return

    total = sum(notas) # Usamos sum() para hacerlo más eficiente
    cantidad = len(notas)
    promedio = total / cantidad
    print(f'El promedio general de las notas es: {promedio:.2f}')

# --- CICLO PRINCIPAL DEL PROGRAMA ---
while True:
    menu()
    opcion = input('Seleccione una opción (1-5): ')
    
    if opcion == '1':
        opcion1()
    elif opcion == '2':
        opcion2()
    elif opcion == '3':
        opcion3()
    elif opcion == '4':
        opcion4()
    elif opcion == '5':
        print('¡Gracias por usar el sistema! Saliendo...')
        break
    else:
        print('Opción inválida. Por favor, intente de nuevo.')
