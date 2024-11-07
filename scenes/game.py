# Leticia Encarnacion Lopez (22-SISN-2-008)

import pygame
from utils.constants import Constants
from entities.enemy import Enemy
from map.map import Map
from entities.player import Player
from utils.assets import Assets


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()

        # Crear el mapa
        self.map = Map()

        # Buscar primera pos valida
        grid_x = 0
        grid_y = 0
        while not self.map.is_walkable(grid_x, grid_y):
            grid_x += 1
        if grid_x >= self.map.grid_width:
            grid_x = 0
            grid_y += 1

        # Crear jugador en posición valida
        self.player = Player(grid_x * Constants.TILE_SIZE,
                             grid_y * Constants.TILE_SIZE,
                             self.map)

        # Crear enemigo en una posición válida
        spawn_x, spawn_y = self.map.find_valid_spawn_position()
        self.enemy = Enemy(spawn_x * Constants.TILE_SIZE,
                           spawn_y * Constants.TILE_SIZE,
                           self.map)
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

        # Procesar las teclas presionadas continuamente
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            self.player.move()

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
        SONIDO_TRANCISION = pygame.mixer.Sound(Assets.SONIDO_TRANCISION)
        SONIDO_TRANCISION.play()

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
