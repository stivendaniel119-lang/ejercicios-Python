palabras=input('ingrese su palabra: ').lower()
contador_vocales= 0
for letra in palabras:
    if letra in 'aeiou':
        contador_vocales=contador_vocales+1
print(f'la palabra contiene {contador_vocales} vocales')