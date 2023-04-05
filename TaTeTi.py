from random import randrange


def ver_tablero(tablero):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(tablero[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|", sep="")
        print("+-------" * 3,"+", sep="")


def ver_movimiento(tablero):
    eleccion_de_ficha = False  # suposición falsa - la necesitamos para entrar en el bucle
    while not eleccion_de_ficha:
        movimiento = input("Ingresa tu movimiento: ")
        eleccion_de_ficha = len(movimiento) == 1 and movimiento >= '1' and movimiento <= '9'
        if not eleccion_de_ficha:
            print("Movimiento erróneo, ingrésalo nuevamente")
            continue
        movimiento = int(movimiento) - 1 	# numero de la celda, del 0 al 8
        row = movimiento // 3 	# fila de la celda
        col = movimiento % 3		# columna de la celda
        marcar = tablero[row][col]  # marca el cuadro elegido
        eleccion_de_ficha = marcar not in ['O', 'X']
        if not eleccion_de_ficha:  # esta ocupado, ingresa una posición nuevamente
            print("¡Cuadro ocupado, ingresa nuevamente!")
            continue
    tablero[row][col] = 'O' 	# colocar '0' al cuadro seleccionado


def casillas_vacias(tablero):
    libre = []  # la lista esta vacía inicialmente
    for row in range(3):  # itera a través de las filas
        for col in range(3):  # iitera a través de las columnas
            if tablero[row][col] not in ['O', 'X']:  # ¿Está la celda libre?
                # si, agrega una nueva tupla a la lista
                libre.append((row, col))
    return libre


def hay_ganador(tablero, marcar):
    if marcar == "X":  # ¿Estamos buscando X?
        quien = 'yo'  # Si, es la maquina
    elif marcar == "O":  # ... ¿o estamos buscando O?
        quien = 'vos'  # Si, es el usuario
    else:
        quien = None  # ¡No debemos de caer aquí!
        diago1 = diago2 = True  # para las diagonales
    for rc in range(3):
        if tablero[rc][0] == marcar and tablero[rc][1] == marcar and tablero[rc][2] == marcar:  # check row rc
            return quien
        if tablero[0][rc] == marcar and tablero[1][rc] == marcar and tablero[2][rc] == marcar:  # check column rc
            return quien
        if tablero[rc][rc] != marcar:  # revisar la primer diagonal
            diago1 = False
        if tablero[2 - rc][2 - rc] != marcar:  # revisar la segunda diagonal
            diago2 = False
    if diago1 or diago2:
        return quien
    return None


def marcar_tablero(tablero):
    # crea una lista de los cuadros vacios o libres
    libre = casillas_vacias(tablero)
    contador = len(libre)
    if contador > 0:  # si la lista no esta vacía, elegir un lugar para 'X' y colocarla
        this = randrange(contador)
        row, col = libre[this]
        tablero[row][col] = 'X'


tablero = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]  # crear un tablero vacío
tablero[1][1] = 'X'  # colocar la primer 'X' en el centro
libre = casillas_vacias(tablero)
turno_usuario = True  # ¿De quien es turno ahora?
while len(libre):
    ver_tablero(tablero)
    if turno_usuario:
        ver_movimiento(tablero)
        ganador = hay_ganador(tablero, 'O')
    else:
        marcar_tablero(tablero)
        ganador = hay_ganador(tablero, 'X')
    if ganador != None:
        break
    turno_usuario = not turno_usuario
    libre = casillas_vacias(tablero)

ver_tablero(tablero)
if ganador == 'vos':
    print("¡Has ganado!")
elif ganador == 'yo':
    print("¡He ganado!")
else:
    print("¡Empate!")
