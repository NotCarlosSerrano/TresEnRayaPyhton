from random import randint

# Código tres en raya

# Devulve dos variables, la primera es i y la segunda es x


def comprobarPosibleTresEnRaya(tablero, i, x, turnoHumano):

    # Está en el medio
    if x == 1 and i == 1:
        # Comprobar arriba-izquierda y abajo-derecha
        if tablero[i-1][x-1] == turnoHumano and tablero[i+1][x+1] == ' ':
            return i+1, x+1
        # Comprobar arriba y abajo
        elif tablero[i][x-1] == turnoHumano and tablero[i][x+1] == ' ':
            return i, x+1
        # Comprobar arriba-derecha y abajo-izquierda
        elif tablero[i+1][x-1] == turnoHumano and tablero[i-1][x+1] == ' ':
            return i-1, x+1
        # Comprobar derecha e izquierda
        elif tablero[i+1][x] == turnoHumano and tablero[i-1][x] == ' ':
            return i+1, x
        # Comprobar abajo-derecha y arrxba-xzquxerda
        elif tablero[i+1][x+1] == turnoHumano and tablero[i-1][x-1] == ' ':
            return i-1, x-1
        # Comprobar abajo y arrxba
        elif tablero[i][x+1] == turnoHumano and tablero[i][x-1] == ' ':
            return i, x-1
        # Comprobar abajo-xzquxerda y arrxba-derecha
        elif tablero[i-1][x+1] == turnoHumano and tablero[i+1][x-1] == ' ':
            print('entro aqui ')
            return i+1, x-1
        # Comprobar xzquxerda y derecha
        elif tablero[i-1][x] == turnoHumano and tablero[i+1][x] == ' ':
            return i+1, x
        # Devolvemos el mismo valor para decir que no hay ninguna posibilidad de hacer tres en raya
        else:
            return i, x
    else:
        # Comprobar arriba-izquierda y arriba-centro
        if tablero[0][0] == turnoHumano and tablero[0][1] == turnoHumano and tablero[0][2] == ' ':
            return 0, 2
        # Comprobar izquierda y centro
        elif tablero[1][0] == turnoHumano and tablero[1][1] == turnoHumano and tablero[1][2] == ' ':
            return 1, 2
        # Comprobar abajo-izquierda y abajo-centro
        elif tablero[2][0] == turnoHumano and tablero[2][1] == turnoHumano and tablero[2][2] == ' ':
            return 2, 2
        # Comprobar arriba-derecha y arriba-centro
        elif tablero[0][2] == turnoHumano and tablero[0][1] == turnoHumano and tablero[0][0] == ' ':
            return 0, 0
        # Comprobar derecha y centro
        elif tablero[1][2] == turnoHumano and tablero[1][1] == turnoHumano and tablero[1][0] == ' ':
            return 1, 0
        # Comprobar abajo-derecha y abajo-centro
        elif tablero[2][2] == turnoHumano and tablero[2][1] == turnoHumano and tablero[2][0] == ' ':
            return 2, 0
        # Comprobar arriba-izquierda y izquierda
        elif tablero[0][0] == turnoHumano and tablero[1][0] == turnoHumano and tablero[2][0] == ' ':
            return 2, 0
        # Comprobar arriba-centro y centro
        elif tablero[0][1] == turnoHumano and tablero[1][1] == turnoHumano and tablero[2][1] == ' ':
            return 2, 1
        # Comprobar arriba-derecha y izquierda-centro
        elif tablero[0][2] == turnoHumano and tablero[1][2] == turnoHumano and tablero[2][2] == ' ':
            return 2, 2
        # Comprobar abajo-izquierda y izquierda-centro
        elif tablero[2][0] == turnoHumano and tablero[1][0] == turnoHumano and tablero[0][0] == ' ':
            return 0, 0
        # Comprobar abajo-centro y centro
        elif tablero[2][1] == turnoHumano and tablero[1][1] == turnoHumano and tablero[0][1] == ' ':
            return 0, 1
        # Comprobar abajo-derecha y derecha-centro
        elif tablero[2][2] == turnoHumano and tablero[1][2] == turnoHumano and tablero[0][2] == ' ':
            return 0, 2
        # Comprobar arriba-izquierda y arriba-derecha
        elif tablero[0][0] == turnoHumano and tablero[0][2] == turnoHumano and tablero[0][1] == ' ':
            return 0, 1
        # Comprobar izquierda-centro y derecha-centro
        elif tablero[1][0] == turnoHumano and tablero[1][2] == turnoHumano and tablero[1][1] == ' ':
            return 1, 1
        # Comprobar abajo-izquierda y abajo-derecha
        elif tablero[2][0] == turnoHumano and tablero[2][2] == turnoHumano and tablero[2][1] == ' ':
            return 2, 1
        # Comprobar arriba-izquierda y abajo-izquierda
        elif tablero[0][0] == turnoHumano and tablero[2][0] == turnoHumano and tablero[1][0] == ' ':
            return 1, 0
        # Comprobar arriba-centro y abajo-centro
        elif tablero[0][1] == turnoHumano and tablero[2][1] == turnoHumano and tablero[1][1] == ' ':
            return 1, 1
        # Comprobar arriba-derecha y abajo-derecha
        elif tablero[0][2] == turnoHumano and tablero[2][2] == turnoHumano and tablero[1][2] == ' ':
            return 1, 2
        else:
            return x, i


