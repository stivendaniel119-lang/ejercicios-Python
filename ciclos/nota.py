estudiantes = []
notas = []


def menu():
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

def opcion2():
    if len(estudiantes) == 0:
        print('estudiantes no registrado')
    else:
     for i in range(len(estudiantes)):
           print(f'Estudiante{estudiantes[i]}Nota{notas[i]}')

def opcion3():
     buscar = input('busacar estudiante')
     encontrado = ('no encontrado')
     i=0
     for estudiantes in estudiantes:
         if buscar == estudiantes:
             encontrado=(f'{buscar}esta en la posicion{i} y saco{notas[i]}de nota')
         1+=1
def opcio4():
    total = 0
    for n in notas:
        total=total+n
    cantidad=len=(notas)
    if cantidad > 0:
        promedio = cantidad
    print