"""Ejercicios Complementarios"""

"""1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección."""
print("----------1----------")
numero1 = 22
print(f"Número Entero: {numero1}")
print(" ")

"""2. No borres la variable número uno y crea una variable llamada "numero2" asignándole
un número decimal de tu elección."""
print("----------2----------")
numero2 = 22.2
print(f"Número Flotante: {numero2}")
print(" ")


"""3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2"."""
print("----------3----------")
suma = numero1 + numero2
print(f"Suma: {suma}")
print(" ")

"""4. Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para
multiplicación y otra para división. Imprime estas variables."""
print("----------4----------")
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"Resultado {numero1} + {numero2}: {suma}")
print(f"Resultado {numero1} - {numero2}: {resta:.2f}")      #Disminuyo la cantidad de decimales que se van a mostrar
print(f"Resultado {numero1} * {numero2}: {multiplicacion}")
print(f"Resultado {numero1} / {numero2}: {division:.2f}")   #Disminuyo la cantidad de decimales que se van a mostrar
print(" ")

"""5. Crea una variable llamada "nombre" y asígnale tu nombre como valor."""
print("----------5----------")
nombre = "Uriel"
print(f"Nombre: {nombre}")
print(" ")

"""6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el
precio de un artículo ficticio."""
print("----------6----------")
precio = 1250.25
print(f"Precio: {precio}")
print(" ")

"""7. Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le
quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al
100% y el valor 0 al 0%"""
print("----------7----------")
descuento = 15
print(f"Descuento: {descuento}")
print(" ")

"""8. Ahora, intenta calcular el precio final aplicando el descuento al precio original y
almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que
aplicar la lógica de matemáticas."""
print("----------8----------")
descuento = (100 - descuento) / 100
precio_final = precio * descuento
print(f"El precio final del producto aplicando un descuento del 15% es de: ${precio_final:.2f}")
print(" ")

"""9. Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu
elección. Qué sea un string"""
print("----------9----------")
cadena = "Hola buenas tardes"
print(f"Cadena: {cadena}")
print(" ")

"""10. Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas
a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de
Python."""
print("----------10----------")
longitud = len(cadena)
print(f"Longitud de la Cadena: {longitud}")
print(" ")

"""11. Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y
conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo
mismo."""
print("----------11----------")
precio = 2250.50
precio_entero = int(precio)
print(f"Precio: {precio}")
print(f"Precio Entero: {precio_entero}")
print(type(precio_entero))
print(" ")

"""12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas
en una tercera variable llamada "nombre_completo", el nombre y el apellido con un
espacio entre medio. Puedes usar libremente la forma de concatenación que quieras"""
print("----------12----------")
nombre = "Uriel"
apellido = "Vera"
nombre_completo = nombre + " " + apellido
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Nombre Completo: {nombre_completo}")
print(" ")

"""13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10."""
print("----------13----------")
edad = 18
print(f"Edad: {edad}")
edad += 5
print(f"Edad: {edad}")
edad -= 10
print(f"Edad: {edad}")
print(" ")

"""14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y
centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3."""
print("----------14----------")
altura = 1.76
print(f"Altura: {altura}")
altura *= 4
print(f"Altura: {altura}")
altura /= 3
print(f"Altura: {altura}")
print(" ")

"""15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después
transfórmalo todo en minúsculas con algún método o función de Python."""
print("----------15----------")
nombre_mayusculas = "URIEL"
print(f"Nombre en Mayusculas: {nombre_mayusculas}")
print(f"Nombre en Minusculas: {nombre_mayusculas.lower()}")
print(" ")

"""16. Por último, con la variable con el nombre en mayúsculas, aplica un método parecido
para que se transforme todo en minúsculas excepto la primera letra"""
print("----------16----------")
nombre_minusculas = nombre_mayusculas.lower()
print("Nombre Final: " + nombre_minusculas.replace("u", "U"))
print(" ")