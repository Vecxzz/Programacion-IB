"""Trabajo Práctico Nro 9"""

"""1- Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
•	Un constructor, donde los datos pueden estar vacíos.
•	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
•	mostrar(): Muestra los datos de la persona.
•	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad."""
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    #Getters
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_dni(self):
        return self.dni
    
    #Setters
    def set_nombre(self, nombre):
        if len(nombre) > 0:
            self.nombre = nombre
        else:
            print("El nombre no es válido")
    
    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad ingresada no es válida")
    
    def set_dni(self, dni):
        if len(dni) == 8:
            self.dni = dni
        else:
            print("El DNI ingresado no es válido")

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def esMayor(self):
        return self.edad >= 18
    
persona = Persona()
persona.set_nombre("Uriel Vera")
persona.set_edad(18)
persona.set_dni("46328687")
persona.mostrar()
print(f"¿Es mayor de edad? {persona.esMayor()}")


"""2- Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
•	Un constructor, donde los datos pueden estar vacíos.
•	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
•	mostrar(): Muestra los datos de la cuenta.
•	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
•	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos."""
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad}")

    def ingresar(self, cantidad_a_ingresar):
        if cantidad_a_ingresar > 0:
            self.cantidad += cantidad_a_ingresar
        else:
            print("La cantidad ingresada no es válida")

    def retirar(self, cantidad_a_retirar):
        if cantidad_a_retirar > 0:
            self.cantidad -= cantidad_a_retirar
        else:
            print("La cantidad ingresada no es válida")

cuenta = Cuenta("Uriel Vera")
cuenta.cantidad = 5000.0
cuenta.mostrar()
cuenta.ingresar(2000.0)
cuenta.retirar(1000.0)
cuenta.mostrar()


"""3- Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos,
imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno)."""
class Triangulo:
    def __init__(self, lado1=0.0, lado2=0.0, lado3=0.0, tipo_triangulo=""):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.tipo_triangulo = tipo_triangulo
    
    def mostrar(self):
        ladoMayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor es {ladoMayor}, es un Triángulo: {self.tipo_triangulo}")

triangulo = Triangulo(8.4, 12.3, 7.4, "Escaleno")
triangulo.mostrar()


"""4- Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.
Además deberá mostrar un menú con las siguientes opciones:
•	Añadir contacto
•	Lista de contactos
•	Buscar contacto
•	Editar contacto
•	Cerrar agenda"""
class Contacto:
    def __init__(self, nombre, telefono, mail):
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contactos(self, nombre, telefono, mail):
        nuevo_contacto = Contacto(nombre, telefono, mail)
        self.contactos.append(nuevo_contacto)

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda esta vacia")
        else:
            print("Lista de Contactos: ")
            for contacto in self.contactos:
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Correo Eléctronico: {contacto.mail}")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Correcto Eléctronico: {contacto.mail}")
                return
            print(f"El contacto {nombre} no se encuentra en la agenda")
    
    def editar_contacto(self, nombre, nuevo_telefono, nuevo_mail):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.telefono = nuevo_telefono
                contacto.mail = nuevo_mail
                print(f"El contacto {nombre} ha sido editado con éxito")
                return
            print(f"El contacto {nombre} no se encuentra en la agenda")

    def menu(self):
        while True:
            print("Menú de Agenda: ")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                self.agregar_contacto(nombre, telefono, email)
            elif opcion == "2":
                self.listar_contactos()
            elif opcion == "3":
                nombre = input("Nombre a buscar: ")
                self.buscar_contacto(nombre)
            elif opcion == "4":
                nombre = input("Nombre del contacto a editar: ")
                nuevo_telefono = input("Nuevo teléfono: ")
                nuevo_email = input("Nuevo email: ")
                self.editar_contacto(nombre, nuevo_telefono, nuevo_email)
            elif opcion == "5":
                print("Cerrando la agenda.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

agenda = Agenda()
agenda.menu()