import pygame
from utils.assets import Assets


class Bomb:
    def __init__(self, grid_x, grid_y, tile_size):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.tile_size = tile_size
        self.timer = 180  # 3 segundos a 60 FPS
        self.explosion_radius = 2
        self.SONIDO= pygame.mixer.Sound(Assets.SONIDO_BOMBA)
        
        self.image = pygame.Surface((tile_size-10, tile_size-10))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = grid_x * tile_size + 5
        self.rect.y = grid_y * tile_size + 5

    def update(self):
        self.timer -= 1

    def should_explode(self):
        return self.timer <= 0

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)