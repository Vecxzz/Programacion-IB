print("----------1----------")
def valid_dni(dni):
    if len(dni) >= 7 and len(dni) <= 8:
        return True
    else:
        return False

user_dni = input("Ingrese su DNI: ")
valid_dni(user_dni)
print(" ")



print("----------2----------")
def word_length(text):
    words =  text.split()
    last_word = words[-1]    
    return len(last_word)

user_word = input("Ingrese una palabra: ")
length = word_length(user_word)
print(f"La longitud de la última palabra es: {length}")
print(" ")



print("----------3----------")
def partners():
    data = []
    while True:
        name1 = input("Ingrese su nombre: ")
        if (not name1):
            print("Proceso finalizado")
            break
        second_name = input("¿Tiene segundo nombre? (S/N): ").lower()
        if (second_name == "s"):
            name2 = input("Ingrese su segundo nombre: ")
        else:
            name2 = ""
        last_name = input("Ingrese su apellido: ")
        while True:
            dni = input("Ingrese su Nro de DNI: ")
            if len(dni) >= 7 and len(dni) <= 8:
                break
            else:
                print("Ingrese un número de DNI válido")
                print(" ")
        data.append((name1, name2, last_name, dni))
        print(" ")
    for partner in data:
        identificador(partner)

def identificador(partner):
    name1, name2, last_name, dni = partner
    letras_last_name = len(last_name)
    digitos_dni = dni[:3]
    print(f"Identificador Único: {name1}{letras_last_name}{digitos_dni}")

partners()
print(" ")



print("----------4----------")
def is_multiple(n1, n2):
    if (n1 % n2 == 0) or (n2 % n1 == 0):
        return True
    else:
        return False

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if is_multiple(num1, num2):
    print("Uno de los números es múltiplo del otro")
else:
    print("Ninguno de los números es múltiplo del otro")
print(" ")



print("----------5----------")
def average_temp():
    max_temperature = float(input("Ingrese la temperatura máxima: "))
    min_temperature = float(input("Ingrese la temperatura mínima: "))
    average = (max_temperature + min_temperature) / 2
    print(f"La temperatura media de este día es de {average}")
    print()

days = int(input("Ingrese la cantidad de días que desea consultar: "))
counter = days
while counter != 0:
    average_temp()
    counter -= 1
print(" ")



print("----------6----------")
def spacing(txt):
    letters = list(txt)
    spaces = ' '.join(letters)
    return spaces

text = input("Ingrese un texto: ")
result = spacing(text)
print(result)
print(" ")



print("----------7----------")
def max_min(numbers):
    filtered_numbers = [num for num in numbers if num is not None]
    
    if filtered_numbers:
        maximum = max(filtered_numbers)
        minimum = min(filtered_numbers)
        return (minimum, maximum)
    else:
        return None
    
values = []
while True:
    num = input("Ingrese un número: ")
    if not num:
        break
    values.append(int(num))

if values:
    result = max_min(values)
    if result is not None:
        minimum, maximum = result
        print(f"El mayor es: {maximum}")
        print(f"El menor es: {minimum}")
    else:
        print("No se ingresaron números.")
else:
    print("No se ingresaron números.")
print(" ")



print("----------8----------")
import math

def area_perimeter(rad):
    area = math.pi * rad**2
    perimeter = 2 * math.pi * rad
    return (round(area, 2), round(perimeter, 2))

radius = float(input("Ingrese el radio de la circunferencia: "))
result = area_perimeter(radius)
print(f"El área de la circunferencia es de: {result[0]}")
print(f"El perímetro de la circunferencia es de: {result[1]}")
print(" ")



print("----------9----------")
def login(user, password):
    attempts = 3
    if (user == "user1") and (password == "asdasd"):
        return True
    else:
        attempts -= 1
        print(f"Intentalo de nuevo, te quedan {attempts} intentos")
        if (attempts == 0):
            print("Acceso Denegado")
            return False

username = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")
result = login(username, password)

if result:
    print("Bienvenido")
else:
    print("Acceso Denegado")
print(" ")



print("----------10----------")
def discount(cart):
    total_price = 0

    for product, info in cart.items():
        price = info['price']
        discount = info['discount']
        discounted_price = price - (price * discount / 100)
        total_price += discounted_price

    return total_price

shopping_cart = {'Memory RAM': {'price': 20.800, 'discount': 5}, 'Processor': {'price': 90.500, 'discount': 10}, 'Motherboard': {'price': 120.200, 'discount': 15}}

final_price = discount(shopping_cart)
print(f"El precio final de la compra con descuento es de: ${final_price}")
print(" ")



print("----------11----------")
def modify_list(input_list):
    new_list = ['@'.join(words) for words in input_list]
    return new_list

def show_list(modify_function, input_list):
    new_list = modify_function(input_list)
    print(f"Nueva lista: {new_list}")

words = ["Hola", "buenas", "tardes"]
print(f"Lista original: {words}")
show_list(modify_list, words)
print(" ")



print("----------12----------")
def show_sentence(sentence):
    words = sentence.split()
    dictionary = {}

    for word in words:
        dictionary[word] = len(word)

    return dictionary

phrase = input("Ingrese una frase: ")
result = show_sentence(phrase)
print(f"Diccionario de palabras y longitudes: {result}")
print(" ")



print("----------13----------")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = int(input("Ingrese un número entero: "))
if is_prime(number):
    print("El número ingresado es primo")
else:
    print("El número ingresado no es primo")
print(" ")



print("----------14----------")
def factorial(num):
    if num < 0:
        return -1 
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

number_count = int(input("¿Cuantos números desea analizar?: "))
total_numbers = 0

for i in range(number_count):
    number = int(input("Ingrese un número: "))
    result = factorial(number)
    if result == -1:
        print("No se puede calcular el factorial de un número negativo")
    else:
        print(f"El factorial de {number} es {result}")
    total_numbers += 1

print(f"Se leyeron {total_numbers} en total")
print(" ")



print("----------15----------")
def frequency(num, dig):
    number = str(num)
    occurrences = 0

    for i in number:
        if i == str(dig):
            occurrences += 1
    return occurrences

number = int(input("Ingrese un número: "))
digit = int(input("Ingrese un dígito: "))
frequency_count = frequency(number, digit)
print(f"El dígito {digit} aparece {frequency_count} veces en el número {number}")
print(" ")



print("----------16----------")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sum_digits(num):
    sum_value = 0
    while num > 0:
        sum_value += num % 10
        num //= 10
    return sum_value

def frequency(num, dig):
    num_str = str(num)
    occurrences = 0
    for j in num_str:
        if j == str(dig):
            occurrences += 1
    return occurrences

largest_prime = 0
while True:
    number = int(input("Ingrese un número primo: "))

    if not is_prime(number):
        break

    if number > largest_prime:
        largest_prime = number
    
    print(f"Suma de sus dígitos: {sum_digits(number)}")

    digit = int(input("Ingrese un dígito: "))
    occurrences = frequency(number, digit)
    print(f"El dígito {digit} aparece {occurrences} veces en {number}")

if largest_prime > 0:
    factorial_result = 1
    for i in range(2, largest_prime + 1):
        factorial_result *= i
    print(f"El factorial del mayor número primo ingresado {largest_prime} es {factorial_result}")
else:
    print("No se ingresaron números primos")
print(" ")