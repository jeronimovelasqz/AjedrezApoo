from Clase_pieza import Pieza



class Rey(Pieza):

    def __init__(self, negro):

        Pieza.__init__(self, negro)

        self.en_jaque = False
        if self.negro:
            self.simbolo = "♚"

        else:
            self.simbolo = "♔"

    def verificar_jaque(self, columna_rey, fila_rey, estructura_tablero):
        rey_en_jaque = False

        for columna, lista_de_piezas in enumerate(estructura_tablero):
            for fila in range(len(lista_de_piezas)):
                if estructura_tablero[columna][fila].negro != self.negro:
                    rey_en_jaque = estructura_tablero[columna][fila].validar_movimiento(columna, fila, columna_rey,
                                                                                        fila_rey, estructura_tablero)
                    if rey_en_jaque:
                        return rey_en_jaque

        return rey_en_jaque

    def validar_movimiento(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila, estructura_tablero):
        jaque_final_valido = False

        if estructura_tablero[ultima_columna][ultima_fila].negro == self.negro:
            return jaque_final_valido

        if abs(ultima_fila - fila_inicial) == 1:
            if abs(ultima_columna - columna_inicial) in [0, 1]:
                jaque_final_valido = True

        elif abs(ultima_columna - columna_inicial) == 1:
            if abs(ultima_fila - fila_inicial) in [0, 1]:
                jaque_final_valido = True

        return jaque_final_valido
