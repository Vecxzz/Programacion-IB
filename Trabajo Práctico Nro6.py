"""Variables Dimensionadas"""

"""1- Solicitar al usuario que ingrese números, estos deben guardarse en una lista.
Para finalizar el usuario debe ingresar 0, el cual no debe guardarse."""
print("----------1----------")
numbers = []

while True:
    number = int(input("Ingrese un número: "))
    if number == 0:
        break
    numbers.append(number)
print(f"Números ingresados: {numbers}")
print(" ")


"""2- A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia.
Mostrar un mensaje si no es posible eliminar."""
print("----------2----------")
if numbers:
    number_delete = int(input("Ingrese un número que desee eliminar de la lista: "))
    if number_delete in numbers:
        numbers.remove(number_delete)
        print(f"Se elimino el número {number_delete} de la lista")
        print(f"Lista actualizada: {numbers}")
    else:
        print(f"El número {number_delete} no se encuentra en la lista. No se puede eliminar")
print(" ")


"""3- Imprimir la sumatoria de todos los números de la lista"""
print("----------3----------")
if numbers:
    sum = sum(numbers)
    print(f"La suma de todos los números de la lista es: {sum}")
print(" ")


"""4- Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado.
Imprimir esta nueva lista, iterando por ella."""
print("----------4----------")
if numbers:
    new_number = int(input("Ingrese otro número: "))
    min_numbers = [num for num in numbers if num < new_number]

    print(f"Nueva lista con números menores que {new_number}: {min_numbers}")
print(" ")


"""5- Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la
lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2],
la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]"""
print("----------5----------")
if numbers:
    numbers_frequency = {}
    for num in numbers:
        if num in numbers_frequency:
            numbers_frequency[num] += 1
        else:
            numbers_frequency[num] = 1

list_of_tuples = [(number, frequency) for number, frequency in numbers_frequency.items()]
print(f"Nueva lista de tuplas: {list_of_tuples}")
print(" ")


"""6- Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’.
A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.

a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario."""
print("----------6----------")
students = []
repeat = []

print("Alumnos Nivel Primario")
while True:
    name = input("Ingrese el nombre del alumno: ")
    if name == "x":
        break
    students.append(name)

print("Alumnos Nivel Secundario")
while True:
    name = input("Ingrese el nombre del alumno: ")
    if name == "x":
        break
    if name in students:
        repeat.append(name)
    else:
        students.append(name)

primary = students[:]

print(f"Los nombres de los alumnos nivel Primario y Secundario son: {students}")
print(f"Los nombres que se repiten entre el nivel Primario y Secundario son: {repeat}")

not_primary = [name for name in primary if name not in students]
print(f"Los nombres de nivel Primario que no se repiten en el nivel Secundario son: {not_primary}")
print(" ")


"""7- Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings.
Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados."""
print("----------7----------")
times = {}

for _ in range(5):
    string = input("Ingrese un String: ")
    
    for char in string:
        if char in times:
            times[char] += 1
        else:
            times[char] = 1

print("Cantidad total de ocurrencias de cada carácter:")
for char, count in sorted(times.items()):
    print(f"'{char}': {count}")
print(" ")



"""8- Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10,
participaron en un campeonato de fútbol con modalidad todos contra todos.

Escriba un programa que:
o	Lea el cuadro de goles en un arreglo de dos dimensiones.
o	Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
o	Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
o	Determine la cantidad de puntos obtenidos por cada equipo."""
print("----------8----------")
goals = [
    [0, 4, 2, 1],
    [5, 0, 3, 2],
    [0, 2, 0, 1],
    [1, 0, 2, 0],
]

num_teams = len(goals)

points = {team: 0 for team in range(1, num_teams + 1)}

for home_team in range(1, num_teams + 1):
    for away_team in range(1, num_teams + 1):
        if home_team != away_team:
            home_goals = goals[home_team - 1][away_team - 1]
            away_goals = goals[away_team - 1][home_team - 1]

            if home_goals > away_goals:
                points[home_team] += 3
            elif home_goals == away_goals:
                points[home_team] += 1
                points[away_team] += 1
            else:
                points[away_team] += 3

for team, total_points in points.items():
    print(f"Equipo {team}: Puntos = {total_points}")

for home_team in range(1, num_teams + 1):
    goals_scored = sum(goals[home_team - 1])
    goals_received = sum(goals[home_team - 1][i] for i in range(num_teams))
    goal_difference = goals_scored - goals_received
    print(f"Equipo {home_team}: Diferencia de goles = {goal_difference}")
print(" ")


