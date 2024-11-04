import pygame as pg


class Constants (object):
    '''
    Todas las constantes utilizadas en el juego
    '''
    # * Pantalla Menu Principal
    ANCHO_MENU = 800
    ALTO_MENU = 600

    # * Pantalla Juego
    ANCHO_JUEGO = 840
    ALTO_JUEGO = 600

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

    # *  Bloques
    TILE_SIZE = 30  # Tamaño de cada bloque en la grilla
    GRID_WIDTH = 28  # Número de bloques en horizontal
    GRID_HEIGHT = 20  # Número de bloques en vertical
    WINDOW_WIDTH = GRID_WIDTH * TILE_SIZE
    WINDOW_HEIGHT = GRID_HEIGHT * TILE_SIZE
