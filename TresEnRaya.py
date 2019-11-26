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
    if (tablero[fila-1][columna-1] == ' '):
        tablero[fila-1][columna-1] = turno
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
        movimientoValido = insertarMovimiento(tablero, columna, fila, turno)
        if (not movimientoValido):
            print('movimiento ilegal')


def jugarPartida():
    tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    turno = 'X'

    acabarPartida = False

    print('¿Listo para jugar al tres en raya? ¡Empezemos!')

    while not acabarPartida:
        print()
        print('Turno: ', turno)
        mostrarTablero(tablero)
        hacerMovimiento(tablero, turno)
        turno = cambiarTurno(turno)
        acabarPartida = comprobarTresEnRaya(tablero)
        empate = comprobarEmpate(tablero)
        if empate:
            break

    mostrarTablero(tablero)
    if empate and not acabarPartida:
        print('Empate')
    else:
        print('ganador: ', cambiarTurno(turno))


jugarPartida()
