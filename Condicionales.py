print("Bienvenido al Sistema")
fecha = input("A continuación, ingrese la fecha actual en el formato: (dia/mes/año): ")

nombre_dia = fecha.split("/")[0].lower()
mes_num = int(fecha.split("/")[1])
dia_num = int(fecha.split("/")[2])

if (nombre_dia == "lunes" and dia_num <= 31 and mes_num <= 12):
    print("Día Lunes")
    print("Clases de Nivel Inicial")
    respuesta = input("¿Hubó Exámenes? (S/N): ")
    respuesta = respuesta.lower()
    if (respuesta == "s"):
        aprob = int(input("Ingrese la cantidad de alumnos que aprobaron: "))
        desaprob = int(input("Ingrese la cantidad de alumnos que desaprobaron: "))
        porcentaje_aprob = aprob / (aprob + desaprob) * 100
        porcentaje_aprob = porcentaje_aprob.__trunc__()
        print(f"El porcentaje de aprobados fue del {porcentaje_aprob}%")
elif (nombre_dia == "martes" and dia_num <= 31 and mes_num <= 12):
    print("Día Martes")
    print("Clases de Nivel Intermedio")
    respuesta = input("¿Hubó Exámenes? (S/N): ")
    respuesta = respuesta.lower()
    if (respuesta == "s"):
        aprob = int(input("Ingrese la cantidad de alumnos que aprobaron: "))
        desaprob = int(input("Ingrese la cantidad de alumnos que desaprobaron: "))
        porcentaje_aprob = aprob / (aprob + desaprob) * 100
        porcentaje_aprob = porcentaje_aprob.__trunc__()
        print(f"El porcentaje de aprobados fue del {porcentaje_aprob}%")
elif (nombre_dia == "miercoles" or nombre_dia == "miércoles" and dia_num <= 31 and mes_num <= 12):
    print("Día Miércoles")
    print("Clase de Nivel Avanzado")
    respuesta = input("¿Hubó Exámenes? (S/N): ")
    respuesta = respuesta.lower()
    if (respuesta == "s"):
        aprob = int(input("Ingrese la cantidad de alumnos que aprobaron: "))
        desaprob = int(input("Ingrese la cantidad de alumnos que desaprobaron: "))
        porcentaje_aprob = aprob / (aprob + desaprob) * 100
        porcentaje_aprob = porcentaje_aprob.__trunc__()
        print(f"El porcentaje de aprobados fue del {porcentaje_aprob}%")
elif (nombre_dia == "jueves" and dia_num <= 31 and mes_num <= 12):
    print("Día Jueves")
    print("Clases de Práctica Hablada")
    porcentaje_asis = int(input("Ingrese el porcentaje de alumnos que asistieron: "))
    if (porcentaje_asis > 50):
        print("Asistió la Mayoría")
    else:
        print("Faltó la Mayoria")
elif (nombre_dia == "viernes" and dia_num <= 31 and mes_num <= 12):
    print("Día Viernes")
    print("Clases de Inglés para Viajeros")
    if (dia_num == 1 and mes_num == 1 or mes_num == 7):
        print("Comienzo del Nuevo Ciclo")
        alumnos_ingreso = int(input("Ingrese la cantidad de alumnos ingresantes del nuevo Ciclo: "))
        arancel = int(input("Ingrese el arancel por cada alumno: "))
        total = alumnos_ingreso = arancel
        print(f"El ingreso total: ${total}")
elif (nombre_dia == "sabado" or nombre_dia == "sábado" and dia_num <= 31 and mes_num <= 12):
    print("Día Sabado")
    print("No hay Clases")
elif (nombre_dia == "domingo" and dia_num <= 31 and mes_num <= 12):
    print("Día Doming")
    print("No hay Clases")
else:
    print("Por favor, ingrese una fecha valida.")