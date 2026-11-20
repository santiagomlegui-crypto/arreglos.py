# Ejercicio 2: Contador de palabras
frase = input("Frase: ")

conteo = {}
for palabra in frase.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)
