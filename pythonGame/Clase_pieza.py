from datetime import datetime


class Pieza:
    COLOR_NEGRO = "yellow"
    COLOR_BLANCO = "blue"

    def __init__(self, negro=True):
        self.negro = negro

    def obtener_posicion_final(self, pieza, columna_inicial, fila_inicial, ultima_posicion_array, estructura_tablero):

        movimientos_posibles = []
        for posicion in ultima_posicion_array:
            movimiento_valido = pieza.validar_movimiento(columna_inicial, fila_inicial, posicion[0], posicion[1],
                                                         estructura_tablero)
            if movimiento_valido:
                movimientos_posibles.append(posicion)

        return movimientos_posibles

    def movimiento_linea_recta(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila,
                               estructura_tablero) -> object:
        jaque_final_valido = False

        if columna_inicial == ultima_columna:

            intervalo = int(abs(ultima_fila - fila_inicial) / (ultima_fila - fila_inicial))

            for i in range(fila_inicial + intervalo, ultima_fila, intervalo):
                if estructura_tablero[columna_inicial][i].black is not None:
                    return jaque_final_valido

            if estructura_tablero[ultima_columna][ultima_fila].negro == estructura_tablero[columna_inicial][
                fila_inicial].negro:
                return jaque_final_valido
            jaque_final_valido = True
            return jaque_final_valido

        if fila_inicial == ultima_fila:
            intervalo = int(abs(ultima_columna - ultima_fila) / (ultima_columna - columna_inicial))
            for i in range(columna_inicial + intervalo, ultima_columna, intervalo):
                if estructura_tablero[i][fila_inicial].negro is not None:
                    return jaque_final_valido

            if estructura_tablero[ultima_columna][ultima_fila].negro == estructura_tablero[columna_inicial][
                fila_inicial].negro:
                return jaque_final_valido
            jaque_final_valido = True
            return jaque_final_valido

        return jaque_final_valido

    def movimiento_diagonal(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila, estructura_tablero):
        jaque_final_valido = False

        if columna_inicial == ultima_columna or fila_inicial == ultima_fila:
            return jaque_final_valido

        intervalo_columna = int(abs(ultima_columna - columna_inicial))
        fila_intervalo = int(abs(ultima_fila - fila_inicial))
        if intervalo_columna != fila_intervalo:
            return jaque_final_valido

        fila_negativa = int(abs(ultima_fila - fila_inicial) / (ultima_fila - fila_inicial))
        columna_negativa = int(abs(ultima_columna - columna_inicial) / (ultima_columna - columna_inicial))

        for c in range(fila_inicial + columna_negativa, ultima_columna, columna_negativa):
            for i in range(fila_inicial + fila_negativa, ultima_fila, fila_negativa):
                if estructura_tablero[c][i].negro is not None:
                    return jaque_final_valido

        if estructura_tablero[ultima_columna][ultima_fila].negro == estructura_tablero[columna_inicial][
            fila_inicial].negro:
            return jaque_final_valido

        jaque_final_valido = True
        return jaque_final_valido
