#Ingresar el ADN
def enter_dna():
    dna = []
    valid_letters = True

    #Valición de las letras ingresadas por el usuario
    while len(dna) < 6:
        letters = input(f"Ingrese la fila {len(dna) + 1} de la matriz (6 letras): ")
        if len(letters) == 6:
            valid_letters = True
            for i in letters:
                if i not in 'ATCG':
                    valid_letters = False
                    break
            if valid_letters:
                dna.append(letters)
            else:
                print("Las letras ingresadas no son válidas. Inténtalo de nuevo")
                print(" ")
        else:
            print("Has ingresado más/menos de 6 letras. Inténtalo de nuevo")
            print(" ")

    return dna

#Recorrer la matriz y encontrar patrones de 4 letras que coincidan
def find_patterns(dna):
    patterns = []

    for i in range(len(dna)):
        for j in range(len(dna[i])):

            #HORIZONTALES
            if j < len(dna[i]) - 3 and dna[i][j:j + 4] == dna[i][j] * 4:
                patterns.append(dna[i][j:j + 4])

            #DIAGONALES - DERECHA
            if i < len(dna) - 3 and j < len(dna[i]) - 3 and dna[i][j] == dna[i + 1][j + 1] == dna[i + 2][j + 2] == dna[i + 3][j + 3]:
                patterns.append(''.join([dna[i + k][j + k] for k in range(4)]))

            #DIAGONALES - IZQUIERDA
            if i < len(dna) - 3 and j >= 3 and dna[i][j] == dna[i + 1][j - 1] == dna[i + 2][j - 2] == dna[i + 3][j - 3]:
                patterns.append(''.join([dna[i + k][j - k] for k in range(4)]))

    return patterns

#Verificar si el humano es mutante o no
def is_mutant(dna):
    return len(find_patterns(dna)) > 1