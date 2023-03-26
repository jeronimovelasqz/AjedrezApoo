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

        for fila in range(self.TAMANO_TABLERO):
            for columna in range(self.TAMANO_TABLERO):
                self.espacio_en_lista.append(self.columnas[columna] + self.filas[fila])
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
            for fila in range(self.TAMANO_TABLERO):
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
        pieza_inicial = self.espacio_en_array[columna_inicial][fila_inicial]
        if pieza_inicial == PiezaVacia():
            return False

        ultimo_jaque_valido = pieza_inicial.validar_movimiento(columna_inicial, fila_inicial, ultima_columna,
                                                               ultima_fila, self.espacio_en_array)
        return ultimo_jaque_valido

    def obtener_posicion_rey(self, estructura_tablero):
        encontro_rey_negro = False
        encontro_rey_blanco = False

        for columna, lista_columna in enumerate(estructura_tablero):
            for fila in range(len(lista_columna)):
                if estructura_tablero[columna][fila].simbolo == "simbolo":
                    encontro_rey_negro = True
                    posicion_rey_negro = Posicion(columna, fila)
                elif estructura_tablero[columna][fila].simbolo == "simbolo":
                    encontro_rey_blanco = True
                    posicion_rey_blanco = Posicion(columna, fila)
            if encontro_rey_blanco and encontro_rey_negro:
                break

        return posicion_rey_negro, posicion_rey_blanco

    def jaque_reyes(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila):
        copia_tablero = self.movimiento_espejo(columna_inicial, fila_inicial, ultima_columna, ultima_fila)

        rey_negro = Rey(True)
        rey_blanco = Rey(True)

        assert (rey_blanco.en_jaque == False)
        assert (rey_negro.en_jaque == False)

        posicion_rey_negro, posicion_rey_blanco = self.obtener_posicion_rey(copia_tablero)

        rey_negro.en_jaque = rey_negro.verificar_jaque(rey_negro.columna, rey_negro.fila, copia_tablero)
        rey_blanco.en_jaque = rey_blanco.verificar_jaque(rey_blanco.columna, rey_blanco.fila, copia_tablero)

        return rey_negro, rey_blanco

    def jaque_mate_rey(self, turno_negras):

        jaque_mate = True

        for columna, lista_pieza in enumerate(self.espacio_en_array):
            for fila, objeto_pieza in enumerate(lista_pieza):

                if objeto_pieza.negro == turno_negras:

                    movimientos_posibles = objeto_pieza.obtener_posicion_final(objeto_pieza, columna, fila,
                                                                               self.posicion_array,
                                                                               self.espacio_en_array)

                    if objeto_pieza.simbolo != 'simbolo' and objeto_pieza.simbolo != 'simbolo':
                        posicion_rey_negro, posicion_rey_blanco = self.get_king_locations(self.espacio_en_array)
                        if turno_negras:
                            columna_rey = posicion_rey_negro.columna
                            fila_rey = posicion_rey_negro.fila
                            rey = Rey(True)
                        else:
                            columna_rey = posicion_rey_blanco.columna
                            fila_rey = posicion_rey_blanco.fila
                            rey = Rey(False)
                        for posicion_final in movimientos_posibles:
                            copia_tablero = self.movimiento_espejo(columna, fila, posicion_final[0], posicion_final[1])
                            in_check = Rey.verificar_jaque(columna_rey, fila_rey, copia_tablero, copia_tablero)
                            if not in_check:
                                jaque_mate = False
                                break

                    else:
                        rey = Rey(turno_negras)
                        for posicion_final in movimientos_posibles:
                            copia_tablero = self.movimiento_espejo(columna, fila, posicion_final[0], posicion_final[1])
                            in_check = rey.verificar_jaque(posicion_final[0], posicion_final[1], copia_tablero)
                            if not in_check:
                                jaque_mate = False
                                break
                if not jaque_mate:
                    break
            if not jaque_mate:
                break
        return jaque_mate

    def movimiento(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila):

        pieza_inicial = self.espacio_en_array[columna_inicial][fila_inicial]
        self.espacio_en_array[columna_inicial][fila_inicial] = PiezaVacia()
        if self.espacio_en_array[ultima_columna][ultima_fila].negro is not None:
            print("{0} ha sido capturado! ".format(self.espacio_en_array[ultima_columna][ultima_fila].simbolo))
        self.espacio_en_array[ultima_columna][ultima_fila] = pieza_inicial

    def movimiento_espejo(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila):

        copia_tablero = copy.deepcopy(self.espacio_en_array)
        pieza_inicial = copia_tablero[columna_inicial][fila_inicial]
        copia_tablero[columna_inicial][fila_inicial] = PiezaVacia()
        copia_tablero[ultima_columna][ultima_fila] = pieza_inicial
        return copia_tablero

    def visualizacion_tablero(self):
        print("\n")
        print("   ", end="")
        for i in range(self.TAMANO_TABLERO):
            print(self.columnas[i].center(7), end=" ")

        print("\n" + " ho" + "_" * (8 * 8))
        print("  " + "|       " * 8 + "|")

        for i in range(self.TAMANO_TABLERO):
            print(self.filas[-(i + 1)], end=" ")

            for j in range(self.TAMANO_TABLERO):
                print("|  " + self.espacio_en_array[j][-(i - self.MAXIMAS_FILAS)].simbolo + "   ", end='')

            print("| " + self.filas[-(i + 1)] + "\n" + "  ", end="")

            for k in range(self.TAMANO_TABLERO):
                if i < 7:

                    print("|" + "_" * 7, end="")
                else:
                    print("|" + "_" * 7, end="")

            print("|" + "\n", end="")

        print("   ", end="")
        for i in range(self.TAMANO_TABLERO):
            print(self.columnas[i].center(7), end=" ")
        print("")

    def __str__(self):
        grafico = ''
        grafico += "\n"
        grafico += "   "

        for i in range(self.TAMANO_TABLERO):
            grafico += self.columnas[i].center(7) + ' '

        grafico += "\n" + "  _" + "_" * (8 * 8) + '\n'

        for i in range(self.TAMANO_TABLERO):
            grafico += self.filas[-(i + 1)] + ' '

            for j in range(self.TAMANO_TABLERO):
                grafico += "| " + self.filas[-(i + 1)] + "\n" + "  "

            for k in range(self.TAMANO_TABLERO):
                if i < 7:
                    grafico += "|" + "_" * 7
                else:
                    grafico += "|" + "_" * 7

            grafico += "|" + "\n"

        grafico += "  "
        for i in range(self.TAMANO_TABLERO):
            grafico += self.columnas[i].center(7) + ' '
        grafico += "\n"
        return grafico

    def inicializador_tablero(self):

        for columna in range(self.TAMANO_TABLERO):
            for fila in range(self.TAMANO_TABLERO):
                self.espacio_en_array[columna][fila] = None

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

        # black pawns, a7 through h7:
        for i in range(self.TAMANO_TABLERO):
            self.espacio_en_array[i][6] = Peon(True)
        # white pawns, a2 through h2:
        for j in range(self.TAMANO_TABLERO):
            self.espacio_en_array[j][1] = Peon(False)

        # Finally, set empty spaces to contain NullPiece()s
        for i in range(len(self.espacio_en_array)):
            for j in range(len(self.espacio_en_array[i])):
                if self.espacio_en_array[i][j] is None:
                    self.espacio_en_array[i][j] = PiezaVacia()

    def space_points_ref(self):

        contador_impresiones_consola = 0

        espacios_vacios_referencias = []
        for i in range(8, 0, -1):
            for j in range(8):
                espacios_vacios_referencias.append(self.columnas[j] + str(i))
        for espacio in espacios_vacios_referencias:
            contador_impresiones_consola += 1
            print("{0} == {1}".format(espacio, self.espacio_en_diccionario[espacio]), end='    ')

            if contador_impresiones_consola > 7:
                print("\n")
                contador_impresiones_consola = 0


prueba = Tablero()
print(prueba.inicializador_tablero())
print(prueba.visualizacion_tablero())
