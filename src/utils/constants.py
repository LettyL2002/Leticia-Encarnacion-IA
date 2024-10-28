import pygame as pg


class Constants (object):
    '''
    Todas las constantes utilizadas en el juego
    '''

    # * Pantalla Menu Principal
    ANCHO_MENU = 800
    ALTO_MENU = 600

    # *  Colores ---> Hexadecimales | RGB
    FONDO = '#000000'  # Sujeto a cambios
    COLOR_PRINCIPAL = '#FFFFFF'  # Sujeto a cambios
    COLOR_SECUNDARIO = '#000000'  # Sujeto a cambios
    COLOR_ACCENTO = '#FF0000'  # Sujeto a cambios

    # future COLORES RGB -- > #? Agrega mas colores si es necesario
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # *  Bloques colores
    BLOQUE_NORMAL = '#FFFFFF'  # Sujeto a cambios
    BLOQUE_INDESTRUCTIBLE = '#000000'  # Sujeto a cambios
    BLOQUE_POR_DESTRUIR = '#FF0000'  # Sujeto a cambios

    # * Fuentes
    pg.font.init()
    FUENTE_PRINCIPAL_MENU = pg.font.Font(None, 74)
    FUENTE_SECUNDARIA = ""
    FUENTE_PEQUENA_MENU = pg.font.Font(None, 36)


class Assets:
    '''
    Todas las rutas de los assets
    '''

    # * Personaje

    PERSONAJE_FRENTE = ""
    PERSONAJE_ATRAS = ""
    PERSONAJE_DERECHA = ""
    PERSONAJE_IZQUIERDA = ""

    # * Animacion Personaje

    PERSONAJE_CAMINANDO1 = ""
    PERSONAJE_CAMINANDO2 = ""
    PERSONAJE_CAMINANDO3 = ""
    # Y asi dependiendo de cuan larga sea la animacion

    # * Enemigos

    ENEMIGO_FRENTE = ""
    ENEMIGO_ATRAS = ""
    ENEMIGO_DERECHA = ""
    ENEMIGO_IZQUIERDA = ""

    # * Animacion Enemigos

    ENEMIGO_CAMINANDO1 = ""
    ENEMIGO_CAMINANDO2 = ""
    ENEMIGO_CAMINANDO3 = ""
    # Y asi dependiendo de cuan larga sea la animacion

    # * Objetos

    BOMBA = ""
    EXPLOSION = ""
