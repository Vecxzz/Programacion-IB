"""Trabajo Práctico Nro 8"""

"""1- Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene."""
print("----------1----------")
def digit_count(n):
    if n < 10:
        return 1
    return 1 + digit_count(n // 10)

number = 123
digits = digit_count(number)
print(f"El número {number} tiene {digits} dígitos")
print(" ")


"""2- Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b."""
print("----------2---------")
def power_of(n, b):
    if n == 1:
        return True
    if n < 1 or n % b != 0:
        return False
    return power_of(n // b, b)

number = 64
base = 2
result = power_of(number, base)
print(f"¿{number} es potencia de {base}? {result}")
print(" ")


"""3- Escribir una función recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con
las posiciones en donde se encuentra b dentro de a."""
print("----------3----------")
def positions_of(a, b, start=0):
    index = a.find(b, start)
    if index == -1:
        return []
    return [index] + positions_of(a, b, index + 1)

string_a = "Un tete a tete con Tete"
string_b = "te"
result = positions_of(string_a, string_b)
print(result)
print(" ")


"""4- Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
•	1 es impar.
•	Si un número es impar, su antecesor es par; y viceversa."""
print("----------4----------")
def even(n):
    if n == 0:
        return True
    else:
        return odd(n - 1)

def odd(n):
    if n == 0:
        return False
    else:
        return even(n - 1)

number = 5
is_even = even(number)
is_odd = odd(number)
print(f"El número {number} es par: {is_even}")
print(f"El número {number} es impar: {is_odd}")
print(" ")


"""5- Escribir una función recursiva que encuentre el mayor elemento de una lista."""
print("----------5----------")
def find_largest(list):
    if len(list) == 1:
        return list[0]
    else:
        max_rest = find_largest(list[1:])
        return list[0] if list[0] > max_rest else max_rest

numbers = [1, 5, 3, 2, 4]
largest = find_largest(numbers)
print(f"El elemento más grande de la lista es: {largest}")
print(" ")


"""6- Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces.
Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])"""
print("----------6----------")
def replicate_list(list, n):
    if not list:
        return []
    else:
        return [list[0]] * n + replicate_list(list[1:], n)

numbers = [1, 2, 3, 4, 5]
replicated_list = replicate_list(numbers, 2)
print(replicated_list)
print(" ")


"""7- Implemente un algoritmo, usando una función recursiva, que resuelva la siguiente sumatoria:
K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p

● El programa debe pedir al usuario que ingrese un número n, y un número d,
● Luego debe calcular el valor de K(n, p) usando una función recursiva,
● Debe imprimir el resultado de K(n, p)"""
print("----------7----------")
def solve_summation(n, p):
    if n == 1:
        return p
    else:
        return n * p + solve_summation(n - 1, p)

n = int(input("Enter the value of n: "))
p = int(input("Enter the value of p: "))

result = solve_summation(n, p)
print(f"El resultado K({n}, {p}) es: {result}")
print(" ")


"""8- El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera:
Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha).
Los valores que se encuentran en los bordes del triángulo son todos unos. Cualquier otro valor se calcula sumando
los dos valores contiguos de la fila de arriba. Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra
en la fila n y la columna k."""
print("----------8----------")
def pascal(n, k):
    if k == 0 or k == n:  
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

row = int(input("Enter the row number (n): "))
column = int(input("Enter the column number (k): "))

value = pascal(row, column)
print(f"El valor en la fila {row} y la columna {column} es: {value}")
print(" ")


"""9- Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos,
y un número k, e imprima todas las posibles cadenas de longitud k formadas con los caracteres dados (permitiendo caracteres repetidos)."""
print("----------9----------")
def combinations(list, k, prefix=""):
    if k == 0:
        print(prefix)
        return
    for char in list:
        new_prefix = prefix + char
        combinations(list, k - 1, new_prefix)

characters = ['A', 'E', 'I', 'O', 'U']
length = 2
combinations(characters, length)
print(" ")


"""10- La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de
papel A4 (210 mm de ancho y 297 mm de largo). Las hojas A0 miden 841 mm de ancho y 1189 mm de largo.
A partir de la A0 las siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N).
Siempre se miden en milímetros con números enteros: entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo.

Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva el ancho y el largo de la hoja A(N)
calculada recursivamente a partir de las medidas de la hoja A(N−1), usando la hoja A0 como caso base.
La función debe devolver el ancho y el largo -en ese orden- en una tupla."""
print("----------10----------")
def sheet_A_measurements(N):
    if N == 0:
        return (841, 1189)
    previous_width, previous_length = sheet_A_measurements(N - 1)
    new_width = previous_length // 2
    new_length = previous_width
    return (new_width, new_length)

N = 4
width, length = sheet_A_measurements(N)
print(f"Las medidas de la hoja A{N} son: Ancho = {width} mm, Largo = {length} mm")
print(" ")