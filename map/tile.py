import pygame
from utils.constants import Constants
from utils.assets import Assets
from pathlib import Path


class Block(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, block_type: str) -> None:
        super().__init__()
        self.block_type = block_type

        # Guardar coordenadas de grilla
        self.grid_x = x
        self.grid_y = y

        # Cargar la imagen según el tipo
        image_path: Path = Assets.TILE_PIEDRA if block_type == "piedra" else Assets.TILE_MADERA
        self.image = pygame.image.load(Path(image_path))
        # Usar el tile_size de la constante
        self.image = pygame.transform.scale(
            self.image, (Constants.TILE_SIZE, Constants.TILE_SIZE))

        # Configurar el rectángulo para colisiones
        self.rect = self.image.get_rect()
        self.rect.x = x * Constants.TILE_SIZE
        self.rect.y = y * Constants.TILE_SIZE

        # Propiedades del bloque
        self.breakable = block_type == "madera"

    def get_collision_rect(self):
        """Retorna el rectángulo de colisión del bloque"""
        return self.rect

    def break_block(self):
        """Intenta romper el bloque si es rompible"""
        if self.breakable:
            self.kill()  # Elimina el sprite del grupo
            return True
        return False
