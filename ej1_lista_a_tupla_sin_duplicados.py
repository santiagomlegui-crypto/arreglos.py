# Ejercicio 1: Conversión de lista a tupla sin duplicados
import ast

lista = ast.literal_eval(input("Lista: "))

# dict.fromkeys elimina duplicados conservando el orden (como un set, pero ordenado)
tupla = tuple(dict.fromkeys(lista))
print(tupla)
