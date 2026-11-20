# Ejercicio 3: Promedio de calificaciones
notas = {}

print('Ingrese "nombre: nota" (línea vacía para terminar)')
while True:
    linea = input("> ").strip()
    if linea == "":
        break
    nombre, nota = linea.split(":")
    notas[nombre.strip()] = float(nota)

if notas:
    print("Promedio general:", sum(notas.values()) / len(notas))
else:
    print("No se ingresaron notas.")
