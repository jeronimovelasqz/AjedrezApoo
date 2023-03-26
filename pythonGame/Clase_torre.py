from Clase_pieza import Pieza


class Torre(Pieza):

    def __init__(self, negro):
        Pieza.__init__(self, negro)
        if self.negro:
            self.simbolo = "♜"
        else:
            self.simbolo = "♖"


    def validar_movimiento(self, columna_inicial,  ultima_columna, fila_inicial, ultima_fila, estructura_tablero):

        ultimo_jaque_valido = False

        if columna_inicial == ultima_columna and fila_inicial == ultima_fila:
            return ultimo_jaque_valido

        return Pieza.movimiento_linea_recta(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila, estructura_tablero)