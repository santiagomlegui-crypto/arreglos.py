# Ejercicio 5: Fusionar diccionarios
import ast

A = ast.literal_eval(input("A = "))
B = ast.literal_eval(input("B = "))

fusion = A.copy()
fusion.update(B)      # B sobrescribe las claves repetidas
print(fusion)
