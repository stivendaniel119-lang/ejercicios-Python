palabra = input("Palabra: ")
contador_vocales = 0
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

for letra in palabra:
    if letra in vocales:
        contador_vocales += 1

print(f"La palabra contiene {contador_vocales} vocales.")
