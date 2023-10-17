"""Variables Dimensionadas"""

"""Ejercicio 1
def agregar_pasajero(datos_pasajeros):
    nombre = input("Ingrese el nombre del pasajero: ")
    dni = input("Ingrese su número de DNI: ")
    ciudad = input("¿A qué ciudad viaja?: ")
    datos_pasajeros.append((nombre, dni, ciudad))
    print("Pasajero agregado con éxito.")

def agregar_ciudad(ciudades):
    nombre = input("Ingrese el nombre de la ciudad: ")
    pais = input("Ingrese el país al que pertenece: ")
    ciudades.append((nombre, pais))
    print("Ciudad agregada con éxito.")

def buscar_ciudad_por_dni(dni, datos_pasajeros):
    for nombre, dni_pasajero, ciudad in datos_pasajeros:
        if dni == dni_pasajero:
            return ciudad
    return None

def contar_pasajeros_por_ciudad(ciudad, datos_pasajeros):
    return sum(1 for _, _, c in datos_pasajeros if c == ciudad)

def buscar_pais_por_dni(dni, datos_pasajeros, ciudades):
    ciudad = buscar_ciudad_por_dni(dni, datos_pasajeros)
    if ciudad:
        for c, pais in ciudades:
            if c == ciudad:
                return pais
    return None

def contar_pasajeros_por_pais(pais, datos_pasajeros, ciudades):
    return sum(1 for _, _, c in datos_pasajeros if c in [c for c, p in ciudades if p == pais])

datos_pasajeros = []
ciudades = []

while True:
    print("Menú:")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Consultar ciudad por DNI")
    print("4. Consultar cantidad de pasajeros por ciudad")
    print("5. Consultar país por DNI")
    print("6. Consultar cantidad de pasajeros por país")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_pasajero(datos_pasajeros)
    elif opcion == "2":
        agregar_ciudad(ciudades)
    elif opcion == "3":
        dni = input("Ingrese el DNI del pasajero: ")
        ciudad = buscar_ciudad_por_dni(dni, datos_pasajeros)
        if ciudad:
            print(f"El pasajero viaja a la ciudad: {ciudad}")
        else:
            print("Pasajero no encontrado.")
    elif opcion == "4":
        ciudad = input("Ingrese el nombre de la ciudad: ")
        cantidad = contar_pasajeros_por_ciudad(ciudad, datos_pasajeros)
        print(f"La cantidad de pasajeros que viajan a {ciudad} es: {cantidad}")
    elif opcion == "5":
        dni = input("Ingrese el DNI del pasajero: ")
        pais = buscar_pais_por_dni(dni, datos_pasajeros, ciudades)
        if pais:
            print(f"El pasajero viaja a {pais}")
        else:
            print("Pasajero no encontrado.")
    elif opcion == "6":
        pais = input("Ingrese el nombre del país: ")
        cantidad = contar_pasajeros_por_pais(pais, datos_pasajeros, ciudades)
        print(f"La cantidad de pasajeros que viajan a {pais} es: {cantidad}")
    elif opcion == "7":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
print("-----------------------------------------------------------------------------------")"""


"""Ejercicio 2"""
def obtener_domicilios_factura(ventas):
    domicilios = []
    for venta in ventas:
        _, _, _, domicilio = venta
        domicilios.append(domicilio)
    return domicilios

ventas = [("Laura Smith", 12, 2350.75, "Elm Street - 123"), ("Carlos Rodríguez", 20, 1768.45, "Oak Avenue - 741"), ("María López", 4, 4210.60, "Maple Lane - 789")]
domicilios_factura = obtener_domicilios_factura(ventas)
print(domicilios_factura)