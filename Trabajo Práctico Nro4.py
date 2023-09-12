"""1- Create a while loop with the following characteristics:
• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x."""
print("----------1----------")
x = 1
while x < 30:
    print(f"El valor de X es: {x}")
    x += 1
    if x == 4:
        print("Se salteo el valor 4")
        x += 1
        continue
    elif x == 6:
        print("Se salteo el valor 6")
        x += 1
        continue
    elif x == 10:
        print("Se salteo el valor 10")
        x += 1
        continue
    elif x == 15:
        print("Se rompio la Ejecución del Bucle en el Valor 15")
        break
print(" ")


"""1- Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas.
Deje una línea en blanco para indicar que ha finalizado la entrada de líneas."""
print("----------2----------")
line = " "
while True:
    line = input("Ingrese una Línea de Texto: ").upper().strip()
    if line:
        print(line)
    else:
        break
print(" ")


"""2- Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50


D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos


Ejemplo de una entrada:
D 200
D 200
R 100
D 50
Introducir una línea vacía indica que ha finalizado la bitácora.
La salida de éste programa sería:
350"""
print("----------3----------")
end_loop = 1
deposit = 0
print("Bienvenido al Sistema")
print("Use el comando D [Cantidad] para depositar dinero. Y el comando R [Cantidad] para retirar dinero")
while end_loop != 0:
    operation = input("¿Qué Operación desea Realizar?: ")
    operation = operation.upper()
    operation = operation.split()
    amount = int(operation[1])
    if operation[0] == "D":
        deposit += amount
        print(deposit)
    elif operation[0] == "R":
        deposit -= amount
        print(deposit)
print(" ")


"""4- Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años
en ese rango, que sean bisiestos y múltiplos de 10.
Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400."""
print("----------4----------")
year1 = int(input("Ingrese el Primer Año: "))
year2 = int(input("Ingrese el Segundo Año: "))
while year1 < year2:
    if (year1 % 10 == 0) or (year1 % 4 == 0) and (year1 % 100 != 0) or (year1 % 400 == 0):
        print(year1)
    year1 += 1
print(" ")


"""5- Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for.
Utiliza la declaración continue para omitir los números impares."""
print("----------5----------")
num = 1
for num in range(1,21):
    if num % 2 != 0:
        continue
    else:
        print(num)
print(" ")


"""6- Crea una lista de números y utiliza un bucle for para encontrar un número específico.
Cuando encuentres el número, usa break para salir del bucle."""
print("----------6----------")
import random
list = []
for i in range(30):
    list.append(random.randint(1, 50))
    if list[i] == list[i]+1:
        list[i] += 1
print(list)
encontrar = int(input("¿Qué Número desea buscar en la lista?: "))
for j in list:
    if j == encontrar:
        print(f"Número {encontrar} Encontrado")
        break
    else:
        print("No Encontrado")
print(" ")


"""7- Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3).
Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir del bucle
(Mostrar un mensaje por cada opción elegida)."""
print("----------7----------")
print("Bienvenido al Sistema")
while True:
    print("1.[Opción 1]   2.[Opción 2]   3.[Opción 3]")
    option = int(input("Selecciona una Opción: "))
    if option == 1:
        print("Has Seleccionado la Opción 1")
    elif option == 2:
        print("Has Seleccionado la Opción 2")
    elif option == 3:
        print("Has Seleccionado la Opción 3")
    elif option == 0:
        break