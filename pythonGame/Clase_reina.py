from Clase_pieza import Pieza


class Reina(Pieza):
    def __init__(self, negro):
        Pieza.__init__(self, negro)

        if self.negro:
            self.simbolo = "♛Q"
        else:
            self.simbolo = "♕Q"

    def validar_movimiento(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila, estructura_tablero):

        jaque_final_valido = False

        if columna_inicial == ultima_columna and fila_inicial == ultima_fila:
            return jaque_final_valido

        if Pieza.movimiento_linea_recta(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila, estructura_tablero):
            return jaque_final_valido

        if Pieza.movimiento_diagonal(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila, estructura_tablero):
            return True

        if Pieza.movimiento_diagonal(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila, estructura_tablero):
            return True

        return jaque_final_valido