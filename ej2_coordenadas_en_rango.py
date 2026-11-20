# Ejercicio 2: Coordenadas dentro de un rango
import ast

coordenada = ast.literal_eval(input("Coordenada (x, y): "))
minimo = float(input("Rango - mínimo: "))
maximo = float(input("Rango - máximo: "))

x, y = coordenada
if minimo <= x <= maximo and minimo <= y <= maximo:
    print("Dentro del rango")
else:
    print("Fuera del rango")
