"""Trabajo Práctico Nro1 Parte 2"""

"""1. Calcular el perímetro y área de un rectángulo dada su base y su altura."""  
print("----------1----------")
base = float(input("Ingrese la base del Rectángulo: "))
altura = float(input("Ingrese la altura del Rectángulo: "))
perimetro = (base * 2) + (altura * 2)
area = base * altura
print(f"Perimetro: {perimetro}")
print(f"Área: {area}")
print(" ")


"""2. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""
print("----------2----------")
cateto1 = float(input("Ingrese el Cateto 1: "))
cateto2 = float(input("Ingrese el Cateto 2: "))
hipotenusa = (cateto1 ** 2) + (cateto2 ** 2)
hipotenusa = hipotenusa * 1/2
print(f"Hipotenusa: {hipotenusa}")
print(" ")

"""3. Dados dos números, mostrar la suma, resta, división y multiplicación de ambos."""
print("----------3----------")
num1 = int(input("Ingrese el Primer Número: "))
num2 = int(input("Ingrese el Segundo Número: "))
suma = num1 + num2
resta = num1 - num2
div = num1 / num2
mult = num1 * num2
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"División: {div}")
print(f"Multiplicación: {mult}")
print(" ")

"""4. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
C = (F-32)*5/9"""
print("----------4----------")
grados_f = float(input("Ingrese un valor en Grados Fahrenheit: "))
grados_c = (grados_f - 32) * 5/9
print(f"Valor en Grados Celcius: {grados_c}")
print(" ")

"""5. ¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?"""
print("----------5----------")
"""a) A = input(nombre, “¿Cuál es tu canción favorita?”)"""
#El problema está en la variable nombre, la cual esta mal colocada y no deberia ir en un input 
#Solucionado se veria así:      A = input("¿Cuál es tu canción favorita?: ")

"""b) precio = input(“Precio: “)
      total = precio + (precio * 0.1)"""
#El problema está en que se espera recibir un dato numérico, ya sea int o float, pero no se le esta indicando
#a la variable que tipo de dato numérico va a recibir, y por ende el dato se guardará como string.
#Solucionado se veria así:      precio = int(input("Precio: "))

"""c) edad = int(input(“Edad: “))
      print(tu edad es, edad)""" 
#El problema está en la segunda línea, ya que al usar el print no se esta usando comillas para separar lo que 
#es texto de lo que es la variable. Además en la primera línea falta un parentesis para cerrar todo correctamente.
#Solucionado se veria así:      edad = int(input("Edad: "))
#                               print("tu edad es", edad)

"""d) edad = int(input(“Edad: “))
   print(“Veamos si tu edad es 18…”, edad=18)"""
#El problema está en la segunda línea, ya que al momento de concatenar la variable edad se le esta asignando
#un valor y esto provoca un error.
#Solucionado se veria así:      print("Veamos si tu edad es 18...", edad)
print(" ")

"""6. Calcular la media de tres números pedidos por teclado."""
print("----------6----------")
num1 = int(input("Ingrese el Primer Número: "))
num2 = int(input("Ingrese el Segundo Número: "))
num3 = int(input("Ingrese el Tercer Número: "))
media = (num1 + num2 + num3) / 3
print(f"La Media de los 3 numeros es: {media}")
print(" ")

"""7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos
corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos."""
print("----------7----------")
minutos = int(input("Ingrese la cantidad de Minutos: "))
horas = minutos / 60
print(f"{minutos} Minutos equivalen a {horas:.2f} Horas")
print(" ")

"""8.	Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber
cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que
recibirá en el mes tomando en cuenta su sueldo base y comisiones."""
print("----------8----------")
sueldo_base = 5000
extra = 0.10
total = sueldo_base + sueldo_base * (extra * 3)
print(f"El total que recibira por sus ventas es de ${total}")
print(" ")

"""9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea
saber cuanto deberá pagar finalmente por su compra."""
print("----------9----------")
precio = float(input("Ingrese el monto de su compra: "))
descuento = (100 - 15) / 100 
total = precio * descuento
print(f"El monto total de su compra sera de ${total}")
print(" ")

"""10. Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. 
Dicha calificación se compone de los siguientes porcentajes:

