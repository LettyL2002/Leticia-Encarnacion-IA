from pathlib import Path


class Assets(object):
    '''
    Todas las rutas de los assets
    '''

    # * Barrel
    PLAYER_FRENTE: Path = Path("assets/images/player/dragon/mover_frente")
    PLAYER_ESPALDA: Path = Path("assets/images/player/dragon/mover_espalda")
    PLAYER_DERECHA: Path = Path("assets/images/player/dragon/mover_derecha")
    PLAYER_IZQUIERDA: Path = Path(
        "assets/images/player/dragon/mover_izquierda")

    # * Personaje

    PERSONAJE_FRENTE_1: Path = Path(f"{PLAYER_FRENTE}/dragon_frente1.png")
    PERSONAJE_FRENTE_2: Path = Path(f"{PLAYER_FRENTE}/dragon_frente1_1.png")
    PERSONAJE_FRENTE_3: Path = Path(f"{PLAYER_FRENTE}/dragon_frente2.png")
    PERSONAJE_FRENTE_4: Path = Path(f"{PLAYER_FRENTE}/dragon_frente2_1.png")
    PERSONAJE_FRENTE_5: Path = Path(f"{PLAYER_FRENTE}/dragon_frente3.png")
    PERSONAJE_FRENTE_6: Path = Path(f"{PLAYER_FRENTE}/dragon_frente3_1.png")

    PERSONAJE_ATRAS_1: Path = Path(f"{PLAYER_ESPALDA}/dragon_espalda1.png")
    PERSONAJE_ATRAS_2: Path = Path(f"{PLAYER_ESPALDA}/dragon_espalda2.png")
    PERSONAJE_ATRAS_3: Path = Path(f"{PLAYER_ESPALDA}/dragon_espalda3.png")
    PERSONAJE_ATRAS_4: Path = Path(f"{PLAYER_ESPALDA}/dragon_espalda1_1.png")
    PERSONAJE_ATRAS_5: Path = Path(f"{PLAYER_ESPALDA}/dragon_espalda2_1.png")
    PERSONAJE_ATRAS_6: Path = Path(f"{PLAYER_ESPALDA}/dragon_espalda3_1.png")

    PERSONAJE_DERECHA_1: Path = Path(f"{PLAYER_DERECHA}/dragon_derecha1.png")
    PERSONAJE_DERECHA_2: Path = Path(f"{PLAYER_DERECHA}/dragon_derecha2.png")
    PERSONAJE_DERECHA_3: Path = Path(f"{PLAYER_DERECHA}/dragon_derecha3.png")
    PERSONAJE_DERECHA_4: Path = Path(f"{PLAYER_DERECHA}/dragon_derecha1_1.png")
    PERSONAJE_DERECHA_5: Path = Path(f"{PLAYER_DERECHA}/dragon_derecha2_1.png")
    PERSONAJE_DERECHA_6: Path = Path(f"{PLAYER_DERECHA}/dragon_derecha3_1.png")

    PERSONAJE_IZQUIERDA_1: Path = Path(
        f"{PLAYER_IZQUIERDA}/dragon_izquierda1.png")
    PERSONAJE_IZQUIERDA_2: Path = Path(
        f"{PLAYER_IZQUIERDA}/dragon_izquierda2.png")
    PERSONAJE_IZQUIERDA_3: Path = Path(
        f"{PLAYER_IZQUIERDA}/dragon_izquierda3.png")
    PERSONAJE_IZQUIERDA_4: Path = Path(
        f"{PLAYER_IZQUIERDA}/dragon_izquierda1_1.png")
    PERSONAJE_IZQUIERDA_5: Path = Path(
        f"{PLAYER_IZQUIERDA}/dragon_izquierda2_1.png")
    PERSONAJE_IZQUIERDA_6: Path = Path(
        f"{PLAYER_IZQUIERDA}/dragon_izquierda3_1.png")

    # Y asi dependiendo de cuan larga sea la animacion

    # * Enemigos caballero
    ENEMIGO_FRENTE = "assets/images/enemy/caballero/caminar_frente/"
    ENEMIGO_ESPALDA = "assets/images/enemy/caballero/caminar_espalda/"
    ENEMIGO_DER = "assets/images/enemy/caballero/caminar_direccion_derecha/"
    ENEMIGO_IZQ = "assets/images/enemy/caballero/caminar_direccion_izquierda/"

    ENEMIGO_FRENTE_1 = f"{ENEMIGO_FRENTE}caminar_frente1.png"
    ENEMIGO_FRENTE_2 = f"{ENEMIGO_FRENTE}caminar_frente2.png"
    ENEMIGO_FRENTE_3 = f"{ENEMIGO_FRENTE}caminar_frente3.png"
    ENEMIGO_FRENTE_4 = f"{ENEMIGO_FRENTE}caminar_frente4.png"
    ENEMIGO_FRENTE_5 = f"{ENEMIGO_FRENTE}caminar_frente5.png"
    ENEMIGO_FRENTE_6 = f"{ENEMIGO_FRENTE}caminar_frente6.png"

    ENEMIGO_ATRAS_1 = f"{ENEMIGO_ESPALDA}caminar_espalda.png"
    ENEMIGO_ATRAS_2 = f"{ENEMIGO_ESPALDA}caminar_espalda1.png"
    ENEMIGO_ATRAS_3 = f"{ENEMIGO_ESPALDA}caminar_espalda2.png"
    ENEMIGO_ATRAS_4 = f"{ENEMIGO_ESPALDA}caminar-espalda3.png"
    ENEMIGO_ATRAS_5 = f"{ENEMIGO_ESPALDA}caminar_espalda5.png"
    ENEMIGO_ATRAS_6 = f"{ENEMIGO_ESPALDA}caminar_espalda6.png"

    ENEMIGO_DERECHA_1 = f"{ENEMIGO_DER}caminar_der1.png"
    ENEMIGO_DERECHA_2 = f"{ENEMIGO_DER}caminar_der2.png"
    ENEMIGO_DERECHA_3 = f"{ENEMIGO_DER}caminar_der3.png"
    ENEMIGO_DERECHA_4 = f"{ENEMIGO_DER}caminar_der4.png"
    ENEMIGO_DERECHA_5 = f"{ENEMIGO_DER}caminar_der5.png"
    ENEMIGO_DERECHA_6 = f"{ENEMIGO_DER}caminar_der6.png"

    ENEMIGO_IZQUIERDA_1 = f"{ENEMIGO_IZQ}caminar_izq1.png"
    ENEMIGO_IZQUIERDA_2 = f"{ENEMIGO_IZQ}caminar_izq2.png"
    ENEMIGO_IZQUIERDA_3 = f"{ENEMIGO_IZQ}caminar_izq3.png"
    ENEMIGO_IZQUIERDA_4 = f"{ENEMIGO_IZQ}caminar_izq4.png"
    ENEMIGO_IZQUIERDA_5 = f"{ENEMIGO_IZQ}caminar_izq5.png"
    ENEMIGO_IZQUIERDA_6 = f"{ENEMIGO_IZQ}caminar_izq6.png"

    # * Enemigo caballero
    ENEMIGO_FRENTE = "assets/images/enemy/enemigo_2/caminar_frente/"
    ENEMIGO_ESPALDA = "assets/images/enemy/enemigo_2/caminar_espalda/"
    ENEMIGO_DERECHA = "assets/images/enemy/enemigo_2/caminar_derecha/"
    ENEMIGO_IZQUIERDA = "assets/images/enemy/enemigo_2/caminar_izquierda/"

    ENEMIGO_FRENTE_1 = f"{ENEMIGO_FRENTE}cab2_caminar_frente1.png"
    ENEMIGO_FRENTE_2 = f"{ENEMIGO_FRENTE}cab2_caminar_frente2.png"
    ENEMIGO_FRENTE_3 = f"{ENEMIGO_FRENTE}cab2_caminar_frente3.png"
    ENEMIGO_FRENTE_4 = f"{ENEMIGO_FRENTE}cab2_caminar_frente4.png"
    ENEMIGO_FRENTE_5 = f"{ENEMIGO_FRENTE}cab2_caminar_frente5.png"
    ENEMIGO_FRENTE_6 = f"{ENEMIGO_FRENTE}cab2_caminar_frente6.png"
    ENEMIGO_FRENTE_7 = f"{ENEMIGO_FRENTE}cab2_caminar_frente7.png"
    ENEMIGO_FRENTE_8 = f"{ENEMIGO_FRENTE}cab2_caminar_frente8.png"

    ENEMIGO_ATRAS_1 = f"{ENEMIGO_ESPALDA}cab2_caminar_espalda1.png"
    ENEMIGO_ATRAS_2 = f"{ENEMIGO_ESPALDA}cab2_caminar_espalda2.png"
    ENEMIGO_ATRAS_3 = f"{ENEMIGO_ESPALDA}cab2_caminar_espalda3.png"
    ENEMIGO_ATRAS_4 = f"{ENEMIGO_ESPALDA}cab2_caminar_espalda4.png"
    ENEMIGO_ATRAS_5 = f"{ENEMIGO_ESPALDA}cab2_caminar_espalda5.png"
    ENEMIGO_ATRAS_6 = f"{ENEMIGO_ESPALDA}cab2_caminar_espalda6.png"
    ENEMIGO_ATRAS_7 = f"{ENEMIGO_ESPALDA}cab2_caminar_espalda7.png"
    ENEMIGO_ATRAS_8 = f"{ENEMIGO_ESPALDA}cab2_caminar_espalda8.png"

    ENEMIGO_DERECHA_1 = f"{ENEMIGO_DERECHA}cab2_caminar_der1.png"
    ENEMIGO_DERECHA_2 = f"{ENEMIGO_DERECHA}cab2_caminar_der2.png"
    ENEMIGO_DERECHA_3 = f"{ENEMIGO_DERECHA}cab2_caminar_der3.png"
    ENEMIGO_DERECHA_4 = f"{ENEMIGO_DERECHA}cab2_caminar_der4.png"
    ENEMIGO_DERECHA_5 = f"{ENEMIGO_DERECHA}cab2_caminar_der5.png"
    ENEMIGO_DERECHA_6 = f"{ENEMIGO_DERECHA}cab2_caminar_der6.png"
    ENEMIGO_DERECHA_7 = f"{ENEMIGO_DERECHA}cab2_caminar_der7.png"
    ENEMIGO_DERECHA_8 = f"{ENEMIGO_DERECHA}cab2_caminar_der8.png"

    ENEMIGO_IZQUIERDA_1 = f"{ENEMIGO_IZQUIERDA}cab2_caminar_izq1.png"
    ENEMIGO_IZQUIERDA_2 = f"{ENEMIGO_IZQUIERDA}cab2_caminar_izq2.png"
    ENEMIGO_IZQUIERDA_3 = f"{ENEMIGO_IZQUIERDA}cab2_caminar_izq3.png"
    ENEMIGO_IZQUIERDA_4 = f"{ENEMIGO_IZQUIERDA}cab2_caminar_izq4.png"
    ENEMIGO_IZQUIERDA_5 = f"{ENEMIGO_IZQUIERDA}cab2_caminar_izq5.png"
    ENEMIGO_IZQUIERDA_6 = f"{ENEMIGO_IZQUIERDA}cab2_caminar_izq6.png"

    # * Bloques

    TILE_MADERA: Path = Path(
        "assets/images/bloque_madera/Caja_madera.png")
    TILE_PIEDRA: Path = Path(
        "assets/images/bloque_piedra/bloque_piedra.png")

    # * Fondo Mapa
    FONDO_MAPA: Path = Path("assets/images/background/fondo_imagen.png")

    # * Bomba

    BOMBA = "assets/images/bomb/"

    BOMBA = f"{BOMBA}fire_principal.png"

    EXPLOSION = "assets/images/bomb/"

    EXPLOSION_1 = f"{EXPLOSION}fire2.png"
    EXPLOSION_2 = f"{EXPLOSION}fire3.png"
    EXPLOSION_3 = f"{EXPLOSION}fire4.png"
    EXPLOSION_4 = f"{EXPLOSION}fire5.png"
    EXPLOSION_5 = f"{EXPLOSION}fire6.png"
    EXPLOSION_6 = f"{EXPLOSION}fire7.png"
    EXPLOSION_7 = f"{EXPLOSION}fire8.png"

    # * fin juego

    FIN_JUEGO = "assets/images/fin de juego/fin_juego.png"

    FIN_JUEGO = f"{FIN_JUEGO}fin_juego.png"
