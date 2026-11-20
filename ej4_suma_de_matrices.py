# Ejercicio 4: Suma de dos matrices
import ast

A = ast.literal_eval(input("A = "))
B = ast.literal_eval(input("B = "))

if len(A) != len(B) or any(len(A[i]) != len(B[i]) for i in range(len(A))):
    print("Error: las matrices deben tener el mismo tamaño.")
else:
    suma = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    print(suma)
