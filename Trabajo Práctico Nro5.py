"""Trabajo Práctico Funciones"""

"""1- Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es.
Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos."""
print("----------1----------")
def dni_valido():
    dni = input("Ingrese su Nro de DNI: ")
    if len(dni) >= 7 and len(dni) <= 8:
        return True
    else:
        return False

print(dni_valido())
print(" ")


"""2- Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas
por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro."""
print("----------2----------")
def longitud_palabra():
    palabra = input("Ingrese una palabra: ").split()
    ultima_palabra = palabra[-1]    
    return len(ultima_palabra)

print(longitud_palabra())
print(" ")


"""3- Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club.
Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante
el ingreso de un nombre vacio.

Precondición: el formato del nombre de los socios será: nombre apellido.
Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2, apellido.
Si un socio tuviera más de un apellido, el usuario solo ingresará uno.

Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario,
el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.

Por cada socio se debe imprimir su identificador único, el cual estará formado por:
el primer nombre, la cantidad de letras del apellido y los 3 primeros dígitos de su DNI."""
print("----------3----------")
def socios():
    datos = []
    while True:
        nombre1 = input("Ingrese su nombre: ")
        if (not nombre1):
            print("Proceso finalizado")
            break
        segundo_nombre = input("¿Tiene segundo nombre? (S/N): ").lower()
        if (segundo_nombre == "s"):
            nombre2 = input("Ingrese su segundo nombre: ")
        else:
            nombre2 = ""
        apellido = input("Ingrese su apellido: ")
        while True:
            dni = input("Ingrese su Nro de DNI: ")
            if len(dni) >= 7 and len(dni) <= 8:
                break
            else:
                print("Ingrese un número de DNI válido")
                print(" ")
        datos.append((nombre1, nombre2, apellido, dni))
        print(" ")
    for socio in datos:
        identificador(socio)

def identificador(socio):
    nombre1, nombre2, apellido, dni = socio
    letras_apellido = len(apellido)
    digitos_dni = dni[:3]
    print(f"Identificador Único: {nombre1}{letras_apellido}{digitos_dni}")

socios()
print(" ")


"""4- Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es múltiplo del otro.
Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo."""
print("----------4----------")
def es_multiplo(n1, n2):
    if (n1 % n2 == 0) or (n2 % n1 == 0):
        return True
    else:
        return False

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if es_multiplo(num1, num2):
    print("Uno de los número es múltiplo del otro")
else:
    print("Ninguno de los números es múltiplo del otro")
print(" ")


"""5- Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y
vaya mostrando la media. El programa pedirá el número de días que se van a introducir."""
print("----------5----------")
def temp_media():
    temp_maxima = float(input("Ingrese la temperatura máxima: "))
    temp_minima = float(input("Ingrese la temperatura mínima: "))
    media = (temp_maxima + temp_minima) / 2
    print(f"La temperatura media de este dia es de {media}")
    print()

dias = int(input("Ingrese la cantidad de dias que desea consultar: "))
contador = dias
while contador != 0:
    temp_media()
    contador -= 1
print(" ")


"""6- Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra.
Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función."""
print("----------6----------")
def espaciado(txt):
    letras = list(txt)
    espacios = ' '.join(letras)
    print(espacios)

texto = input("Ingrese un texto: ")
espaciado(texto)
print(" ")


"""7- Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior."""
print("----------7----------")
def max_min(numeros):
    mayor = max(numeros)
    menor = min(numeros)
    print(f"El mayor es: {mayor}")
    print(f"El menor es: {menor}") 

valores = []
while True:
    num = input("Ingrese un número: ")
    if not num:
        break
    valores.append(int(num))

if valores:
    max_min(valores)
else:
    print("No se ingresaron números: ")
print(" ")


"""8- Diseñar una función que calcule el área y el perímetro de una circunferencia.
Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro."""
print("----------8----------")
import math
def area_perimetro(rad):
    area = math.pi * rad**2
    perimetro = 2 * math.pi * rad
    print(f"El área de la circunferencia es de: {area}")
    print(f"El perimetro de la circunferencia es de: {perimetro}")

radio = float(input("Ingrese el radio de la circunferencia: "))
area_perimetro(radio)
print(" ")


