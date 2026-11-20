# Ejercicio 5: Transposición de una matriz
import ast

A = ast.literal_eval(input("Matriz: "))

transpuesta = [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
print(transpuesta)
