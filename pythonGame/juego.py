from Clase_pieza import Pieza
from Clase_caballo import Caballo
from Clase_torre import Torre
from Clase_alfil import Alfil
from Clase_peon import Peon
from Clase_reina import Reina
from Pieza_vacia import PiezaVacia
from exepciones import MovimientoInvalido
from Posicion import Posicion
from Clase_rey import Rey
from Tablero import Tablero


def main():
    tablero_juego = Tablero()
    tablero_juego.inicializador_tablero()
    turno_negras = False
    rey_en_jaque = False
    game_over = False

    # Game loop:
    while True:
        if not turno_negras:
            turno = "blancas"
            enemigo = "negras"
        else:
            turno = "negras"
            enemigo = "blancas"
        print(tablero_juego)

        if rey_en_jaque:
            print("{0} king is in check.".format(turno.title()))
            game_over = tablero_juego.jaque_mate_rey(turno_negras)

        if game_over:
            print(f"GAME OVER! CHECKMATE! {enemigo.upper()} WINS!")
            break


        posicion_incial = move_input(tablero_juego, "Inicio")
        columna_inicial, fila_inicial = tablero_juego.obtener_indices(posicion_incial)

        if tablero_juego.espacio_en_array[columna_inicial][fila_inicial].negro != turno_negras:
            print(f"Invalid move! You must choose a {turno} piece to move!")
            continue
        posicion_final = move_input(tablero_juego, "End")
        if posicion_final == 'deshacer':
            continue
        ultima_columna, ultima_fila = tablero_juego.obtener_indices(posicion_final)


        if not tablero_juego.validar_movimiento(columna_inicial, fila_inicial, ultima_columna, ultima_fila):
            print("Invalid movement!")
            continue


        rey_negro, rey_blanco = tablero_juego.jaque_reyes(columna_inicial, fila_inicial, ultima_columna, ultima_fila)
        if not rey_en_jaque:
            if turno_negras and rey_negro.en_jaque:
                print(f"Invalid move! Friendly {turno} king would be placed in check.")
                continue
            if not turno_negras and rey_blanco.en_jaque:
                print(f"Invalid move! Friendly {turno} king would be placed in check.")
                continue

        else:
            if turno_negras and rey_negro.en_jaque:
                print(f"Invalid move! Friendly {turno} king is still in check.")
                continue
            if not turno_negras and rey_blanco.en_jaque:
                print(f"Invalid move! Friendly {turno} king is still in check.")
                continue


        tablero_juego.movimiento(columna_inicial, fila_inicial, ultima_columna, ultima_fila)


        if turno_negras and rey_blanco.en_jaque:
            rey_en_jaque = True
        elif not turno_negras and rey_negro.en_jaque:
            rey_en_jaque = True
        else:
            rey_en_jaque = False

        # Finally, switch turns.
        if not turno_negras:
            turno_negras = True
        else:
            turno_negras = False


def move_input(tablero_juego, inicio_fin):

    while True:
        if inicio_fin == "Deshacer":
            print('Type "undo" to return to beginning of turn.')

        ultima_posicion = input(f"{inicio_fin} location? Type \"board\" at any time to view the board.\n")
        ultima_posicion = ultima_posicion.lower().strip()

        if ultima_posicion == "tablero":
            print(tablero_juego)
            continue

        if ultima_posicion.lower() == 'undo':
            return ultima_posicion

        elif ultima_posicion in tablero_juego.espacio_en_lista:
            pass

        else:
            print("Invalid location!")
            continue

        return ultima_posicion


def test():
    '''Prints out board lists and calls board functions for testing.'''
    tablero_juego = Tablero()
    #tablero_juego.test_init()
    turno_negras = False
    rey_en_jaque = False

    print(tablero_juego, '\n\n')
    print("SPACE ARRAY")

    print(tablero_juego.espacio_en_array, '\n\n')
    print("SPACE LIST")

    print(tablero_juego.espacio_en_lista, '\n\n')
    print("SPACE DICT")

    print(tablero_juego.espacio_en_diccionario, "\n\n")
    print("LOCATION ARRAY")

    print(tablero_juego.posicion_array)
    tablero_juego.espacios_vacios_referencia()

    # Game loop:
    while True:

        if not turno_negras:
            turno = "blanco"
            enemigo = "negra"

        else:
            turno = "negra"
            enemigo = "blanco"

        print(tablero_juego)
        game_over = False

        if rey_en_jaque:
            print("{0} king is in check.".format(turno.title()))
            game_over = tablero_juego.jaque_mate_rey(turno_negras)

        if game_over:
            print(f"GAME OVER! CHECKMATE! {enemigo.upper()} WINS!")
            break


        posicion_incial = move_input(tablero_juego, "Start")
        columna_incial, fila_inicial = tablero_juego.obtener_indices(posicion_incial)

        if tablero_juego.espacio_en_array[columna_incial][fila_inicial].negro != turno_negras:
            print(f"Invalid move! You must choose a {turno} piece to move!")
            continue
        end_posn = move_input(tablero_juego, "End")
        ultima_columna, ultima_fila = tablero_juego.obtener_indices(end_posn)


        if not tablero_juego.validar_movimiento(columna_incial, fila_inicial, ultima_columna, ultima_fila):
            print("Invalid movement!")
            continue


        rey_negro, rey_blanco = tablero_juego.jaque_reyes(columna_incial, fila_inicial, ultima_columna, ultima_fila)

        if not rey_en_jaque:

            if turno_negras and rey_negro.in_check:
                print(f"Invalid move! Friendly {turno} king would be placed in check.")
                continue

            if not turno_negras and rey_blanco.in_check:
                print(f"Invalid move! Friendly {turno} king would be placed in check.")
                continue
        else:

            if turno_negras and rey_negro.in_check:
                print(f"Invalid move! Friendly {turno} king is still in check.")
                continue

            if not turno_negras and rey_blanco.in_check:
                print(f"Invalid move! Friendly {turno} king is still in check.")
                continue


        tablero_juego.movimiento(columna_incial, fila_inicial, ultima_columna, ultima_fila)


        if turno_negras and rey_blanco.en_jaque:
            rey_en_jaque = True

        elif not turno_negras and rey_negro.en_jaque:
            rey_en_jaque = True

        else:
            rey_en_jaque = False

        if not turno_negras:
            turno_negras = True

        else:
            turno_negras = False


# test()
main()
