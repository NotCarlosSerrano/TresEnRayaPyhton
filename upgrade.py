# Si hay una en el centro esa mandará
        if not movRealizado2:

            try:
                fila = movimientos[0]
                columna = movimientos[1]

                if tablero[fila][columna] == ' ':
                    insertarMovimiento(tablero, columna, fila, turnoMaquina)
                elif tablero[1][1] == ' ':
                    insertarMovimiento(tablero, 1, 1, turnoMaquina)
                else:
                    print('mov random')
                    movRandoms = movRandom(tablero)
                    insertarMovimiento(tablero, movRandoms[0], movRandoms[1], turnoMaquina)
            except:
                movRandoms = movRandom(tablero)
                insertarMovimiento(tablero, movRandoms[0], movRandoms[1], turnoMaquina)
