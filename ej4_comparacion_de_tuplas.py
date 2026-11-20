# Ejercicio 4: Comparación de tuplas
import ast

t1 = ast.literal_eval(input("Primera tupla: "))
t2 = ast.literal_eval(input("Segunda tupla: "))

if t1 > t2:
    print("La primera tupla es mayor.")
elif t1 < t2:
    print("La segunda tupla es mayor.")
else:
    print("Las tuplas son iguales.")