"""9- Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero
si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado
hacer login y si no se ha podido hacer login incremente este valor.

Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login,
solamente tenemos tres oportunidades para intentarlo."""
print("----------9----------")
def login(user, password):
    intentos = 3
    if (user == "usuario1") and (password == "asdasd"):
        return True
    else:
        intentos -= 1
        print(f"Intentalo de nuevo, te quedan {intentos} intentos")
        if (intentos == 0):
            print("Acceso denegado")

usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")
login(usuario, contraseña)
print(" ")


"""10- Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios y porcentajes
del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra."""
print("----------10----------")
def descuento(carrito):
    precio_total = 0
    
    for producto, info in carrito.items():
        precio = info['precio']
        descuento = info['descuento']
        precio_descuento = precio - (precio * descuento / 100)
        precio_total += precio_descuento
    
    return precio_total

carrito_compras = {'Memoria RAM': {'precio': 20.800, 'descuento': 5}, 'Procesador': {'precio': 90.500, 'descuento': 10}, 'Placa Madre': {'precio': 120.200, 'descuento': 15}}

precio_final = descuento(carrito_compras)
print(f"El precio final de la compra con descuento es de: ${precio_final}")
print(" ")


"""11- Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado
de aplicar la función dada a cada uno de los elementos de la lista."""
print("----------11----------")
def modificar_lista(lista):
    nueva_lista = ['@'.join(palabras) for palabras in lista]
    return nueva_lista

def mostrar_lista(modificar_lista, lista):
    nueva_lista = modificar_lista(lista)
    print(f"Nueva lista: {nueva_lista}")

palabras = ["Hola", "buenas", "tardes"]
print(f"Lista original: {palabras}")
mostrar_lista(modificar_lista, palabras)
print(" ")


"""12- Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud."""
print("----------12----------")
def mostrar_frase(frase):
    palabras = frase.split()
    diccionario = {}

    for palabra in palabras:
        diccionario[palabra] = len(palabra)

    return diccionario

frase = input("Ingrese una frase: ")
resultado = mostrar_frase(frase)
print(f"Diccionario de palabras y longitudes: {resultado}")
print(" ")


"""13- Escribir una función que calcule el módulo de un vector."""



"""14- Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida."""
print("----------14----------")
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numero = int(input("Ingrese un número entero: "))
if es_primo(numero):
    print("El número ingresado es primo")
else:
    print("El número ingresado no es primo")
print(" ")


"""15- Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar,
la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario."""
print("----------15----------")
def factorial(num):
    resultado = 1
    for i in range(1, num+1):
        resultado *= i
    return resultado

cantidad_numeros = int(input("¿Cuantos números desea analizar?: "))
total_numeros = 0

for i in range(cantidad_numeros):
    numero = int(input("Ingrese un número: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")
    total_numeros += 1

print(f"Se leyeron {total_numeros} en total")
print(" ")


"""16- Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número,
utilizando para ello una función que calcule la frecuencia."""
print("----------16----------")
def frecuencia(num, dig):
    numero = str(num)
    frecuencia = 0

    for i in numero:
        if i == str(dig):
            frecuencia += 1
    return frecuencia

numero = int(input("Ingrese un número: "))
digit = int(input("Ingrese un dígito: "))
ocurrencias = frecuencia(numero, digit)
print(f"El dígito {digit} aparece {ocurrencias} veces en el número {numero}")
print(" ")


"""17- Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo.
Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces
que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado."""
print("----------17----------")
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def suma_digitos(num):
    suma = 0
    while num > 0:
        suma += num % 10
        num //= 10
    return suma

def frecuencia(num, dig):
    num_str = str(num)
    frecuencia = 0
    for j in num_str:
        if j == str(dig):
            frecuencia += 1
    return frecuencia

mayor_primo = 0
while True:
    numero = int(input("Ingrese un número primo: "))

    if not es_primo(numero):
        break

    if numero > mayor_primo:
        mayor_primo = numero
    
    print(f"Suma de sus dígitos: {suma_digitos(numero)}")

    digito = int(input("Ingrese un dígito: "))
    ocurrencias = frecuencia(numero, digito)
    print(f"EL dígito {digito} aparece {ocurrencias} veces en {numero}")

if mayor_primo > 0:
    resultado_factorial = 1
    for i in range(2, mayor_primo + 1):
        resultado_factorial *= i
    print(f"El factorial del mayor número primo ingresado {mayor_primo} es {resultado_factorial}")
else:
    print("No se ingresaron número primos")
print(" ")