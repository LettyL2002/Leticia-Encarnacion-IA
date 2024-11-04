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

    # *  Bloques
    TILE_SIZE = 50  # Tamaño de cada bloque en la grilla
    GRID_WIDTH = 16  # Número de bloques en horizontal
    GRID_HEIGHT = 12  # Número de bloques en vertical
    WINDOW_WIDTH = GRID_WIDTH * TILE_SIZE
    WINDOW_HEIGHT = GRID_HEIGHT * TILE_SIZE


class Assets(object):
    '''
    Todas las rutas de los assets
    ''' 

    # * Barrel
    PLAYER_FRENTE = "assets/images/player/dragon/mover frente/"
    PLAYER_ESPALDA = "assets/images/player/dragon/mover espalda/"
    PLAYER_DERECHA = "assets/images/player/dragon/mover derecha/"
    PLAYER_IZQUIERDA = "assets/images/player/dragon/mover izquierda/"

    # * Personaje

    PERSONAJE_FRENTE_1 = f"{PLAYER_FRENTE}dragon_frente1.png"
    PERSONAJE_FRENTE_2 = f"{PLAYER_FRENTE}dragon_frente1.1.png"
    PERSONAJE_FRENTE_3 = f"{PLAYER_FRENTE}dragon_frente2.png"
    PERSONAJE_FRENTE_4 = f"{PLAYER_FRENTE}dragon_frente2.1.png"
    PERSONAJE_FRENTE_5 = f"{PLAYER_FRENTE}dragon_frente3.png"
    PERSONAJE_FRENTE_6 = f"{PLAYER_FRENTE}dragon_frente3.1.png"

    PERSONAJE_DERECHA = ""
    PERSONAJE_IZQUIERDA = ""

    # Y asi dependiendo de cuan larga sea la animacion

    # * Enemigos

    ENEMIGO_FRENTE = ""
    ENEMIGO_ATRAS = ""
    ENEMIGO_DERECHA = ""
    ENEMIGO_IZQUIERDA = ""

    # * Bloques

    TILE_MADERA = "\\assets\\images\\bloque_madera\\Caja_madera.png"
    TILE_PIEDRA = "\\assets\\images\\bloque_piedra\\bloque_piedra.png"

    # * Fondo Mapa
    FONDO_MAPA = "\\assets\\images\\background\\fondo.png"

    # * Objetos

    BOMBA = ""
    EXPLOSION = ""
