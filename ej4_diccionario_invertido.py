# Ejercicio 4: Diccionario invertido
import ast

dic = ast.literal_eval(input("Diccionario: "))

invertido = {v: k for k, v in dic.items()}
print(invertido)
