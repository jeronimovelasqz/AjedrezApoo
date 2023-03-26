from Posicion import Posicion

"""from Clase_rey import Rey
from Clase_caballo import Caballo
from Clase_torre import Torre
from Clase_reina import Reina
from Clase_alfil import Alfil
from Clase_peon import Peon
"""


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
                self.espacio_en_array = tuple(self.espacio_en_array)


            def obtener_indices(self, posn):


