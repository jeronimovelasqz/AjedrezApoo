class Alfil(Pieza):

    def __init__(self, negro):
        Pieza.__init__(self.negro)
        if self.negro:
            self.simbolo = "simbolo"

        else:
            self.simbolo = "simbolo"

    def validar_movimiento(self, columna_incial, fila_inicial, ultima_columna, ultima_fila, estructura_tablero):
        jaque_final_valido = False

        if columna_incial == ultima_columna and fila_inicial == ultima_fila:
            return jaque_final_valido

        if Pieza.movimiento_en_diagonal(self, columna_incial, fila_inicial, ultima_columna, ultima_fila,
                                        estructura_tablero):
            return True

        return jaque_final_valido
