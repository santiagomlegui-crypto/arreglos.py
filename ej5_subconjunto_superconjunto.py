# Ejercicio 5: Subconjunto y superconjunto
A = set(int(x) for x in input("Conjunto A: ").split())
B = set(int(x) for x in input("Conjunto B: ").split())

if A.issubset(B):
    print("A es subconjunto de B")
if B.issubset(A):
    print("B es subconjunto de A")
if A.issuperset(B):
    print("A es superconjunto de B")
if B.issuperset(A):
    print("B es superconjunto de A")
if not (A.issubset(B) or B.issubset(A)):
    print("Ninguno es subconjunto del otro")
