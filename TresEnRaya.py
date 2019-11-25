# Código tres en raya

def mostrarTablero(tablero):
    print('   1', ' 2', ' 3', end = '')
    for x in range(len(tablero)):
        print()
        print(x+1, ' ', end = '')
        for y in range(len(tablero)):
            print(tablero[x][y], ' ', end = '')

# Devuelve True si inserta el movimiento, en caso contrario devuelve False
def insertarMovimiento(tablero, columna, fila, turno):
    if (tablero[columna-1][fila-1] == ' '):
        tablero[columna-1][fila-1] = turno
        return True
    else:
        return False

def pedirNum():
    columna = -1
    while(columna < 1 or columna > 3):
        columna = int(input())
    return columna

def comprobarTresEnRaya(tablero):
    if (tablero[1][1] == tablero[1][2] and tablero[1][1] == tablero[1][3]):
        print('ganador izquierda')
    elif (tablero[2][1] == tablero[2][2] and tablero[2][1] == tablero[2][3]):
        print('ganador centro-arriba-abajo')
    elif (tablero[3][1] == tablero[3][2] and tablero[3][1] == tablero[3][3]):
        print('ganador derecha')
    elif (tablero[1][1] == tablero[2][1] and tablero[1][1] == tablero[3][1]):
        print('ganador arriba')
    elif (tablero[1][2] == tablero[2][2] and tablero[1][2] == tablero[3][2]):
        print('ganador centro-izq-der')
    elif (tablero[1][3] == tablero[2][3] and tablero[1][3] == tablero[3][3]):
        print('ganador abajo')
    elif (tablero[1][1] == tablero[2][2] and tablero[1][1] == tablero[3][3]):
        print('ganador hor-izq-arr-abajo-der')
    elif tablero[3][1] == tablero[2][2] and tablero[3][1] == tablero[1][3]:
        print('ganbador hor-der-arr-abajo-izq')

def cambiarTurno(turno):
    if (turno == 'O'):
        return 'X'
    else:
        return 'O'

def jugarPartida():
    tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    turno = 'X'
    
    acabarPartida = False

    print('¿Listo para jugar al tres en raya? ¡Empezemos!')

    while not acabarPartida:
        print('a')


jugarPartida()
