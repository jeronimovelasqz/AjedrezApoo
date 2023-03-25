from Clase_pieza import Pieza


class PiezaVacia(Pieza):

    def __init__(self):
        super().__init__()
        self.simbolo = " "
        self.negro = None

    def validar_movimiento(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila, estructura_tablero):
        return False
