def imprime_laberinto(lab):
    print("Laberinto original:")
    for fila in lab:
        print(fila)
    print()


def imprime_camino(res):
    for fila in res:
        print(fila)
    print()


def imprime_por_filas(res):
    for f in range(len(res)):
        print("Impresion", f + 1)

        for x in range(f + 1):
            print(res[x])

        print()


def laberinto(lab, f, c, puntos, camino):
    # Verificar los limites de la matriz
    if f < 0 or f >= len(lab):
        return False
    if c < 0 or c >= len(lab[0]):
        return False

    if lab[f][c] == 0:
        return False

    if (f, c) in camino:
        return False

    camino.append((f, c))

    if lab[f][c] == 3 or lab[f][c] == 4:
        puntos = puntos + lab[f][c]

    if lab[f][c] == 'F':
        if puntos >= 23:
            return True
        else:
            camino.pop()
            return False

    if laberinto(lab, f - 1, c, puntos, camino):
        return True

    if laberinto(lab, f, c + 1, puntos, camino):
        return True

    if laberinto(lab, f + 1, c, puntos, camino):
        return True

    if laberinto(lab, f, c - 1, puntos, camino):
        return True

    # Si no hay salida, retirar esta celda
    camino.pop()
    return False


lab = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

camino = []

imprime_laberinto(lab)

if laberinto(lab, 8, 0, 0, camino):

    res = [[0 for c in range(9)] for f in range(9)]

    for f, c in camino:
        res[f][c] = 1

    imprime_por_filas(res)

    print("Impresion 10")
    print("¡Salimos! Se encontro un camino con 23 puntos o mas.")
    print("Matriz final del camino:")
    imprime_camino(res)

else:
    print("No se encontro un camino con 23 puntos o mas.")