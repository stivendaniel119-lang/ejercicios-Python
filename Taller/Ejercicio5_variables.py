numero_A = int(input("Número A: "))
numero_B = int(input("Número B: "))

auxiliar = numero_A  
numero_A = numero_B   
numero_B = auxiliar   

print("\nDespués del intercambio:")
print(f"Número A: {numero_A}")
print(f"Número B: {numero_B}")
