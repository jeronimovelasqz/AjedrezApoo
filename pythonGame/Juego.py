import itertools
import exepciones
import itertools
import fichas

# Definimos variables CONSTANTES
# Guia de estilo PEP8

BLANCAS = "blancas"
NEGRAS = "negras"

# uniDict = {WHITE: {Pawn: "♙", Rook: "♖", Knight: "♘", Bishop: "♗", King: "♔", Queen: "♕"},
# BLACK: {Pawn: "♟️", Rook: "♜", Knight: "♞", Bishop: "♝", King: "♚", Queen: "♛"}}


# cardinales y diagonales
chessCardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
chessDiagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]


class Juego:

    def __init__(self):
        self.turno_jugador = NEGRAS
        self.mensaje = "en esta variable iran las indicaciones"
        self.tablero = {}
        self.mover_pieza()
        print("para usar el programa de ajedrez por favor , ingrese\n"
              "el movimiento")
        self.main()

    def main(self):
        while True:
            self.imprimir_tablero()
            print(self.mensaje)
            self.mensaje = ""
            posicion_inicial, posicion_final = self.parseInput()

            try:
                target = self.tablero[posicion_inicial]

            except exepciones.MovimientoInvalido:
                self.mensaje = "no se pudo encontrar la pieza\n" \
                               "index fuera de rango"
                target = None

            if target:
                print("se encontro " + str(target))
                if target.Color != self.turno_jugador:
                    self.mensaje = "usted no puede mover fichas en\n" \
                                   "este turno"
                    continue

                if target.isValid(posicion_inicial, posicion_final, target.Color, self.tablero):
                    self.mensaje = "ha realizado un movimiento valido"
                    self.tablero[posicion_final] = self.tablero[posicion_inicial]
                    del self.tablero[posicion_inicial]
                    self.es_jaque()
                    if self.turno_jugador == NEGRAS:
                        self.turno_jugador = BLANCAS
                    else:
                        self.turno_jugador = NEGRAS

                else:
                    self.mensaje = "movimiento invalido " + str(target.movimientos_disponibles(posicion_inicial[0],
                                                                                               posicion_final[1],
                                                                                               self.tablero))

                    print(target.movimiento_disponibles(posicion_inicial[0], posicion_final[1], self.tablero))
            else:
                self.mensaje = "no existe pieza en ese espacio"

    def mover_pieza(self):

        for pieza in range(0, 8):
            self.tablero[(pieza, 1)] = Peon(BLANCAS, uniDict[BLANCAS][Peon], 1)
            self.tablero[(pieza, 6)] = Peon(NEGRAS, uniDict[NEGRAS][Peon, -1])

        placers = [Torre, Caballo, Alfil, Reina, Rey, Alfil, Caballo, Torre]

        for pieza in range(0, 8):
            self.tablero[(pieza, 0)] = placers[pieza](BLANCAS, uniDict[BLANCAS][placers[pieza]])
            self.tablero[((7 - pieza), 7)] = placers[pieza](NEGRAS, uniDict[NEGRAS][placers[pieza]])
        placers.reverse()

    def es_jaque(self):
        rey = Rey
        reyDict = {}
        piezaDict = {NEGRAS: [], BLANCAS: []}
        for posicion, pieza in self.tablero.items():
            if type(pieza) == Rey:
                reyDict[pieza.Color] = posicion
            print(pieza)

        # blancas
        if self.puede_ver_rey(reyDict[BLANCAS], piezaDict[NEGRAS]):
            self.mensaje = "Jugador de blancas esta en jaque"

        if self.puede_ver_rey(reyDict[NEGRAS], piezaDict[BLANCAS]):
            self.mensaje = "Jugador de negras esta en jaque"

    def puede_ver_rey(self, posicion_rey, lista_de_pieza):
        for pieza, posicion in lista_de_pieza:
            if pieza.isValid(posicion, posicion_rey, pieza.Color, self.tablero):
                return True

    def parseInput(self):
        try:
            a, b = input().split()
            a = ((ord(a[0]) - 97), int(a[1]) - 1)
            b = (ord(b[0]) - 97, int(b[1]) - 1)
            print(a, b)
            return a, b
        except exepciones.InvalidDecoding:
            print("error decoding input. please try again")
            return (-1, -1), (-1, -1)

    def imprimir_tablero(self):
        print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for casilla in range(0, 8):
            print("-" * 32)
            print(chr(casilla + 97), end="|")
            for j in range(0, 8):
                item = self.tablero.get((casilla, j), " ")
                print(str(item) + ' |', end=" ")
            print()
        print("-" * 32)


class Pieza:

    def __init__(self, color, nombre):
        self.nombre = nombre
        self.posicion = None
        self.Color = color

    def isValid(self, posicion_inicial, posicion_final, Color, tablero):
        if posicion_final in self.movimientos_disponibles(posicion_inicial[0], posicion_inicial[1], tablero,
                                                          Color = Color):
            return True
        return False

    def __repr__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    def movimientos_disponibles(self, x, y, tablero):
        print("ERROR: no hay movimiento posible ")

    def AdNauseum(self, x, y, tablero, Color, intervals):
        """repeats the given interval until another piece is run into.
        if that piece is not of the same color, that square is added and
         then the list is returned"""
        respuestas = []
        for xint, yint in intervals:
            xtemp, ytemp = x + xint, y + yint
            while self.esta_en_limites(xtemp, ytemp):
                # print(str((xtemp,ytemp))+"is in bounds")

                target = tablero.get((xtemp, ytemp), None)
                if target is None:
                    respuestas.append((xtemp, ytemp))
                elif target.Color != Color:
                    respuestas.append((xtemp, ytemp))
                    break
                else:
                    break

                xtemp, ytemp = xtemp + xint, ytemp + yint
        return respuestas

    def esta_en_limites(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        return False

    def no_hay_conflicto(self, tablero, color_inicial, x, y):

        if self.esta_en_limites(x, y) and (((x, y) not in tablero) or tablero[(x, y)].Color != color_inicial):
            return True
        return False


def caballo_lista(x, y, int1, int2):
    return [(x + int1, y + int2), (x - int1, y + int2), (x + int1, y - int2), (x - int1, y - int2),
            (x + int2, y + int1), (x - int2, y + int1), (x + int2, y - int1), (x - int2, y - int1)]


def rey_lista(x, y):
    return [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y), (x - 1, y + 1),
            (x - 1, y - 1)]
