num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

if num1 > num2:
    print(f"\nEl número mayor es: {num1}")
elif num2 > num1:
    print(f"\nEl número mayor es: {num2}")
else:
    print("\nAmbos números son iguales.")