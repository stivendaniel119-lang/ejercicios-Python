frase = input("Frase:\n\n")
palabras = frase.split()
conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print("\nSalida esperada:\n")
for palabra, cantidad in conteo_palabras.items():
    print(f"{palabra} : {cantidad}")
