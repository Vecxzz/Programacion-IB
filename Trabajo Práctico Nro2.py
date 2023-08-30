"""Trabajo Práctico Nro2"""

"""1- Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el
computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años."""
print("----------1----------")
edad = int(input("Ingrese la cantidad de años que tiene su computadora: "))
if edad <= 2 and edad > 1:
    print("Su computadora es Nueva")
else:
    print("Su computadora es Vieja")
print(" ")


"""2- Hacer que el programa anterior muestre un mensaje de error si el usuario digita un nnúmero negativo."""
print("----------2----------")
edad = int(input("Ingrese la cantidad de años que tiene su computadora: "))
if edad <= 2 and edad > 1:
    print("Su computadora es Nueva")
elif edad > 2:  
    print("Su computadora es Vieja")
elif edad < 0:
    print("Error, el número ingresado es incorrecto")
print(" ")


"""3- Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación.
Imprimir "coincidencia" si ambos nombres comienzan con la misma letra. Si no es así, imprimir "no hay coincidencia"."""
print("----------3----------")
nombre1 = input("Ingrese el Primer Nombre: ")
nombre2 = input("Ingrese el Segundo Nombre: ")
if nombre1[0] == nombre2[0]:
    print("Coincidencia")
else:
    print("No hay Conincidencia")
print(" ")


"""4- Crear un programa que permita al usuario elegir un candidato por el cual votar.
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.

Según el candidato elegido (A, B o C) se debe imprimir el mensaje: Usted ha votado por el partido [color del candidato elegido].

Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar "Opción errónea."""
print("----------4----------")
print("Bienvenido al Sistema")
print("Ingrese 1 (Para el Partido Rojo) - 2 (Para el Partido Verde) - 3 (Para el Partido Azul)")
voto = int(input("Seleccione el candidato que desea votar: "))
if voto == 1:
    print("Usted ha votado por el Partido Rojo")
elif voto == 2:
    print("Usted ha votado por el Partido Verde")
elif voto == 3:
    print("Usted ha votado por el Partido Azul")
else:
    print("Por favor, seleccione una opción valida")
print(" ")


"""5- Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato."""
print("----------5----------")
letra = input("Ingrese una letra: ")
letra = letra.capitalize()
if len(letra) > 1:
    print("Error. No se puede procesar el dato")
elif letra == "A" and "E" and "I" and "O" and "U":
    print("El Vocal")
else:
    print("No es Vocal")
print(" ")


"""6- Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible
por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400."""
print("----------6----------")
a = int(input("Ingrese el Año: "))
if (a % 2 == 0) and (a % 100 != 0):
    print("Es un Año Bisiesto")
elif (a % 2 == 0) and (a % 400 == 0):
    print("Es un Año Bisiesto")
else:
    print("No es un Año Bisiesto")
print(" ")

"""7- Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres."""
print("----------7----------")
num1 = int(input("Ingrese el Primer Número: "))
num2 = int(input("Ingrese el Segundo Número: "))
num3 = int(input("Ingrese el Tercer Número: "))
if num1 > num2 and num1 > num3:
    print(f"El Número Mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El Número Mayor es: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"El Número Mayor es: {num3}")
print(" ")


"""8- Escribí un programa que solicite ingresar un nombre de usuario y una contraseña.
Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”.
Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”."""
print("----------8----------")
nombre_usuario = input("Ingrese su Nombre de Usuario: ")
clave = input("Ingrese su Contraseña: ")
if nombre_usuario == "Gwenevere" and clave == "excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")
print(" ")


