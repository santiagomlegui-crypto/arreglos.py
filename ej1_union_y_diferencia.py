# Ejercicio 1: Unión y diferencia entre conjuntos
A = set(int(x) for x in input("A (números separados por espacios): ").split())
B = set(int(x) for x in input("B (números separados por espacios): ").split())

print("Unión:", A | B)
print("Diferencia:", A - B)
