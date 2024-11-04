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
    
    PERSONAJE_ATRAS_1 = "{PLAYER_ATRAS}dragon_espalda1.png"
    PERSONAJE_ATRAS_1 = "{PLAYER_ATRAS}dragon_espalda2.png"
    PERSONAJE_ATRAS_1 = "{PLAYER_ATRAS}dragon_espalda3.png"
    PERSONAJE_ATRAS_1 = "{PLAYER_ATRAS}dragon_espalda1.1.png"
    PERSONAJE_ATRAS_1 = "{PLAYER_ATRAS}dragon_espalda2.1.png"
    PERSONAJE_ATRAS_1 = "{PLAYER_ATRAS}dragon_espalda3.1.png"

    PERSONAJE_DERECHA_1 = "{PLAYER_DERECHA}dragon_derecha1.png"
    PERSONAJE_DERECHA_2 = "{PLAYER_DERECHA}dragon_derecha2.png"
    PERSONAJE_DERECHA_3 = "{PLAYER_DERECHA}dragon_derecha3.png"
    PERSONAJE_DERECHA_4 = "{PLAYER_DERECHA}dragon_derecha1.1.png"
    PERSONAJE_DERECHA_5 = "{PLAYER_DERECHA}dragon_derecha2.1png"
    PERSONAJE_DERECHA_6 = "{PLAYER_DERECHA}dragon_derecha3.1png"
    
    PERSONAJE_IZQUIERDA_1 = "{PLAYER_IZQUIERDA}dragon_izquierda1.png"
    PERSONAJE_IZQUIERDA_2= "{PLAYER_IZQUIERDA}dragon_izquierda2.png"
    PERSONAJE_IZQUIERDA_3 = "{PLAYER_IZQUIERDA}dragon_izquierda3.png"
    PERSONAJE_IZQUIERDA_4 = "{PLAYER_IZQUIERDA}dragon_izquierda1.1.png"
    PERSONAJE_IZQUIERDA_5 = "{PLAYER_IZQUIERDA}dragon_izquierda2.1.png"
    PERSONAJE_IZQUIERDA_6 = "{PLAYER_IZQUIERDA}dragon_izquierda3.1.png"

    # Y asi dependiendo de cuan larga sea la animacion

    # * Enemigos caballero
    PLAYER_FRENTE = "assets/images/enemy/caballero/caminar frente/"
    PLAYER_ESPALDA = "assets/images/enemy/caballero/caminar espalda/"
    PLAYER_DERECHA = "assets/images/enemy/caballero/caminar direccion derecha/"
    PLAYER_IZQUIERDA = "assets/images/enemy/caballero/caminar direccion izquierda/"

    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}caminar_frente1.png"
    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}caminar_frente2.png"
    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}caminar_frente3.png"
    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}caminar_frente4.png"
    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}caminar_frente5.png"
    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}caminar_frente6.png"
    
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}caminar espalda.png"
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}caminar espalda1.png"
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}caminar espalda2.png"
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}caminar espalda3.png"
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}caminar espalda5.png"
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}caminar espalda6.png"
    
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}caminar_der1.png"
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}caminar_der2.png"
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}caminar_der3.png"
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}caminar_der4.png"
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}caminar_der5.png"
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}caminar_der6.png"
    
    ENEMIGO_IZQUIERDA = "{ENEMIGO_IZQUIERDA}caminar_izq1.png"
    ENEMIGO_IZQUIERDA = "{ENEMIGO_IZQUIERDA}caminar_izq2.png"
    ENEMIGO_IZQUIERDA = "{ENEMIGO_IZQUIERDA}caminar_izq3.png"
    ENEMIGO_IZQUIERDA = "{ENEMIGO_IZQUIERDA}caminar_izq4.png"
    ENEMIGO_IZQUIERDA = "{ENEMIGO_IZQUIERDA}caminar_izq5.png"
    ENEMIGO_IZQUIERDA = "{ENEMIGO_IZQUIERDA}caminar_izq6.png"
 
    # * Enemigo caballero
    PLAYER_FRENTE = "assets/images/enemy/enemigo 2/caminar frente/"
    PLAYER_ESPALDA = "assets/images/enemy/enemigo 2/caminar espalda/"
    PLAYER_DERECHA = "assets/images/enemy/enemigo 2/caminar derecha/"
    PLAYER_IZQUIERDA = "assets/images/enemy/enemigo 2/caminar izquierda/"

    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}cab2_caminar_frente1.png"
    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}cab2_caminar_frente2.png"
    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}cab2_caminar_frente3.png"
    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}cab2_caminar_frente4.png"
    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}cab2_caminar_frente5.png"
    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}cab2_caminar_frente6.png"
    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}cab2_caminar_frente7.png"
    ENEMIGO_FRENTE = "{ENEMIGO_FRENTE}cab2_caminar_frente8.png"
    
    
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}cab2_caminar_espalda1.png"
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}cab2_caminar_espalda2.png"
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}cab2_caminar_espalda3.png"
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}cab2_caminar_espalda4.png"
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}cab2_caminar_espalda5.png"
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}cab2_caminar_espalda6.png"
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}cab2_caminar_espalda7.png"
    ENEMIGO_ATRAS = "{ENEMIGO_ATRAS}cab2_caminar_espalda8.png"
    
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}cab2_caminar_der1.png"
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}cab2_caminar_der2.png"
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}cab2_caminar_der3.png"
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}cab2_caminar_der4.png"
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}cab2_caminar_der5.png"
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}cab2_caminar_der6.png"
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}cab2_caminar_der7.png"
    ENEMIGO_DERECHA = "{ENEMIGO_DERECHA}cab2_caminar_der8.png"
    
    ENEMIGO_IZQUIERDA = "{ENEMIGO_IZQUIERDA}cab2_caminar_izq1.png"
    ENEMIGO_IZQUIERDA = "{ENEMIGO_IZQUIERDA}cab2_caminar_izq2.png"
    ENEMIGO_IZQUIERDA = "{ENEMIGO_IZQUIERDA}cab2_caminar_izq3.png"
    ENEMIGO_IZQUIERDA = "{ENEMIGO_IZQUIERDA}cab2_caminar_izq4.png"
    ENEMIGO_IZQUIERDA = "{ENEMIGO_IZQUIERDA}cab2_caminar_izq5.png"
    ENEMIGO_IZQUIERDA = "{ENEMIGO_IZQUIERDA}cab2_caminar_izq6.png"
    
    # * Bloques

    TILE_MADERA = "\\assets\\images\\bloque_madera\\Caja_madera.png"
    TILE_PIEDRA = "\\assets\\images\\bloque_piedra\\bloque_piedra.png"

    # * Fondo Mapa
    FONDO_MAPA = "\\assets\\images\\background\\fondo.png"


 # * Bomba
 
BOMBA  = "assets/images/bomb/"

BOMBA = "{BOMBA}fire_principal.png"

EXPLOSION = "assets/images/bomb/"

EXPLOSION = "{EXPLOSION}fire2.png" 
EXPLOSION = "{EXPLOSION}fire3.png" 
EXPLOSION = "{EXPLOSION}fire4.png" 
EXPLOSION = "{EXPLOSION}fire5.png" 
EXPLOSION = "{EXPLOSION}fire6.png" 
EXPLOSION = "{EXPLOSION}fire7.png" 
EXPLOSION = "{EXPLOSION}fire8.png" 

# * fin juego

FIN_JUEGO = "assets/images/fin de juego/fin_juego.png"