def movRandom(tablero):

    listaX = []
    listaI = []

    for x in range(len(tablero)):
        for i in range(len(tablero)):
            if tablero[x][i] == ' ':
                listaX.append(x)
                listaI.append(i)

    numRandom = randint(0, len(listaX))
    numRandom -= 1
    num1 = listaI[numRandom]
    num2 = listaX[numRandom]

    return num1, num2


def mostrarTablero(tablero):
    print('   1', ' 2', ' 3', end='')
    for x in range(len(tablero)):
        print()
        print(x+1, ' ', end='')
        for y in range(len(tablero)):
            print(tablero[x][y], ' ', end='')
    print()

# Devuelve True si inserta el movimiento, en caso contrario devuelve False


def insertarMovimiento(tablero, columna, fila, turno):
    if (tablero[fila][columna] == ' '):
        tablero[fila][columna] = turno
        return True
    else:
        return False


def pedirNum(frase=''):
    columna = -1
    while(columna < 1 or columna > 3):
        if (frase != ''):
            print(frase, end='')
        columna = int(input())
    return columna


def comprobarTresEnRaya(tablero):
    if (tablero[0][0] == tablero[0][1] and tablero[0][0] == tablero[0][2] and tablero[0][0] != ' '):
        return True
    elif (tablero[1][0] == tablero[1][1] and tablero[1][0] == tablero[1][2] and tablero[1][0] != ' '):
        return True
    elif (tablero[2][0] == tablero[2][1] and tablero[2][0] == tablero[2][2] and tablero[2][0] != ' '):
        return True
    elif (tablero[0][0] == tablero[1][0] and tablero[0][0] == tablero[2][0] and tablero[0][0] != ' '):
        return True
    elif (tablero[0][1] == tablero[1][1] and tablero[0][1] == tablero[2][1] and tablero[0][1] != ' '):
        return True
    elif (tablero[0][2] == tablero[1][2] and tablero[0][2] == tablero[2][2] and tablero[0][2] != ' '):
        return True
    elif (tablero[0][0] == tablero[1][1] and tablero[0][0] == tablero[2][2] and tablero[0][0] != ' '):
        return True
    elif (tablero[2][0] == tablero[1][1] and tablero[2][0] == tablero[0][2] and tablero[2][0] != ' '):
        return True
    else:
        return False


def comprobarEmpate(tablero):
    if (tablero[0][0] != ' ' and tablero[0][1] != ' ' and tablero[0][2] != ' ' and tablero[1][0] != ' ' and tablero[1][1] != ' ' and tablero[1][2] != ' ' and tablero[2][0] != ' ' and tablero[2][1] != ' ' and tablero[2][2] != ' '):
        return True
    else:
        return False