"""9- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""
print("----------9----------")
nombre = input("Ingrese su Nombre: ")
nombre = nombre.capitalize()
genero = input("Ingrese su Sexo (M/F): ")
genero = genero.capitalize()
if nombre[0] == "M" and "N" and "O" and "P" and "Q" and "R" and "S" and "T" and "U" and "V" and "W" and "X" and "Y" and "Z" and genero == "F":
    print("Perteneces al grupo A")
elif nombre[0] == "O" and "P" and "Q" and "R" and "S" and "T" and "U" and "V" and "W" and "X" and "Y" and "Z" and genero == "M":
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")
print(" ")


"""10- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma
automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar
el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es
mayor de 18 años, $1000."""
print("----------10----------")
edad = int(input("Ingrese su Edad: "))
if edad < 4:
    print("Precio de la Entrada: GRATIS")
elif edad >= 4 and edad <=18:
    print("Precio de la Entrada: $500")
elif edad > 18:
    print("Precio de la Entrada: $1000")
print(" ")


"""11- La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un
menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas
la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""
print("----------11----------")
print("Bienvenido a la Pizzeria Bella Napoli")
opcion = input("¿Desea una Pizza Vegetariana? (S/N): ")
opcion = opcion.upper()
if opcion == "S":
    print("A continuación, seleccione que ingredientes Extras desea agregar a su Pizza")
    print("Ingredientes Vegetarianos: (1).Pimiento  (2).Tofu")
    opcion2 = int(input("Seleccione un ingrediente: "))
    if opcion2 == 1:
        extra = "Pimiento"
    elif opcion2 == 2:
        extra = "Tofu"
    print("Su pedido ha sido Finalizado.")
    print(f"Detalles del pedido: Pizza Vegetariana - Ingredientes: Mozzarella, Tomate, {extra}")
elif opcion == "N":
    print("A continuación, seleccione que ingredientes Extras desea agregar a su Pizza")
    print("Ingredientes NO Vegetarianos: (1).Peperoni   (2).Jámon   (3).Salmón")
    opcion2 = int(input("Seleccione un ingrediente: "))
    if opcion2 == 1:
        extra = "Peperoni"
    elif opcion2 == 2:
        extra = "Jámon"
    elif opcion2 == 3:
        extra = "Salmón"
    print("Su pedido ha sido Finalizado.")
    print(f"Detalles del pedido: Pizza NO Vegetariana - Ingredientes: Mozzarella, Tomate, {extra}")
print(" ")


"""12- Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde
ese año o cuántos años faltan para llegar a ese año."""
print("----------12----------")
a = int(input("Ingrese el Año Actual: "))
a2 = int(input("Ingrese un Año Cualquiera: "))
if a > a2:
    print(f"Han pasado {a - a2} años desde {a2} hasta {a}")
elif a < a2:
    print(f"Faltan {a2 - a} años para llegar a {a2}")
print(" ")


"""13- Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
Haciendo que el programa avise cuando se escriben valores negativos o nulos."""
print("----------13----------")
num1 = int(input("Ingrese el Primer Número: "))
num2 = int(input("Ingrese el Segundo Número: "))
mayor = 0
menor = 0
if num1 < 0 or num2 < 0:
    print("Error. Se ha ingresado un valor Negativo")

if num1 > num2:
    mayor = num1
    menor = num2
elif num2 > num1:
    mayor = num2
    menor = num1

if mayor % menor == 0:
    print(f"El Número {mayor} es Múltiplo de {menor}")
print(" ")


"""14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución.
Se recuerda que la fórmula de las soluciones es x = -b / a"""
print("----------14----------")
print("Ecuación a resolver: a x + b = 0")
valor_a = int(input("Ingrese el valor de a: "))
valor_b = int(input("Ingrese el valor de b: "))
valor_x = -valor_b / valor_a
print(f"El valor de X es: {valor_x}")
print(" ")


"""15- Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo.
Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces
la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene
que pedir entonces el radio y escribir el área."""
print("----------15----------")
opcion = input("¿Desea calcular el Área de un Triángulo o de un Círculo? (T/C): ")
opcion = opcion.upper()
if opcion == "T":
    print("Has seleccionado Trángulo")
    base = int(input("Ingrese la Base: "))
    altura = int(input("Ingrese la Altura: "))
    area_t = (base * altura) / 2
    print(f"El Área del Triángulo es: {area_t}")
elif opcion == "C":
    print("Has seleccionado Círculo")
    radio = int(input("Ingrese el Radio: "))
    import math
    area_c = (radio ** 2) * math.pi
    print(f"El Área del Círculo es: {area_c}")
