# Ejercicio 1: Agenda telefónica
agenda = {}

print('Ingrese "nombre - teléfono" (escriba "fin" para terminar)')
while True:
    linea = input("> ").strip()
    if linea.lower() == "fin":
        break
    if " - " not in linea:
        print("Formato inválido. Use: nombre - teléfono")
        continue
    nombre, telefono = linea.split(" - ", 1)
    agenda[nombre.strip()] = telefono.strip()

print(agenda)
