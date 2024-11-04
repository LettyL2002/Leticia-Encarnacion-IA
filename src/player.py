import pygame
import math
from enum import Enum
from bomb import Bomb
from nodo import Selector, Secuencia, Accion, Timer


# Estados del jugador

class PlayerState(Enum):
    IDLE = 1
    MOVING = 2
    PLANTING_BOMB = 3
    DAMAGED = 4


class Player:
    def __init__(self, x, y, game_map, tile_size=50):
        # Atributos básicos
        self.x = x
        self.y = y
        self.map = game_map
        self.tile_size = tile_size
        self.speed = 5
        self.state = PlayerState.IDLE
        self.health = 100
        self.bombs = []
        self.bomb_limit = 3
        self.invulnerable = False

        # Sprite y rectángulo de colisión
        self.image = pygame.Surface((tile_size-10, tile_size-10))
        self.image.fill((0, 255, 0))  # Color verde para el jugador
        self.rect = self.image.get_rect()
        self.update_rect_position()

        # Configuración del árbol de comportamientos
        self.setup_behavior_tree()

    def setup_behavior_tree(self):
        self.comportamiento = Selector()

        # Secuencias principales
        secuencia_danado = Secuencia()
        secuencia_movimiento = Secuencia()
        secuencia_bomba = Secuencia()
        secuencia_idle = Secuencia()

        # Agregar secuencias al comportamiento principal
        self.comportamiento.agregar_hijo(secuencia_danado)
        self.comportamiento.agregar_hijo(secuencia_bomba)
        self.comportamiento.agregar_hijo(secuencia_movimiento)
        self.comportamiento.agregar_hijo(secuencia_idle)

        # Secuencia de daño
        esta_danado = Accion(lambda: self.state == PlayerState.DAMAGED)
        timer_invulnerable = Timer(60)  # 1 segundo de invulnerabilidad
        timer_invulnerable.agregar_hijo(Accion(self.end_invulnerability))
        secuencia_danado.agregar_hijo(esta_danado)
        secuencia_danado.agregar_hijo(timer_invulnerable)

        # Secuencia de colocación de bomba
        puede_poner_bomba = Accion(self.can_plant_bomb)
        plantar_bomba = Accion(self.plant_bomb)
        secuencia_bomba.agregar_hijo(puede_poner_bomba)
        secuencia_bomba.agregar_hijo(plantar_bomba)

        # Secuencia de movimiento
        hay_input = Accion(self.check_movement_input)
        mover = Accion(self.move)
        secuencia_movimiento.agregar_hijo(hay_input)
        secuencia_movimiento.agregar_hijo(mover)

        # Secuencia idle
        secuencia_idle.agregar_hijo(Accion(self.idle))

    def update_rect_position(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def check_movement_input(self):
        keys = pygame.key.get_pressed()
        return any([keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]])

    def move(self):
        keys = pygame.key.get_pressed()
        new_x, new_y = self.x, self.y

        if keys[pygame.K_LEFT]:
            new_x -= self.speed
        if keys[pygame.K_RIGHT]:
            new_x += self.speed
        if keys[pygame.K_UP]:
            new_y -= self.speed
        if keys[pygame.K_DOWN]:
            new_y += self.speed

        # Verificar colisiones con el mapa
        grid_x = new_x // self.tile_size
        grid_y = new_y // self.tile_size

        if self.map.is_walkable(grid_x, grid_y):
            self.x = new_x
            self.y = new_y
            self.update_rect_position()
            self.state = PlayerState.MOVING
            return True
        return False

    def can_plant_bomb(self):
        return (len(self.bombs) < self.bomb_limit and
                pygame.key.get_pressed()[pygame.K_SPACE])

    def plant_bomb(self):
        grid_x = self.x // self.tile_size
        grid_y = self.y // self.tile_size
        bomb = Bomb(grid_x, grid_y, self.tile_size)
        self.bombs.append(bomb)
        self.state = PlayerState.PLANTING_BOMB
        return True

    def take_damage(self, damage):
        if not self.invulnerable:
            self.health -= damage
            self.invulnerable = True
            self.state = PlayerState.DAMAGED
            return True
        return False

    def end_invulnerability(self):
        self.invulnerable = False
        self.state = PlayerState.IDLE
        return True

    def idle(self):
        self.state = PlayerState.IDLE
        return True

    def update_bombs(self):
        for bomb in self.bombs[:]:
            bomb.update()
            if bomb.should_explode():
                self.bombs.remove(bomb)

    def get_position_for_astar(self):
        return (self.x // self.tile_size, self.y // self.tile_size)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0)
                         if not self.invulnerable else (255, 0, 0), self.rect)

    def update(self):
        self.comportamiento.ejecutar()
        self.update_bombs()