print(" ")


"""16- Haz una calculadora básica pida al usuario dos valores, a y b. Según la opción que desean, realizar la operación:

Si operación es 1 entonces debemos ver el resultado de a + b
Si operación es 2 entonces debemos ver el resultado de a * b
Si operación es 3 entonces debemos ver el resultado de a - b
Si operación es 4 entonces debemos ver el resultado de a / b"""
print("----------16----------")
print("Bienvenido. A continuación, ingrese 2 valores")
num1 = int(input("Ingrese el Primer Valor: "))
num2 = int(input("Ingrese el Segundo Valor: "))
print("Ahora seleccione el tipo de operación que desea realizar")
opcion = int(input("(1).Suma   (2).Multiplicación  (3).Resta   (4).División "))
if opcion == 1:
    resultado = num1 + num2
    print("Ha seleccionado SUMA")
    print(f"El resultado de {num1} + {num2} es: {resultado}")
elif opcion == 2:
    resultado = num1 * num2
    print("Ha seleccionado MULTIPLICACIÓN")
    print(f"El resultado de {num1} * {num2} es: {resultado}")
elif opcion == 3:
    resultado = num1 - num2
    print("Ha seleccionado RESTA")
    print(f"El resultado de {num1} - {num2} es: {resultado}")
elif opcion == 4:
    resultado = num1 / num2
    print("Ha seleccionado DIVISIÓN")
    print(f"El resultado de {num1} / {num2} es: {resultado}")
print(" ")


"""17- Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes,
otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje."""
print("----------17----------")
dia = input("Ingrese el Día Actual: ")
dia = dia.upper()
if dia == "LUNES":
    print(f"Hoy es LUNES. Feliz Comienzo de Semana :)")
elif dia == "MARTES":
    print(f"Hoy es MARTES. Buena Suerte en tu Día :)")
elif dia == "MIERCOLES":
    print(f"Hoy es MIÉRCOLES. Ya vamos por la Mitad :)")
elif dia == "JUEVES":
    print(f"Hoy es JUEVES. Hoy va a ser un Gran Día :)")
elif dia == "VIERNES":
    print(f"Hoy es VIERNES. Feliz Fin de Semana :)")
elif dia == "SABADO":
    print(f"Hoy es SABADO. Espero que te Diviertas Hoy :)")
elif dia == "DOMINGO":
    print(f"Hoy es DOMINGO. Descansa :)")
else:
    print(F"{dia} No es un Día Válido")
print(" ")


"""18- Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes."""
print("----------18----------")
horas = int(input("Ingrese el total de Horas trabajadas durante el ultimo mes: "))
salario = int(input("Ingrese el Salario que gana por Hora: "))
if horas <= 48:
    salario = salario * horas
    print(f"Su salario total es de ${salario}")
elif horas > 48:
    horas_extras = horas - 48
    salario = salario * horas * (horas_extras + 0.10) 
print(" ")


"""19- Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más,
existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento."""
print("----------19----------")
cantidad = int(input("Ingrese la cantidad de lapices que desea comprar: "))
if cantidad >= 1000:
    total = (cantidad * 60) * 0.93
    print(f"El total final a pagar con un descuento del 7% sera de: ${total}")
else:
    print("El total final a pagar sera de: $", (cantidad * 60))
print(" ")


"""20- Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas,
es mayor o igual a 6; caso contrario saldrá desaprobado."""
print("----------20----------")
nota1 = int(input("Ingrese la Primer Nota Obtenida: "))
nota2 = int(input("Ingrese la Segunda Nota Obtenida: "))
nota3 = int(input("Ingrese la Tercera Nota Obtenida: "))
nota4 = int(input("Ingrese la Cuarta Nota Obtenida: "))
promedio = (nota1 + nota2 + nota3 + nota4) / 4
if promedio >= 6:
    print("El Alumno esta Aprobado")
elif promedio < 6:
    print("El Alumno esta Desaprobado")
print(" ")