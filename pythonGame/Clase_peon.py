from Clase_pieza import Pieza


class Peon(Pieza):

    def __init__(self, negro):
        Pieza.__init__(self, negro)
        if self.negro:
            self.simbolo = "♟"

        else:
            self.simbolo = "♙"

    def validar_movimiento(self, columna_inicial, fila_inicial, ultima_columna, ultima_fila, estructura_tablero):

        jaque_final_valido = False

        if abs(columna_inicial - ultima_columna) > 1:
            return jaque_final_valido

        if self.negro:

            if ultima_fila >= fila_inicial:
                return jaque_final_valido

            if columna_inicial == ultima_columna:
                if fila_inicial == 6:
                    if ultima_fila == 5:
                        if estructura_tablero[ultima_columna][ultima_fila].negro is None:
                            jaque_final_valido = True
                            return jaque_final_valido

                    if ultima_fila == 4:
                        if estructura_tablero[ultima_columna][ultima_fila].negro is None and \
                                estructura_tablero[ultima_columna][ultima_fila + 1].negro is None:
                            jaque_final_valido = True
                            return jaque_final_valido
                    return jaque_final_valido

                if fila_inicial < 6:
                    if ultima_fila != fila_inicial - 1:
                        return jaque_final_valido
                    if estructura_tablero[ultima_columna][ultima_fila].negro is not None:
                        return jaque_final_valido
                    else:
                        jaque_final_valido = True
                        return jaque_final_valido

            if abs(columna_inicial - ultima_columna) == 1:
                if ultima_fila != fila_inicial - 1:
                    return jaque_final_valido
                if not estructura_tablero[ultima_columna][ultima_fila].negro:
                    jaque_final_valido = True
                    return jaque_final_valido
                else:
                    return jaque_final_valido

        if not self.negro:

            if ultima_fila <= fila_inicial:
                return jaque_final_valido

            if columna_inicial == ultima_columna:
                if fila_inicial == 1:
                    if ultima_fila == 2:
                        if estructura_tablero[ultima_columna][ultima_fila].negro is None:
                            jaque_final_valido = True
                            return jaque_final_valido

                    if ultima_fila == 3:
                        if estructura_tablero[ultima_columna][ultima_fila].negro is None and \
                                estructura_tablero[ultima_columna][ultima_fila - 1].negro is None:
                            jaque_final_valido = True
                            return jaque_final_valido
                    return jaque_final_valido

                if fila_inicial > 1:
                    if ultima_fila != fila_inicial + 1:
                        return jaque_final_valido
                    if estructura_tablero[ultima_columna][ultima_fila].negro is not None:
                        return jaque_final_valido
                    else:
                        jaque_final_valido = True
                        return jaque_final_valido

            if abs(columna_inicial - ultima_columna) == 1:
                if ultima_fila != fila_inicial + 1:
                    return jaque_final_valido
                if estructura_tablero[ultima_columna][ultima_fila].negro:
                    jaque_final_valido = True
                    return jaque_final_valido
                else:
                    return jaque_final_valido
