# Ejercicio 3: Intersección de números pares
A = [int(x) for x in input("Lista A: ").split()]
B = [int(x) for x in input("Lista B: ").split()]

comunes_pares = {n for n in set(A) & set(B) if n % 2 == 0}
print(comunes_pares)
