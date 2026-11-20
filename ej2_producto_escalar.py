# Ejercicio 2: Producto escalar de dos listas
a = [float(x) for x in input("Lista A: ").split()]
b = [float(x) for x in input("Lista B: ").split()]

if len(a) != len(b):
    print("Error: las listas deben tener el mismo tamaño.")
else:
    producto = sum(a[i] * b[i] for i in range(len(a)))
    if producto.is_integer():
        producto = int(producto)
    print("Producto escalar =", producto)
