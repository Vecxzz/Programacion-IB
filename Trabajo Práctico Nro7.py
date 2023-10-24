"""Trabajo Práctico Nro 7"""

"""1- Escribe un programa que tome una lista de números como entrada y la ordene
en orden ascendente utilizando el método de ordenamiento de burbuja."""
print("----------1----------")
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

list = [3, 1, 4, 5, 2]
bubble_sort(list)
print("Lista Ordenada")
print(list)
print(" ")


"""2- Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente
en orden ascendente utilizando el método de ordenamiento de selección."""
print("----------2----------")
def selection_sort(words):
    n = len(words)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if words[j] < words[min_index]:
                min_index = j
        if min_index != i:
            words[i], words[min_index] = words[min_index], words[i]

list = ["Benjamin", "Alejandro", "Dario", "Ezequiel", "Cristian"]

print("Palabras Desordenadas: ")
print(list)

selection_sort(list)

print("Palabras Ordenadas: ")
print(list)
print(" ")


"""3- Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor, año de publicación, etc.).
Luego, escribe un programa que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor."""
print("----------3----------")
def bubble_sort(books, field="Año de Publicación"):
    n = len(books)
    for i in range(n):
        for j in range(0, n - i - 1):
            if books[j][field] > books[j + 1][field]:
                books[j], books[j + 1] = books[j + 1], books[j]

books = [
    {"Título": "Bajo la misma estrella", "Autor": "John Green", "Año de Publicación": 2012},
    {"Título": "IT", "Autor": "Stephen King", "Año de Publicación": 1986 },
    {"Título": "Fahrenheit", "Autor": "Ray Bradbury", "Año de Publicación": 1953}
]

bubble_sort(books, "Año de Publicación")

for book in books:
    print(f"Título: {book['Título']}, Autor: {book['Autor']}, Año de Publicación {book['Año de Publicación']}")
print(" ")


"""4- Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su longitud.
Puedes utilizar el método de ordenamiento de inserción."""
print("----------4----------")
def insertion_sort(strings):
    n = len(strings)
    for i in range(1, n):
        key = strings[i]
        j = i - 1
        while j >= 0 and len(key) < len(strings[j]):
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = key

list = ["Benjamin", "Alejandro", "Dario", "Ezequiel", "Cristian"]

print("Lista Desordenada: ")
print(list)

insertion_sort(list)

print("Lista Ordenada: ")
print(list)
print(" ")


"""5- Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente."""
print("----------5----------")
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

list = [3, 1, 4, 5, 2]
bubble_sort(list)
print("Lista Ordenada")
print(list)
print(" ")


"""6- Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de ordenamiento por conteo."""
print("----------6----------")
def counting_sort(numbers):
    if not numbers:
        return numbers
    
    max_value = max(numbers)
    count = [0] * (max_value + 1)

    for num in numbers:
        count[num] += 1

    sorted_numbers = []
    for i in range(max_value + 1):
        sorted_numbers.extend([i] * count[i])
    
    return sorted_numbers

list = [3, 1, 4, 5, 2, 7, 10, 6, 9, 8]
sorted_numbers = counting_sort(list)
print(sorted_numbers)
print(" ")


"""7- Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que ordene esta lista de manera que
primero estén los números ordenados de menor a mayor y luego las cadenas de caracteres ordenadas alfabéticamente."""
print("----------7----------")
def order_numbers_strings(list):
    numbers = []
    strings = []

    for i in list:
        if isinstance(i, (int, float)):
            numbers.append(i)
        elif isinstance(i, str):
            strings.append(i)
        
    numbers.sort()
    strings.sort()

    sorted_list = numbers + strings
    return sorted_list

mixed_list = ["Lionel Messi", 10, "Cristiano Ronaldo", 7, "Erling Haaland", 9]
sorted_mixed_list = order_numbers_strings(mixed_list)
print(sorted_mixed_list)
print(" ")


"""8- Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números."""
print("----------8----------")
def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2  
        left_half = numbers[:mid]
        right_half = numbers[mid:]

        merge_sort(left_half)  
        merge_sort(right_half)  

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                numbers[k] = left_half[i]
                i += 1
            else:
                numbers[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            numbers[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            numbers[k] = right_half[j]
            j += 1
            k += 1

list = [3, 1, 4, 5, 2, 7, 10, 6, 9, 8]
print("Lista Desordenada:")
print(list)

merge_sort(list)
print("Lista Ordenada:")
print(list)
print(" ")