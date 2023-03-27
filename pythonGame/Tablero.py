from Posicion import Posicion
from pythonGame.Pieza_vacia import PiezaVacia
import copy
from Clase_rey import Rey
from Clase_caballo import Caballo
from Clase_torre import Torre
from Clase_reina import Reina
from Clase_alfil import Alfil
from Clase_peon import Peon


class Tablero:
    columnas = 'abcdefgh'
    filas = '12345678'
    TAMANO_TABLERO = 8
    MAXIMAS_FILAS = TAMANO_TABLERO - 1
    MAXIMAS_COLUMNAS = TAMANO_TABLERO - 1

    def __init__(self):

        self.posicion_array = []
        self.espacio_en_diccionario = {}
        self.espacio_en_array = []
        self.espacio_en_lista = []

        for filas in range(self.TAMANO_TABLERO):
            for columna in range(self.TAMANO_TABLERO):
                self.espacio_en_lista.append(self.columnas[columna] + self.filas[filas])
        self.espacio_en_lista = tuple(self.espacio_en_lista)

        x = 0
        y = 0

        for espacio in self.espacio_en_lista:
            self.espacio_en_diccionario[espacio] = Posicion(x, y)
            x += 1
            if x > self.MAXIMAS_COLUMNAS:
                x = 0
                y += 1

        for columna in range(self.TAMANO_TABLERO):
            fila_lista = []
            for filas in range(self.TAMANO_TABLERO):
                fila_lista.append(None)
            self.espacio_en_array.append(fila_lista)

        for posn in self.espacio_en_lista:
            test_posn = self.obtener_indices(posn)
            self.posicion_array.append(test_posn)
        self.posicion_array = tuple(self.posicion_array)

    def obtener_indices(self, posn):

        columna = self.espacio_en_diccionario[posn].columna
        fila = self.espacio_en_diccionario[posn].fila
        return columna, fila

    def validar_movimiento(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila):

        posicion_inicial = self.espacio_en_array[columna_inicial][fila_inicial]
        if posicion_inicial == PiezaVacia():
            return False

        jaque_final_valido = posicion_inicial.validar_movimiento(columna_inicial, fila_inicial, ultima_columna,
                                                                 ultima_fila, self.espacio_en_array)
        return jaque_final_valido

    def obtener_posicion_rey(self, estructura_tablero):

        encontro_rey_negro = False
        encontro_rey_blanco = False
        for columna, lista_columna in enumerate(estructura_tablero):
            for fila in range(len(lista_columna)):

                if estructura_tablero[columna][fila].simbolo =="♚K":
                    encontro_rey_negro = True
                    posicion_rey_negro = Posicion(columna, fila)

                elif estructura_tablero[columna][fila].simbolo == "♔K":
                    encontro_rey_blanco = True
                    posicion_rey_blanco = Posicion(columna, fila)

            if encontro_rey_negro and encontro_rey_blanco:
                break

        return posicion_rey_negro, posicion_rey_blanco

    def jaque_reyes(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila):

        copia_tablero = self.movimiento_espejo(columna_inicial, fila_inicial, ultima_columna, ultima_fila)

        rey_negro = Rey(True)
        rey_blanco = Rey(False)
        assert (rey_blanco.en_jaque == False)
        assert (rey_negro.en_jaque == False)

        posicion_rey_negro, posicion_rey_blanco = self.obtener_posicion_rey(copia_tablero)

        rey_negro.en_jaque = rey_negro.verificar_jaque(posicion_rey_negro.columna, posicion_rey_negro.fila,
                                                       copia_tablero)
        rey_blanco.en_jaque = rey_blanco.verificar_jaque(posicion_rey_blanco.columna, posicion_rey_blanco.fila,
                                                         copia_tablero)

        return rey_negro, rey_blanco

    def jaque_mate_rey(self, turno_negras):

        jaque_mate = True

        for columna, lista_pieza in enumerate(self.espacio_en_array):
            for fila, objeto_pieza in enumerate(lista_pieza):

                if objeto_pieza.negro == turno_negras:

                    movimientos_posible = objeto_pieza.obtener_posicion_final(objeto_pieza, columna, fila,
                                                                              self.posicion_array,
                                                                              self.espacio_en_array)

                    if objeto_pieza.simbolo != 'bK' and objeto_pieza.simbolo != 'wK':
                        posicion_rey_negro, posicion_rey_blanco = self.obtener_posicion_rey(self.espacio_en_array)

                        if turno_negras:
                            king_column = posicion_rey_negro.columna
                            king_row = posicion_rey_negro.fila
                            rey = Rey(True)

                        else:
                            king_column = posicion_rey_blanco.columna
                            king_row = posicion_rey_blanco.fila
                            rey = Rey(False)

                        for ultima_posicion in movimientos_posible:
                            board_copy = self.movimiento_espejo(columna, fila, ultima_posicion[0], ultima_posicion[1])
                            in_check = rey.verificar_jaque(king_column, king_row, board_copy)
                            if not in_check:
                                jaque_mate = False
                                break

                    else:
                        rey = Rey(turno_negras)

                        for ultima_posicion in movimientos_posible:
                            board_copy = self.movimiento_espejo(columna, fila, ultima_posicion[0], ultima_posicion[1])
                            in_check = rey.verificar_jaque(ultima_posicion[0], ultima_posicion[1], board_copy)
                            if not in_check:
                                jaque_mate = False
                                break
                if not jaque_mate:
                    break
            if not jaque_mate:
                break
        return jaque_mate

    def movimiento(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila):

        starting_piece = self.espacio_en_array[columna_inicial][fila_inicial]
        self.espacio_en_array[columna_inicial][fila_inicial] = PiezaVacia()

        if self.espacio_en_array[ultima_columna][ultima_fila].negro is not None:
            print("{0} ha sido capturado!".format(self.espacio_en_array[ultima_columna][ultima_fila].simbolo))
        self.espacio_en_array[ultima_columna][ultima_fila] = starting_piece

    def movimiento_espejo(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila):

        copia_tablero = copy.deepcopy(self.espacio_en_array)
        starting_piece = copia_tablero[columna_inicial][fila_inicial]
        copia_tablero[columna_inicial][fila_inicial] = PiezaVacia()
        copia_tablero[ultima_columna][ultima_fila] = starting_piece
        return copia_tablero

    def visualizacion_tablero(self):
        print("\n")
        print("   ", end="")
        for i in range(self.TAMANO_TABLERO):
            print(self.columnas[i].center(5), end=" ")

        print("\n" + "  " + "_" * (8 * 6))
        print("  " + "|     " * 8 + "|")

        for i in range(self.TAMANO_TABLERO):
            print(self.filas[-(i + 1)], end=" ")

            for j in range(self.TAMANO_TABLERO):
                print("| " + self.espacio_en_array[j][-(i - self.MAXIMAS_FILAS)].simbolo + "  ", end='')

            print("| " + self.filas[-(i + 1)] + "\n" + "  ", end="")

            for k in range(self.TAMANO_TABLERO):
                if i < 7:
                    print("|" + "_" * 5, end="")
                else:
                    print("|" + "_" * 5, end="")

            print("|" + "\n", end="")

        print("   ", end="")
        for i in range(self.TAMANO_TABLERO):
            print(self.columnas[i].center(5), end=" ")
        print("")

    def __str__(self):
        '''Returns a string and defines print() pertaining to printing out the chessboard.'''
        #Print out column letters:
        graphic = ''
        graphic += "\n"
        graphic += "   "
        for i in range(self.TAMANO_TABLERO):
            graphic += self.columnas[i].center(7) + ' '

        # Print out line at top.
        graphic += "\n" + "  _" + "_" * (8 * 8) + '\n'
        # print("  " + "|       " * 8 + "|")     # Enable this line to add one more empty space line at the top

        # Print out row number. self.rows is printed out starting from the end, hence rows[-(i+1)]
        for i in range(self.TAMANO_TABLERO):
            graphic += self.filas[-(i + 1)] + ' '

            # Print out each space. Print the row numbers again after 8 spaces.
            # Print the symbols for each pieces. Printing starts at top, Positions(0,7) thru (7,7), and ends at bottom, Position(0,0) thru (7,0).
            for j in range(self.TAMANO_TABLERO):
                graphic += "|  " + self.espacio_en_array[j][-(i - self.MAXIMAS_FILAS)].simbolo + "   "

            # Print out the row number again at the end of the line.
            graphic += "| "  + "\n" + "  "

            # Print out the horizontal lines between rows.
            for k in range(self.TAMANO_TABLERO):
                if i < 7:
                    # can possibly change underscore "_" to "-" here:
                    graphic += "|" + "_" * 7
                else:
                    graphic += "|" + "_" * 7

            # Print the right end of the board. Go to the next line.
            graphic += "|" + "\n"

        #Print out column letters again:
        graphic += "   "
        for i in range(self.TAMANO_TABLERO):
            graphic += self.columnas[i].center(7) + ' '
        graphic += "\n"
        return graphic


    def tablero_init(self):

        for columna in range(self.TAMANO_TABLERO):
            for fila in range(self.TAMANO_TABLERO):
                self.espacio_en_array[columna][fila] = None

        # Initialize piece locations.
        self.espacio_en_array[0][7] = Torre(True)  # a8
        self.espacio_en_array[7][7] = Torre(True)  # h8
        self.espacio_en_array[0][0] = Torre(False)  # a1
        self.espacio_en_array[7][0] = Torre(False)  # h1
        self.espacio_en_array[4][7] = Rey(True)  # e8
        self.espacio_en_array[4][0] = Rey(False)  # e1
        self.espacio_en_array[3][7] = Reina(True)  # d8
        self.espacio_en_array[3][0] = Reina(False)  # d1
        self.espacio_en_array[1][7] = Caballo(True)  # b8
        self.espacio_en_array[6][7] = Caballo(True)  # g8
        self.espacio_en_array[1][0] = Caballo(False)  # b1
        self.espacio_en_array[6][0] = Caballo(False)  # g1
        self.espacio_en_array[2][7] = Alfil(True)  # c8
        self.espacio_en_array[5][7] = Alfil(True)  # f8
        self.espacio_en_array[2][0] = Alfil(False)  # c1
        self.espacio_en_array[5][0] = Alfil(False)  # f1

        for i in range(self.TAMANO_TABLERO):
            self.espacio_en_array[i][6] = Peon(True)

        for j in range(self.TAMANO_TABLERO):
            self.espacio_en_array[j][1] = Peon(False)

        for i in range(len(self.espacio_en_array)):
            for j in range(len(self.espacio_en_array[i])):
                if self.espacio_en_array[i][j] is None:
                    self.espacio_en_array[i][j] = PiezaVacia()

    def referencias_espacios_vacios(self):

        impresor_contador = 0

        referencia_de_espacio_en_lista = []
        for i in range(8, 0, -1):
            for j in range(8):
                referencia_de_espacio_en_lista.append(self.columnas[j] + str(i))

        for espacio in referencia_de_espacio_en_lista:
            impresor_contador += 1
            print("{0} == {1}".format(espacio, self.espacio_en_diccionario[espacio]), end='    ')

            if impresor_contador > 7:
                print("\n")
                impresor_contador = 0

    def test_init(self):

        for columna in range(self.TAMANO_TABLERO):
            for fila in range(self.TAMANO_TABLERO):
                self.espacio_en_array[columna][fila] = None

        self.espacio_en_array[3][6] = Torre(True)
        self.espacio_en_array[0][7] = Torre(False)
        self.espacio_en_array[0][5] = Torre(False)
        self.espacio_en_array[7][0] = Torre(False)
        self.espacio_en_array[4][7] = Rey(True)
        self.espacio_en_array[4][0] = Rey(False)
        self.espacio_en_array[3][7] = Reina(True)  # d8
        self.espacio_en_array[3][0] = Reina(False)  # d1

        for j in range(self.TAMANO_TABLERO):
            self.espacio_en_array[j][1] = Peon(False)

        for i in range(len(self.espacio_en_array)):
            for j in range(len(self.espacio_en_array[i])):
                if self.espacio_en_array[i][j] is None:
                    self.espacio_en_array[i][j] = PiezaVacia()


prueba = Tablero()
# print(prueba.visualizacion_tablero())
# print(prueba.referencias_espacios_vacios())
# print(prueba.test_init())
#print(prueba.__str__())
