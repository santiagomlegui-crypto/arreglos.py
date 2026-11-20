# Ejercicio 3: Empaquetar y desempaquetar datos
nombre = input("Nombre: ")
edad = int(input("Edad: "))
pais = input("País: ")

datos = (nombre, edad, pais)      # empaquetar

n, e, p = datos                   # desempaquetar
print("Nombre:", n)
print("Edad:", e)
print("País:", p)
