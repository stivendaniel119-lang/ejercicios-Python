num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
operacion = int(input("Operación: "))

if operacion == 1:
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif operacion == 2:
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif operacion == 3:
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif operacion == 4:

    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida.")
