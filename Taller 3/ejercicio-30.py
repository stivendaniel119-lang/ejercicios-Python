terminos = int(input("Cantidad de términos: "))

a, b = 0, 1

for i in range(terminos):
    print(a, end=" ")
    a, b = b, a + b
print()  
