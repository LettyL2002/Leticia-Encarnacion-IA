import pygame as pg
from constants import Constants, Assets


class Block(pg.sprite.Sprite):
    def __init__(self, x, y, block_type):
        super().__init__()
        self.block_type = block_type

        # Cargar la imagen correspondiente según el tipo de bloque
        if block_type == 'piedra':
            self.image = pg.image.load(Assets.TILE_PIEDRA)
        elif block_type == 'madera':
            self.image = pg.image.load(Assets.TILE_MADERA)

        # Escalar la imagen al tamaño del tile
        self.image = pg.transform.scale(
            self.image, (Constants.TILE_SIZE, Constants.TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x * Constants.TILE_SIZE
        self.rect.y = y * Constants.TILE_SIZE

        # Atributos adicionales
        # Solo los bloques de madera son rompibles
        self.breakable = block_type == 'madera'