• 55% del promedio de sus tres calificaciones parciales.
• 30% de la calificación del examen final.
• 15% de la calificación de un trabajo final.
"""
print("----------10----------")
parcial1 = float(input("Ingrese la califiación obtenida en el Primer Parcial: "))
parcial2 = float(input("Ingrese la calificación obtenida en el Segundo Parcial: "))
parcial3 = float(input("Ingrese la calificación obtenida en el Tercer Parcial: "))
examen_final = float(input("Ingrese la calificación obtenida en el Examen Final: "))
trabajo_final = float(input("Ingrese la calificación obtenida en el Trabajo Final: "))
nota_final = ((parcial1 + parcial2 + parcial3) / 3) * 0.55
nota_final += examen_final * 0.30
nota_final += trabajo_final * 0.15
print(f"La calificación final del alumno sera: {nota_final:.2f}")
print(" ")

"""11. Pide al usuario dos números y muestra la “distancia” entre ellos
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo)."""
print("----------11----------")
num1 = int(input("Ingrese el Primer Número: "))
num2 = int(input("Ingrese el Segundo Número: "))
valor_abs = abs(num1 - num2)
print(f"La distancia entre ambos numeros es: {valor_abs}")
print(" ")

"""12. Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica."""
print("----------12----------")
num = int(input("Ingrese un Número: "))
cuadrada = num ** 0.5
cubica = num ** 0.3 
print(f"La Raíz Cuadrada del número ingresado es: {cuadrada}")
print(f"La Raíz Cúbica del número ingresado es: {cubica:.2f}")
print(" ")

"""13. Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
Ejemplo, si se introduce 23 que muestre 32."""
print("----------13----------")
num = int(input("Ingrese un Número de 2 Cifras: "))
residuo = num % 100
decenas = residuo // 10
unidades = residuo % 10
print(f"El número ingresado fue: {num}")
print(f"El número invertido es: {unidades}{decenas}")
print(" ")

"""14. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que
intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables."""
print("----------14----------")
variable_a = int(input("Ingrese el valor del la Variable A: "))
variable_b = int(input("Ingrese el valor de la Variable B: "))
print(f"El valor de la Variable A es: {variable_a}")
print(f"El valor de la Variable B es: {variable_b}")
auxiliar = variable_a
variable_a = variable_b
variable_b = auxiliar
print(f"El valor de la Variable A ahora es: {variable_a}")
print(f"El valor de la Variable B ahora es: {variable_b}")
print(" ")

"""15. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
Escribir un algoritmo que determine la hora de llegada a la ciudad B."""
print("----------15----------")
hh = int(input("Ingrese la Hora de salida: "))
mm = int(input("Ingrese los Minutos de salida: "))
ss = int(input("Ingrese los Segundos de salida: "))
tiempo = int(input("Ingrese el tiempo de viaje en Segundos: "))
total_segundos = (hh * 3600 + mm * 60 + ss) + tiempo
hh = total_segundos / 3600
mm = total_segundos - (hh * 3600)
ss = total_segundos - (hh * 3600) - (mm * 60)
print(f"La hora de llegada sera: {hh} : {mm} : {ss}")
print(" ")

"""16. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales."""
print("----------16----------")
nombre = input("Ingrese su Nombre: ")
apellido = input("Ingrese su Apellido: ")
print(nombre[0])
print(apellido[0])
print(" ")

"""17. Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario.
A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”."""
print("----------17----------")
usuario = input("Ingrese su Nombre: ")
print(f"Ahora estás en la matrix {usuario}")
print(" ")

"""18. Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante.
A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina.
Imprimir en pantalla el monto final a pagar."""
print("----------18----------")
precio = float(input("Ingrese el monto a pagar: "))
precio += precio * 0.062
precio += precio * 0.10
print(f"El total final a pagar es de ${precio}")
print(" ")

"""19. Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada
uno de ellos en una variable numérica (en total, tres variables diferentes).
Finalmente, mostrar la fecha en formato dd/mm/aaaa."""
print("----------19----------")
dia = int(input("Ingrese su Día de nacimiento: "))
mes = int(input("Ingrese su Mes de nacimiento: "))
a = int(input("Ingrese su Año de nacimiento: "))
print(f"{dia}/{mes}/{a}")
print(" ")

"""20. Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA."""
print("----------20----------")
fecha = int(input("Ingrese su Día de nacimiento: ")), int(input("Ingrese su Mes de nacimiento: ")), int(input("Ingrese su Año de nacimiento: "))
dia = (fecha[0])
mes = (fecha[1])
a = (fecha[2])
print(f"{dia}/{mes}/{a}")
print(" ")

"""21. Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto,
para saber cuántos tanques de combustible consumirá el viaje entero.

Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible,
qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.

Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de
combustible necesarios."""
print("----------21----------")
kilometros = float(input("Ingrese la cantidad de Kilometros que puede recorrer su moto con 1 litro de combustible: "))
litros = float(input("Ingrese la capacidad de combustible en Litros que tiene su tanque: "))
total_kilometros = float(input("Ingrese la cantidad de Kilometros a recorrer: "))
tanques = litros / kilometros 
total_tanques = total_kilometros / tanques
print(f"Para recorrer {total_kilometros} Kilometros se necesitaran {total_tanques} Tanques")
print(" ")