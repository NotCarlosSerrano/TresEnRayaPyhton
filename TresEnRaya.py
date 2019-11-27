# Código tres en raya


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
        movimientoValido = insertarMovimiento(tablero, columna-1, fila-1, turno)
        if (not movimientoValido):
            print('movimiento ilegal')

def movMaquina(tablero, turnoMaquina):
    
    if turnoMaquina == 'X':
        turnoHumano = 'O'
    else:
        turnoHumano = 'X'

    for x in range(len(tablero)):
        for i in range(len(tablero)):
            if tablero[x][i] == turnoHumano:
                print(comprobarPosibleTresEnRaya(tablero, x, i, turnoHumano))
    

def comprobarPosibleTresEnRaya(tablero, x, i, turnoHumano):
    
    # Está en el medio
    if x == 1 and i == 1:
        # Comprobar arriba-izquierda y abajo-derecha
        if tablero[x-i][i-1] == turnoHumano and tablero[x+1][i+1] == ' ':
            return x+1, i+1
        # Comprobar arriba y abajo
        elif tablero[x][i-1] == turnoHumano and tablero[x][i+1] == ' ':
            return x, i+1
        # Comprobar arriba-derecha y abajo-izquierda
        elif tablero[x+1][i-1] == turnoHumano and tablero[x-1][i+1] == ' ':
            return x-1, i+1
        # Comprobar derecha e izquierda
        elif tablero[x+1][i] == turnoHumano and tablero[x-1][i] == ' ':
            return x+1, i
        # Comprobar abajo-derecha y arriba-izquierda
        elif tablero[x+1][i+1] == turnoHumano and tablero[x-1][i-1] == ' ':
            return x-1, i-1
        # Comprobar abajo y arriba
        elif tablero[x][i+1] == turnoHumano and tablero[x][i-1] == ' ':
            return x, i-1
        # Comprobar abajo-izquierda y arriba-derecha
        elif tablero[x-1][i+1] == turnoHumano and tablero[x+1][i-1] == ' ':
            return x+1, i-1
        # Comprobar izquierda y derecha
        elif tablero[x-1][i] == turnoHumano and tablero[x+1][i] == ' ':
            return x+1, i
        # Devolvemos el mismo valor para decir que no hay ninguna posibilidad de hacer tres en raya
        else:
            return x, i
    else:
        print('else')
    

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
        turno = cambiarTurno(turno)
        movMaquina(tablero, turno)
        turno = cambiarTurno(turno)
        acabarPartida = comprobarTresEnRaya(tablero)
        empate = comprobarEmpate(tablero)
        if empate:
            break

    mostrarTablero(tablero)
    if empate and not acabarPartida:
        print('Empate')
    else:
        print('ganador: ', turno)


jugarPartida()
