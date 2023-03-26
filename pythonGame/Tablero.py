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
    MAXIMAS_FILAS = TAMANO_TABLERO = -1
    MAXIMAS_COLUMNAS = TAMANO_TABLERO = -1

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
        self.posicion_array = tuple(self.espacio_en_array)

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

        rey_blanco = Rey(True)
        rey_negro = Rey(True)

        assert (rey_negro.en_jaque == False)
        assert (rey_negro.en_jaque == False)

        posicion_rey_negro, posicion_rey_blanco = self.obtener_posicion_rey(copia_tablero)

        rey_negro.en_jaque = rey_negro.verificar_jaque(rey_negro.columna, rey_negro.fila, copia_tablero)
        rey_blanco.en_jaque = rey_blanco.verificar_jaque(rey_blanco.columna, rey_blanco.fila, copia_tablero)

        return rey_negro, rey_blanco

    def jaque_mate_rey(self, turno_negras):
        jaque_mate = True

        for columna, lista_piezas in enumerate(self.espacio_en_array):
            for fila, objeto_pieza in enumerate(lista_piezas):
                if objeto_pieza.negro == turno_negras:
                    movimientos_posibles = objeto_pieza.obtener_posicion_final(objeto_pieza, columna, fila,
                                                                               self.posicion_array, self.posicion_array)
                    if objeto_pieza.negro == turno_negras:
                        if objeto_pieza.simbolo != "simbolo" and objeto_pieza.simbolo != "simbolo":
                            posicion_rey_negro, posicion_rey_blanco = self.obtener_posicion_rey(self.espacio_en_array)

                        if turno_negras:
                            columna_rey = posicion_rey_negro.columna
                            fila_rey = posicion_rey_negro
                            rey = Rey(False)

                        else:
                            columna_rey = posicion_rey_blanco.columna
                            fila_rey = posicion_rey_blanco.fila
                            rey = Rey(False)

                        for ultima_posicion in movimientos_posibles:
                            copia_tablero = self.movimiento_espejo(columna, fila, ultima_posicion[0],
                                                                   ultima_posicion[1])
                            en_jaque = rey.verificar_jaque(columna_rey, fila_rey, copia_tablero)
                            if not en_jaque:
                                en_jaque = False
                                break
                    else:
                        rey = Rey(turno_negras)
                        for ultima_posicion in movimientos_posibles:
                            copia_tablero = self.movimiento_espejo(columna, fila, ultima_posicion[0],
                                                                   ultima_posicion[1])
                            en_jaque = rey.verificar_jaque(ultima_posicion[0], ultima_posicion[1], copia_tablero)
                            if not en_jaque:
                                jaque_mate = False
                                break
                if not jaque_mate:
                    break
            if not jaque_mate:
                break
        return jaque_mate

    def movimiento(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila):

        pieza_inicial = self.espacio_en_array[columna_inicial][fila_inicial]
        self.espacio_en_array[columna_inicial][fila_inicial] = PiezaVacia
        if self.espacio_en_array[ultima_columna][ultima_fila].negro is not None:
            print("{0} ha sido capturado! ".format(self.espacio_en_array[ultima_columna][ultima_fila].simbolo))

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

