"""Trabajo Práctico Nro 3"""

"""1- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""
print("----------1----------")
word = input("Ingrese una Palabra: ")
for i in range(10):
    print(word)
print(" ")


"""2- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años
que ha cumplido (desde 1 hasta su edad)."""
print("----------2----------")
age = int(input("Ingrese su Edad: "))
initial_age = 1
for i in range(age):
    print(initial_age)
    initial_age += 1
print(" ")


"""3- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números
impares desde 1 hasta ese número separados por comas."""
print("----------3----------")
num = int(input("Ingrese un numero entero positivo: "))
reply = 0
num_1 = 0
array = ""
while num_1 <= num:
    num_1 += 1
    if (num_1 > 0) and (num_1 % 2 == 0):
        print("")
    else:
        array += str(num_1) + ", "
print(array)
print(" ")


"""4- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
la cuenta atrás desde ese número hasta cero separados por comas."""
print("----------4----------")
num = int(input("Ingrese un Número Entero: "))
for i in range(num+1):
    print(num)
    num -= 1
print(" ")


"""5- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""
print("----------5----------")
investment = float(input("Ingrese la cantidad de dinero que desea invertir: $"))
interest = float(input("Ingrese el interés anual: "))
years = int(input("Ingrese la duración de la inversión: "))
total = 0
for n in range(1, years+1):
    profit = ((investment/100)*interest)*n
    print(f"Las ganancias en el {n} año sera de ${profit}")
print(" ")


"""6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo,
de altura el número introducido."""
print("----------6----------")
num_triangle = int(input("Ingrese un número entero: "))
if num_triangle < 0:
    print("Ingrese un número positivo")
