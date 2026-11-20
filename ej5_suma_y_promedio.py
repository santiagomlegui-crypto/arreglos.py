# Ejercicio 5: Suma y promedio con tuplas
import ast

tupla = ast.literal_eval(input("Tupla de números: "))

print("Suma =", sum(tupla))
print("Promedio =", sum(tupla) / len(tupla))
