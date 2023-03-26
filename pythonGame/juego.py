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
            print("{0} el rey esta en jaque.".format(turno.title()))
            game_over = tablero_juego.jaque_mate_rey(turno_negras)

        if game_over:
            print(f"FIN DEL JUEGO, JAQUE MATE! {enemigo.upper()} GANA!")
            break


        posicion_incial = move_input(tablero_juego, "Inicio")
        columna_inicial, fila_inicial = tablero_juego.obtener_indices(posicion_incial)

        if tablero_juego.espacio_en_array[columna_inicial][fila_inicial].negro != turno_negras:
            print(f"movimiento invalido, debe esperar {turno} y mover pieza!")
            continue
        posicion_final = move_input(tablero_juego, "deshacer")
        if posicion_final == 'deshacer':
            continue
        ultima_columna, ultima_fila = tablero_juego.obtener_indices(posicion_final)


        if not tablero_juego.validar_movimiento(columna_inicial, fila_inicial, ultima_columna, ultima_fila):
            print("movimiento invalido!")
            continue


        rey_negro, rey_blanco = tablero_juego.jaque_reyes(columna_inicial, fila_inicial, ultima_columna, ultima_fila)
        if not rey_en_jaque:
            if turno_negras and rey_negro.en_jaque:
                print(f"movimiento invalido!  {turno} el rey seguiria en jaque.")
                continue
            if not turno_negras and rey_blanco.en_jaque:
                print(f"movimiento invalido! {turno} el rey estaria en jaque")
                continue

        else:
            if turno_negras and rey_negro.en_jaque:
                print(f"movimiento invalido! {turno} el rey sigue en jaque.")
                continue
            if not turno_negras and rey_blanco.en_jaque:
                print(f"movimiento invalido! {turno} el rey sigue en jaque.")
                continue


        tablero_juego.movimiento(columna_inicial, fila_inicial, ultima_columna, ultima_fila)


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


def move_input(tablero_juego, inicio_fin):

    while True:
        if inicio_fin == "Deshacer":
            print('Type "Deshacer" para retornar el inicio del turno.')

        ultima_posicion = input(f"{inicio_fin} poosicion? Type \"tablero\" para vizualizar el tablero.\n")
        ultima_posicion = ultima_posicion.lower().strip()

        if ultima_posicion == "tablero":
            print(tablero_juego)
            continue

        if ultima_posicion.lower() == 'Deshacer':
            return ultima_posicion

        elif ultima_posicion in tablero_juego.espacio_en_lista:
            pass

        else:
            print("posicion invalida!")
            continue

        return ultima_posicion


def test():

    tablero_juego = Tablero()
    tablero_juego.test_init()
    turno_negras = False
    rey_en_jaque = False

    print(tablero_juego, '\n\n')
    print("ESPACIO EN ARRAY")

    print(tablero_juego.espacio_en_array, '\n\n')
    print("ESPACIO EN LISTA")

    print(tablero_juego.espacio_en_lista, '\n\n')
    print("ESPACIO EN DICCIONARIO")

    print(tablero_juego.espacio_en_diccionario, "\n\n")
    print("POSICION EN ARRAY")

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
            print("{0} rey en jaque.".format(turno.title()))
            game_over = tablero_juego.jaque_mate_rey(turno_negras)

        if game_over:
            print(f"FIN DEL JUEGO JAQUE MATE! {enemigo.upper()} GANA!")
            break


        posicion_incial = move_input(tablero_juego, "Start")
        columna_incial, fila_inicial = tablero_juego.obtener_indices(posicion_incial)

        if tablero_juego.espacio_en_array[columna_incial][fila_inicial].negro != turno_negras:
            print(f"movimiento invalido , debe escoger {turno} pieza a mover!")
            continue
        posicion_final = move_input(tablero_juego, "final")
        ultima_columna, ultima_fila = tablero_juego.obtener_indices(posicion_final)


        if not tablero_juego.validar_movimiento(columna_incial, fila_inicial, ultima_columna, ultima_fila):
            print("Movimiento invalido!")
            continue


        rey_negro, rey_blanco = tablero_juego.jaque_reyes(columna_incial, fila_inicial, ultima_columna, ultima_fila)

        if not rey_en_jaque:

            if turno_negras and rey_negro.in_check:
                print(f"movimiento invalido {turno} rey estaria en jaque.")
                continue

            if not turno_negras and rey_blanco.in_check:
                print(f"movimiento invalido {turno} rey estaria en jaque.")
                continue
        else:

            if turno_negras and rey_negro.in_check:
                print(f"movimiento invalido {turno} rey sigue en jaque.")
                continue

            if not turno_negras and rey_blanco.in_check:
                print(f"movimiento invalido {turno} rey sigue en jaque.")
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