else:
    for i in range(1, num_triangle+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print("")
print(" ")


"""7- Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10."""
print("----------7----------")
mult = 1
while mult < 11:
    print(f"1*{mult}= ", 1*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"2*{mult}= ", 2*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"3*{mult}= ", 3*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"4*{mult}= ", 4*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"5*{mult}= ", 5*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"6*{mult}= ", 6*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"7*{mult}= ", 7*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"8*{mult}= ", 8*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"9*{mult}= ", 9*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"10*{mult}= ", 10*mult)
    mult += 1
print(" ")


"""8- Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo."""
print("----------8----------")
n = int(input("Ingrese un numero entero positivo: "))
for i in range(1,n+1):
    if (i % 2 != 0):
        for j in range(i, 0 , -1) :
            if (j % 2 != 0):
                print(j,end=" ")
           
    print("")
print(" ")


"""9- Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""
print("----------9----------")
password = "contraseña"
user_password = ""
while user_password != password:
    user_password = input("Ingrese la Contraseña: ")
    if user_password != password:
        print("Contraseña Incorrecta")
print("Bienvenido")
print(" ")


"""10- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no."""
print("----------10----------")
num = int(input("Ingrese un número entero: "))
if num % 2 == 0 and num % 3 == 0:
    print(num, " no es un número primo")
else:
    print(num, " es un número primo")
print(" ")


"""11- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la
palabra introducida empezando por la última."""
print("----------11----------")
word_input = input("Ingrese una palabra: ")
for i in range(len(word_input)-1, 0-1, -1):
    print(word_input[i])
print(" ")


"""12- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número
de veces que aparece la letra en la frase."""
print("----------12----------")
phrase = input("Ingrese una frase: ")
letter = input("Ingrese la letra que quiere contar en la frase: ")
phrase = phrase.lower()
letter = letter.lower()
letter_count = phrase.count(letter)
if letter_count == 1:
    print(f"La letra '{letter}' se encuentra {letter_count} vez en la frase '{phrase}'")
elif letter_count > 1:
    print(f"La letra '{letter}' se encuentra {letter_count} veces en la frase '{phrase}'")
else:
    print(f"La letra '{letter}' no se encuentra en la frase '{phrase}'")
print(" ")


"""13- Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará."""
print("----------13----------")
i = 0
while i == 0:
    word = input("Escriba algo: ")
    print (f"[{word}]")
    if (word == "salir") or (word == "Salir"):
        break
print(" ")


"""14- Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles
impares desde el primero hasta el segundo."""
print("----------14----------")
num1 = int(input("Ingrese el Primer Número: "))
num2 = int(input("Ingrese el Segundo Número: "))
if num1 % 2 == 0:
    print(f"{num1} es PAR")
else: 
    print(f"{num1} es IMPAR")

if num2 % 2 == 0:
    print(f"{num2} es PAR")
elif num2 % 2 != 0:
    print(f"{num2} es IMPAR")
print(" ")


"""15- Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores."""
print("----------15----------")
num = int(input("Ingrese un número entero mayor a 0:"))
div = 1
for i in range(num):
    if num % div == 0:
        print(f"{div} es divisor de {num}")
    div += 1
print(" ")


"""16- Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido."""
print("----------16----------")
num_amount = int(input("¿Cúantos números va a ingresar? "))
n = 1
negative_nums = 0
while n < num_amount+1:
    num = int(input("Ingrese un número: "))
    if num < 0:
        negative_nums += 1
    n += 1
print(f"Ha ingresado {negative_nums} números negativos")
print(" ")


"""17- Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas)."""
print("----------17----------")
phrase_1 = input("Ingrse una frase: ")
print("Lista de vocales encontradas en la frase: ", phrase_1)
phrase_1 = phrase_1.lower()
if phrase_1.find("a") >= 1:
    print("a")
if phrase_1.find("e") >= 1:
    print("e")
if phrase_1.find("i") >= 1:
    print("i")
if phrase_1.find("o") >= 1:
    print("o")
if phrase_1.find("u") >= 1:
    print("u")
print(" ")


"""18- Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci.
La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores
en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…"""
print("----------18----------")
fib = int(0)
fib_2 = int(1)
result = int(0)
while result < 55:
    for i in range (0, 10-1):
        result = (fib) + (fib_2)
        fib =  fib_2
        fib_2 = result
        print(result)
print(" ")


"""19- Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad,
que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez
las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo.
El programa deberá comprobar que las cantidades ingresadas sean positivas."""
print("----------19----------")
meta = int(input("¿Cúanto Dinero desea Ahorrar? $"))
saved = 0
while saved < meta:
    saving = 0
    saving = int(input("Ingrese la cantidad que desea ahorrar hoy: $"))
    saved += saving
    print(f"Has ingresado {saving}. Te faltan: ${meta - saved}")
if saved >= meta:
    print(f"Felicidades, has alcanzado tu meta de {meta}. Cantidad ahorrada: {saved}")
print(" ")


"""20- Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados."""
print("----------20----------")
num = int(input("Ingrese un Número Entero: "))
sum = 0
while num != 0:
    sum += num
    num = int(input("Ingrese otro Número para Sumar o 0 si desea Salir: "))
print(f"La Suma Total es {sum}")
print(" ")


"""21- Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado."""
print("----------21----------")
num = int(input("Ingrese un número entero: "))
biggest = num
while num != 0:
    num = int(input("Ingrese otro número o ingrese 0 para salir: "))
    if num > biggest:
        biggest = num
print("El número ingresado más grande es: ", biggest)
print(" ")


"""22- Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen.
La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron
números pares."""
print("----------22----------")
nums = 0
digits_sum = 0
pair = 0
while nums != "-1":
    nums = input("Ingrese un número: ")
    if nums == "-1":
        break
    for x in nums:
        if x == "-":
            continue
        else:
            digits_sum += int(x)
    print("La suma de los dígitos del número ingresado es: ", digits_sum)
    print("Para terminar ingrese el número -1.")
    if int(nums) % 2 == 0:
            pair += 1
    digits_sum = 0
print(pair, " de los números ingresados fueron números pares.")
print(" ")


"""23- Crear un programa que permita al usuario ingresar los montos de las compras de un cliente
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el
usuario ingrese el monto 0."""
print("----------23----------")
print("Bienvenido al Sistema")
mount = 1
total = 0
while mount != 0:
    mount = int(input("Ingrese el monto a pagar por su Producto: $"))
    total += mount
    print(f"Total a pagar: ${total}")
    if mount == 0:
        print(f"El Total Final a Pagar es de: ${total}")
print(" ")


"""24- Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto.
Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000,
se le debe aplicar un 10% de descuento."""
print("----------24----------")
print("Bienvenido al Sistema")
mount = 1
total = 0
end_loop = 1
while end_loop != 0:
    mount = int(input("Ingrese el monto a pagar por su Producto: $"))
    if mount < 0:
        print("Por favor, ingrese un monto valido")
        continue
    elif mount == 0:
        print(f"El Total Final a Pagar es de: ${total}")
        end_loop = 0
    else:
        total += mount
    print(f"Total a pagar: ${total}")
if total > 1000:
    total = total * 0.9
    print(f"Por exeder los $1000 obtienes un descuento del 10%. El Total Final a Pagar es de: ${total}")
