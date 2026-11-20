# Ejercicio 1: Números mayores que el promedio
entrada = input("Ingrese números separados por espacios: ")
numeros = [float(x) for x in entrada.split()]

promedio = sum(numeros) / len(numeros)
mayores = sorted(n for n in numeros if n > promedio)
mayores = [int(n) if n.is_integer() else n for n in mayores]

print("Promedio:", promedio)
print("Mayores que el promedio:", mayores)
