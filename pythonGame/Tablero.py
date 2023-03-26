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
        pass


    def jaque_reyes(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila):
        pass


    def jaque_mate_reyes(self, turno_negras):
        pass



    def movimiento_espejo(self):
        pass



    def visualizacion_tablero(self):
        pass

