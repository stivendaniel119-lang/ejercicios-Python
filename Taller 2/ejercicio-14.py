edad = int(input("Edad: "))

if 0 <= edad <= 12:
    print("Clasificación: Niño")
elif 13 <= edad <= 17:
    print("Clasificación: Adolescente")
elif 18 <= edad <= 59:
    print("Clasificación: Adulto")
elif edad >= 60:
    print("Clasificación: Adulto mayor")
else:
    print("Edad no válida")