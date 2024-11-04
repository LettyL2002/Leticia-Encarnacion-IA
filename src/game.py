import pygame
from config import CONFIG
from constants import Constants
from enemy import Enemy
from map import Map
from player import Player


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()

        # Crear el mapa
        self.map = Map()

        # Crear jugador (posición inicial)
        self.player = Player(Constants.TILE_SIZE,
                             Constants.TILE_SIZE, self.map)

        # Crear enemigo
        enemy_x = (self.map.grid_width - 2) * Constants.TILE_SIZE
        enemy_y = (self.map.grid_height - 2) * Constants.TILE_SIZE
        self.enemy = Enemy(enemy_x, enemy_y, self.map)
        self.enemy.set_target(self.player)

        # Lista de bombas activas
        self.bombs = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        self.player.update()
        self.enemy.update()

        # Actualizar bombas
        for bomb in self.bombs[:]:
            bomb.update()
            if bomb.should_explode():
                self.bombs.remove(bomb)
                # Lógica de explosión

    def draw(self):
        self.screen.fill(Constants.BLACK)

        # Dibujar mapa
        self.map.draw(self.screen)

        # Dibujar bombas
        for bomb in self.bombs:
            bomb.draw(self.screen)

        # Dibujar jugador y enemigo
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