"""9- Escribir un programa que simule el juego clásico de Memoria (Memotest) utilizando matrices.
El juego consiste en un tablero de cartas boca abajo y el objetivo es encontrar todas las parejas de cartas iguales."""
print("----------9----------")
import copy
def showBoard(board):
    pos = 1
    coords2 = {1:'a', 2:'b', 3:'c', 4:'d'}
    print(end='    ')
    for i in range(1,5):
        print(coords2[pos], end = '   ')
        pos += 1
    print("")
    pos = 1
    for i in board:
        print(pos, end='   ')
        for j in i:
            print(j, end = '   ')
        pos +=1
        print("")

def board_state(board):
    board_state_bool = True
    for i in board:
        for j in i:
            if j == 'X':
                return False
    return board_state_bool

def card_input():
    user_coord = input("Ingrese una posición (EJ: b3): ").lower()
    while user_coord[0] not in coords.keys() or int(user_coord[1]) not in coords.values():
        user_coord = input("Ingrese una posición valida: ").lower()
    while current_board[int(user_coord[1])-1][coords[user_coord[0]]] != 'X':
        user_coord = input(f"La carta en las coordenadas {user_coord} ya ha sido revelada: ").lower()
        while user_coord[0] not in coords.keys() or int(user_coord[1]) not in coords.values():
            user_coord = input("Ingrese una posición valida: ").lower()
    while current_board_aux[int(user_coord[1])-1][coords[user_coord[0]]] != 'X':
        user_coord = input(f"Ya has seleccionado esa carta: ").lower()
        while user_coord[0] not in coords.keys() or int(user_coord[1]) not in coords.values():
            user_coord = input("Ingrese una posición valida: ").lower()
    return user_coord

coords = {'a':0, 'b':1, 'c':2, 'd':3}
current_board = [
    ['X','X','X','X'],
    ['X','X','X','X'],
    ['X','X','X','X']]
current_board_aux = copy.deepcopy(current_board)
cards = [
    [1,4,3,2],
    [6,6,5,1],
    [2,5,4,3]]
complete_board = board_state(current_board)

print("Bienvenido a Memotest!")
print("Encuentra todos los pares del tablero para ganar el juego!")
print("El tablero a resolver es el siguiente: ")
print("")
while complete_board == False:
    already_selected = False
    showBoard(current_board)
    print("")
    input_coord = card_input()
    column = input_coord[0]
    column = coords[column]
    row = int(input_coord[1])-1
    current_board_aux[row][column] = cards[row][column]
    first_selected = current_board_aux[row][column]
    showBoard(current_board_aux)
    print("")
    input_coord = card_input()
    column = input_coord[0]
    column = coords[column]
    row = int(input_coord[1])-1
    current_board_aux[row][column] = cards[row][column]
    last_selected = current_board_aux[row][column]
    showBoard(current_board_aux)
    if last_selected == first_selected:
        print("Has encontrado un par!")
        print("")
        current_board = copy.deepcopy(current_board_aux)
    else:
        print("No se ha encontrado un par")
        print("")
        current_board_aux = copy.deepcopy(current_board)
    complete_board = board_state(current_board)

print("Has ganado! Felicidades!")
print(" ")


"""10- Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
a.	la diagonal principal.
b.	la diagonal inversa."""
print("----------10----------")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

principal = [matriz[i][i] for i in range(len(matriz))]

inversa = [matriz[i][len(matriz) - 1 - i] for i in range(len(matriz))]

print(f"Diagonal principal: {principal}")
print(f"Diagonal Inversa: {inversa}")
print(" ")


"""11- Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario."""
print("----------11----------")
divisas = {"Euro": "€", "Dollar": "$", "Yen": "¥"}
divisa = input("Ingrese una divisa: ")

if divisa in divisas:
    symbol = divisas[divisa]
    print(f"El símbolo de {divisa} es {symbol}")
else:
    print("La divisa ingresada no se encuentra en la lista")
print(" ")


"""12- Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>’."""
print("----------12----------")
name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")
adress = input("Ingrese su dirección: ")
phone = input("Ingrese su número de teléfono: ")

user_date = {
    "Nombre": name,
    "Edad": age,
    "Dirección": adress,
    "Telefono": phone
}

message = f"{user_date['Nombre']} tiene {user_date['Edad']} años, vive en {user_date['Dirección']} y su número de teléfono es {user_date['Telefono']}."
print(message)
print(" ")


"""13- Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello."""
print("----------13----------")
fruits = {"Manzana": 80, "Naranja": 100, "Banana": 120, "Durazno": 120}

user_fruit = input("¿Qué fruta le gustaría comprar?: ").title()
if user_fruit in fruits:
    kg_fruit = float(input("¿Cúantos Kilos desea?: "))
    total = fruits[user_fruit] * kg_fruit
    print(f"Usted desea comprar {kg_fruit} Kilos de {user_fruit}. El total es de: ${total}")
else:
    print("La fruta seleccionada no se encuentra en la lista")
print(" ")