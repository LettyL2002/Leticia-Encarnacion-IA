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

    # * Enemigo caballero 1 Barrer
    ENEMIGO_FRENTE: Path = Path("assets/images/enemy/caballero/caminar_frente")
    ENEMIGO_ESPALDA: Path = Path(
        "assets/images/enemy/caballero/caminar_espalda")
    ENEMIGO_DER: Path = Path(
        "assets/images/enemy/caballero/caminar_direccion_derecha")
    ENEMIGO_IZQ: Path = Path(
        "assets/images/enemy/caballero/caminar_direccion_izquierda")

    # * Enemigos caballero
    ENEMIGO_FRENTE_1: Path = Path(f"{ENEMIGO_FRENTE}/caminar_frente1.png")
    ENEMIGO_FRENTE_2: Path = Path(f"{ENEMIGO_FRENTE}/caminar_frente2.png")
    ENEMIGO_FRENTE_3: Path = Path(f"{ENEMIGO_FRENTE}/caminar_frente3.png")
    ENEMIGO_FRENTE_4: Path = Path(f"{ENEMIGO_FRENTE}/caminar_frente4.png")
    ENEMIGO_FRENTE_5: Path = Path(f"{ENEMIGO_FRENTE}/caminar_frente5.png")
    ENEMIGO_FRENTE_6: Path = Path(f"{ENEMIGO_FRENTE}/caminar_frente6.png")

    ENEMIGO_ATRAS_1: Path = Path(f"{ENEMIGO_ESPALDA}/caminar_espalda1.png")
    ENEMIGO_ATRAS_2: Path = Path(f"{ENEMIGO_ESPALDA}/caminar_espalda2.png")
    ENEMIGO_ATRAS_3: Path = Path(f"{ENEMIGO_ESPALDA}/caminar_espalda3.png")
    ENEMIGO_ATRAS_4: Path = Path(f"{ENEMIGO_ESPALDA}/caminar_espalda4.png")
    ENEMIGO_ATRAS_5: Path = Path(f"{ENEMIGO_ESPALDA}/caminar_espalda5.png")
    ENEMIGO_ATRAS_6: Path = Path(f"{ENEMIGO_ESPALDA}/caminar_espalda6.png")

    ENEMIGO_DERECHA_1: Path = Path(f"{ENEMIGO_DER}/caminar_der1.png")
    ENEMIGO_DERECHA_2: Path = Path(f"{ENEMIGO_DER}/caminar_der2.png")
    ENEMIGO_DERECHA_3: Path = Path(f"{ENEMIGO_DER}/caminar_der3.png")
    ENEMIGO_DERECHA_4: Path = Path(f"{ENEMIGO_DER}/caminar_der4.png")
    ENEMIGO_DERECHA_5: Path = Path(f"{ENEMIGO_DER}/caminar_der5.png")
    ENEMIGO_DERECHA_6: Path = Path(f"{ENEMIGO_DER}/caminar_der6.png")

    ENEMIGO_IZQUIERDA_1: Path = Path(f"{ENEMIGO_IZQ}/caminar_izq1.png")
    ENEMIGO_IZQUIERDA_2: Path = Path(f"{ENEMIGO_IZQ}/caminar_izq2.png")
    ENEMIGO_IZQUIERDA_3: Path = Path(f"{ENEMIGO_IZQ}/caminar_izq3.png")
    ENEMIGO_IZQUIERDA_4: Path = Path(f"{ENEMIGO_IZQ}/caminar_izq4.png")
    ENEMIGO_IZQUIERDA_5: Path = Path(f"{ENEMIGO_IZQ}/caminar_izq5.png")
    ENEMIGO_IZQUIERDA_6: Path = Path(f"{ENEMIGO_IZQ}/caminar_izq6.png")

    # * Enemigo caballero 2 Barrer
    ENEMIGO2_FRENTE: Path = Path(
        "assets/images/enemy/enemigo_2/caminar_frente")
    ENEMIGO2_ESPALDA: Path = Path(
        "assets/images/enemy/enemigo_2/caminar_espalda")
    ENEMIGO2_DERECHA: Path = Path(
        "assets/images/enemy/enemigo_2/caminar_derecha")
    ENEMIGO2_IZQUIERDA: Path = Path(
        "assets/images/enemy/enemigo_2/caminar_izquierda")

    # * Enemigo caballero 2
    ENEMIGO2_FRENTE_1: Path = Path(
        f"{ENEMIGO2_FRENTE}/cab2_caminar_frente1.png")
    ENEMIGO2_FRENTE_2: Path = Path(
        f"{ENEMIGO2_FRENTE}/cab2_caminar_frente2.png")
    ENEMIGO2_FRENTE_3: Path = Path(
        f"{ENEMIGO2_FRENTE}/cab2_caminar_frente3.png")
    ENEMIGO2_FRENTE_4: Path = Path(
        f"{ENEMIGO2_FRENTE}/cab2_caminar_frente4.png")
    ENEMIGO2_FRENTE_5: Path = Path(
        f"{ENEMIGO2_FRENTE}/cab2_caminar_frente5.png")
    ENEMIGO2_FRENTE_6: Path = Path(
        f"{ENEMIGO2_FRENTE}/cab2_caminar_frente6.png")
    ENEMIGO2_FRENTE_7: Path = Path(
        f"{ENEMIGO2_FRENTE}/cab2_caminar_frente7.png")
    ENEMIGO2_FRENTE_8: Path = Path(
        f"{ENEMIGO2_FRENTE}/cab2_caminar_frente8.png")

    ENEMIGO2_ATRAS_1: Path = Path(
        f"{ENEMIGO2_ESPALDA}/cab2_caminar_espalda1.png")
    ENEMIGO2_ATRAS_2: Path = Path(
        f"{ENEMIGO2_ESPALDA}/cab2_caminar_espalda2.png")
    ENEMIGO2_ATRAS_3: Path = Path(
        f"{ENEMIGO2_ESPALDA}/cab2_caminar_espalda3.png")
    ENEMIGO2_ATRAS_4: Path = Path(
        f"{ENEMIGO2_ESPALDA}/cab2_caminar_espalda4.png")
    ENEMIGO2_ATRAS_5: Path = Path(
        f"{ENEMIGO2_ESPALDA}/cab2_caminar_espalda5.png")
    ENEMIGO2_ATRAS_6: Path = Path(
        f"{ENEMIGO2_ESPALDA}/cab2_caminar_espalda6.png")
    ENEMIGO2_ATRAS_7: Path = Path(
        f"{ENEMIGO2_ESPALDA}/cab2_caminar_espalda7.png")
    ENEMIGO2_ATRAS_8: Path = Path(
        f"{ENEMIGO2_ESPALDA}/cab2_caminar_espalda8.png")

    ENEMIGO2_DERECHA_1: Path = Path(
        f"{ENEMIGO2_DERECHA}/cab2_caminar_der1.png")
    ENEMIGO2_DERECHA_2: Path = Path(
        f"{ENEMIGO2_DERECHA}/cab2_caminar_der2.png")
    ENEMIGO2_DERECHA_3: Path = Path(
        f"{ENEMIGO2_DERECHA}/cab2_caminar_der3.png")
    ENEMIGO2_DERECHA_4: Path = Path(
        f"{ENEMIGO2_DERECHA}/cab2_caminar_der4.png")
    ENEMIGO2_DERECHA_5: Path = Path(
        f"{ENEMIGO2_DERECHA}/cab2_caminar_der5.png")
    ENEMIGO2_DERECHA_6: Path = Path(
        f"{ENEMIGO2_DERECHA}/cab2_caminar_der6.png")
    ENEMIGO2_DERECHA_7: Path = Path(
        f"{ENEMIGO2_DERECHA}/cab2_caminar_der7.png")
    ENEMIGO2_DERECHA_8: Path = Path(
        f"{ENEMIGO2_DERECHA}/cab2_caminar_der8.png")

    ENEMIGO2_IZQUIERDA_1: Path = Path(
        f"{ENEMIGO2_IZQUIERDA}/cab2_caminar_izq1.png")
    ENEMIGO2_IZQUIERDA_2: Path = Path(
        f"{ENEMIGO2_IZQUIERDA}/cab2_caminar_izq2.png")
    ENEMIGO2_IZQUIERDA_3: Path = Path(
        f"{ENEMIGO2_IZQUIERDA}/cab2_caminar_izq3.png")
    ENEMIGO2_IZQUIERDA_4: Path = Path(
        f"{ENEMIGO2_IZQUIERDA}/cab2_caminar_izq4.png")
    ENEMIGO2_IZQUIERDA_5: Path = Path(
        f"{ENEMIGO2_IZQUIERDA}/cab2_caminar_izq5.png")
    ENEMIGO2_IZQUIERDA_6: Path = Path(
        f"{ENEMIGO2_IZQUIERDA}/cab2_caminar_izq6.png")

    """
        #Future  Animacion
    
        ENEMIGO2_IZQUIERDA_7: Path = Path(
        f"{ENEMIGO2_IZQUIERDA}/cab2_caminar_izq7.png")
    ENEMIGO2_IZQUIERDA_8: Path = Path(
        f"{ENEMIGO2_IZQUIERDA}/cab2_caminar_izq8.png")
    
    """

    # * Bloques

    TILE_MADERA: Path = Path(
        "assets/images/bloque_madera/Caja_madera.png")
    TILE_PIEDRA: Path = Path(
        "assets/images/bloque_piedra/bloque_piedra.png")

    # * Fondo Mapa
    FONDO_MAPA: Path = Path("assets/images/background/fondo_imagen.png")

    # * Fondo Menu
    FONDO_MENU: Path = Path("assets/images/pantalla_inicio/inicio.png")

    # * Bomba

    BOMBA: Path = Path("assets/images/bomb")

    BOMBA_ANIMACION: Path = Path(f"{BOMBA}/fire_principal.png")

    EXPLOSION: Path = Path("assets/images/bomb")

    EXPLOSION_1: Path = Path(f"{EXPLOSION}/fire2.png")
    EXPLOSION_2: Path = Path(f"{EXPLOSION}/fire3.png")
    EXPLOSION_3: Path = Path(f"{EXPLOSION}/fire4.png")
    EXPLOSION_4: Path = Path(f"{EXPLOSION}/fire5.png")
    EXPLOSION_5: Path = Path(f"{EXPLOSION}/fire6.png")
    EXPLOSION_6: Path = Path(f"{EXPLOSION}/fire7.png")
    EXPLOSION_7: Path = Path(f"{EXPLOSION}/fire8.png")

    # * fin juego

    FIN_JUEGO: Path = Path("assets/images/fin de juego/fin_juego.png")

    """
        #! Disclaimer:
        #? Para los sonidos se recomienda usar archivos .WAV o .OGG

        #?Para la música de fondo se recomienda usar archivos .MP3 

        Para la Musica 
            pygame.mixer.music.load(RUTA)
            pygame.mixer.music.play(-1) # -1 para que se repita 
            #? Lo ideal es usarlo en el bucle principal del juego


        Para los efectos de sonido
            var = pygame.mixer.Sound(RUTA)
            var.play() #? para reproducir el sonido luego de X o Y accion

    """

    # * Musica
    # ! fondo_completo.mp3 (Archivo corrupto)
    MUSICA_FONDO: Path = Path("assets/sound/music/fondo.mp3")

    # * Sonidos
    SONIDO_TRANCISION: Path = Path("assets/sound/effects/transición.wav")

    """
        A su definir cuales sonidos son del player y cuales osn del enemigo , ahi sonidos con variables que hacen referencia al player peor están asignados a la clase enemigo
    """

    SONIDO_PERSONAJE_RUGIDO: Path = Path(
        "assets/sound/effects/rugido_dragon.wav")
    SONIDO_PERSONAJE_ATAQUE: Path = Path(
        "assets/sound/effects/ataque_enemigo.wav")
    SONIDO_BOMBA: Path = Path("assets/sound/effects/explosion_bomba.wav")
    SONIDO_BOTON: Path = Path("assets/sound/effects/Botones.wav")
