estudiantes= []
notas= []
total= []

cantidad=int(input('cuantos estudinates: ')) 
for i in range(cantidad):
    nombre=input('nombre estudiante: ')
    estudiantes.append(nombre)
    nota=float(input('nota del estudinates: '))
    notas.append(nota) 

for i in range (cantidad):
   print(f'el estudiante{estudiantes[i]}saco {notas[i]}')

buscar = input ('buscar estudiantes: ')
encontardo='no encontrado'

for i in estudiantes:
    if estudiantes == buscar:
       encontardo = print (f'estudiante encontado en {i} con nota de {i}')
       print(encontardo)
for n in notas :
    total = total + n

promedio = total/cantidad
print(promedio)     