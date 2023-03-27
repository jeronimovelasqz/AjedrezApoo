from Clase_pieza import Pieza


class Caballo(Pieza):

    def __init__(self, negro):
        Pieza.__init__(self, negro)
        if self.negro:
            self.simbolo = "♞"

        else:
            self.simbolo = "♘"

    def validar_movimiento(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila, estructura_tablero):

        if abs(columna_inicial - ultima_columna) == 1 and abs(fila_inicial - ultima_fila) == 2:
            if estructura_tablero[columna_inicial][fila_inicial].negro != estructura_tablero[ultima_columna][ultima_fila].negro:
                return True

        if abs(columna_inicial - ultima_columna) == 2 and abs(fila_inicial - ultima_fila) == 1:
            if estructura_tablero[columna_inicial][fila_inicial].negro != estructura_tablero[ultima_columna][ultima_fila].negro:
                return True
        return False