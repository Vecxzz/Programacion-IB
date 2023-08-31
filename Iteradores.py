"""Ejercicios en clase FOR - WHILE"""

"""Ejercicio 1 (FOR)"""
abecedario="abcdefghijklmnñopqrstuvwxyz"
corrimiento=int(input("Ingrese cuantos espacios desea correr: "))

for i in range(5):
    mensaje_ingresado=input("Ingrese un mensaje: ")
    mensaje_ingresado=mensaje_ingresado.lower()
    mensaje_encriptado=" "
    for letra in mensaje_ingresado:
        if letra in abecedario:
            indice=abecedario.find(letra)
            indice=(indice + corrimiento)%27
            mensaje_encriptado += abecedario[indice]
        else:
            mensaje_encriptado += letra
    print(mensaje_encriptado)


"""Ejercicio 2 (WHILE)"""
numero = 1
total_pares = 0
total_impares = 0
while numero != 0:
    numero = int(input("Número: "))
    primer_digito = numero // 10
    ultimo_digito = numero % 10
    pares = 0
    impares = 0
    if (primer_digito % 2 == 0) and (ultimo_digito % 2 == 0):
        pares = 2
        total_pares += 2
        impares = 0
        total_pares += 0
        print(f"Dígitos PARES: {pares} - Dígitos IMPARES: {impares}")
    elif (primer_digito % 2 == 0) and (ultimo_digito % 2 != 0):
        pares = 1
        total_pares += 1
        impares = 1
        total_impares += 1
        print(f"Dígitos PARES: {pares} - Dígitos IMPARES: {impares}")
    elif (primer_digito % 2 != 0) and (ultimo_digito % 2 == 0):
        pares = 1
        total_pares += 1
        impares = 1
        total_impares += 1
        print(f"Dígitos PARES: {pares} - Dígitos IMPARES: {impares}")
    elif (primer_digito % 2 != 0) and (ultimo_digito % 2 != 0):
        pares = 0
        total_pares += 0
        impares = 2
        total_impares += 2
        print(f"Dígitos PARES: {pares} - Dígitos IMPARES: {impares}")

print(f"Total de Dígitos Pares: {total_pares}")
print(f"Total de Dígitos Impares: {total_impares}")
    