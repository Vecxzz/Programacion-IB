#Importar las funciones correspondientes
from funciones import enter_dna, find_patterns, is_mutant

#Bucle Menú
print("Bienvenido al Sistema")
while True:
    print("1. INGRESAR ADN")
    print("2. SALIR")
    user_option = int(input("¿Qué acción deseas realizar? : "))

    #Si el usuario elige ingresar un ADN
    if user_option == 1:
        dna = enter_dna()
        
        if is_mutant(dna):
            print("El ADN ingresado corresponde a un MUTANTE")
        else:
            print("El ADN ingresado corresponde a un HUMANO")
    elif user_option == 2:
        print("Saliendo del programa")
    else:
        print("La opción ingresada no es válida. Intentelo de nuevo")
    