def cambiarTurno(turno):
    if (turno == 'O'):
        return 'X'
    else:
        return 'O'


def hacerMovimiento(tablero, turno):
    movimientoValido = False

    while not movimientoValido:
        columna = pedirNum('Columna: ')
        fila = pedirNum('Fila: ')
        movimientoValido = insertarMovimiento(
            tablero, columna-1, fila-1, turno)
        if (not movimientoValido):
            print('movimiento ilegal')


def movMaquina(tablero, turnoMaquina):

    if turnoMaquina == 'X':
        turnoHumano = 'O'
    else:
        turnoHumano = 'X'

    movRealizado = False

    # Comprobación si puede ganar
    for x in range(len(tablero)):
        for i in range(len(tablero)):
            if tablero[x][i] == turnoMaquina:
                movimientos = comprobarPosibleTresEnRaya(tablero, i, x, turnoMaquina)

    # Si puede ganar hará el movimiento y marcara movRealizado para ni siquiere buscar la posible derrota
    try:
        fila = movimientos[0]
        columna = movimientos[1]
        if tablero[fila][columna] == ' ':
            insertarMovimiento(tablero, columna, fila, turnoMaquina)
            movRealizado = True
    except:
        print('no existe')

    movRealizado2 = False

    if not movRealizado:
        for x in range(len(tablero)):
            for i in range(len(tablero)):
                if tablero[x][i] == turnoHumano:
                    movimientos = comprobarPosibleTresEnRaya(tablero, i, x, turnoHumano)
                    if x == 1 and i == 1 and movimientos[0] != 1 and movimientos[1] != 1:
                        insertarMovimiento(tablero, movimientos[1], movimientos[0], turnoMaquina)
                        movRealizado2 = True

        # Si hay una en el centro esa mandará
        if not movRealizado2:

            try:
                fila = movimientos[0]
                columna = movimientos[1]

                if tablero[fila][columna] == ' ':
                    insertarMovimiento(tablero, columna, fila, turnoMaquina)
                elif tablero[1][1] == ' ':
                    insertarMovimiento(tablero, 1, 1, turnoMaquina)
                elif tablero[0][0] == ' ' and tablero[2][0] == ' ' and tablero[0][2] == ' ' and tablero[2][2] == ' ':
                    numRandom = randint(0, 3)
                    if numRandom == 0:
                        insertarMovimiento(tablero, 0, 0, turnoMaquina)
                    elif numRandom == 1:
                        insertarMovimiento(tablero, 2, 0, turnoMaquina)
                    elif numRandom == 2:
                        insertarMovimiento(tablero, 0, 2, turnoMaquina)
                    else:
                        insertarMovimiento(tablero, 2, 2, turnoMaquina)
                else:
                    print('mov random')
                    movRandoms = movRandom(tablero)
                    insertarMovimiento(tablero, movRandoms[0], movRandoms[1], turnoMaquina)
                    
            except:
                movRandoms = movRandom(tablero)
                insertarMovimiento(tablero, movRandoms[0], movRandoms[1], turnoMaquina)

            


def jugarPartida():
    tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    turno = 'X'
    print(len(tablero))
    acabarPartida = False

    print('¿Listo para jugar al tres en raya? ¡Empezemos!')

    while not acabarPartida:
        print()
        print('Turno: ', turno)
        mostrarTablero(tablero)
        hacerMovimiento(tablero, turno)
        acabarPartida = comprobarTresEnRaya(tablero)
        empate = comprobarEmpate(tablero)
        if empate or acabarPartida:
            break
        turno = cambiarTurno(turno)
        movMaquina(tablero, turno)
        acabarPartida = comprobarTresEnRaya(tablero)
        empate = comprobarEmpate(tablero)
        if empate or acabarPartida:
            break
        turno = cambiarTurno(turno)

    mostrarTablero(tablero)
    if empate and not acabarPartida:
        print('Empate')
    else:
        print('ganador: ', turno)

jugarPartida()
