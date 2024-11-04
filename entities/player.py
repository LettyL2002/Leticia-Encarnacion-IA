import pygame
import math
from enum import Enum
from entities.bomb import Bomb
from ai.nodo import Selector, Secuencia, Accion, Timer


class PlayerState(Enum):
    IDLE = 1
    MOVING = 2
    PLANTING_BOMB = 3
    DAMAGED = 4


class Player:
    def __init__(self, grid_x, grid_y, game_map, tile_size=30):
        # Atributos básicos
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.map = game_map
        self.tile_size = tile_size

        # Posición y movimiento
        self.x = grid_x * tile_size
        self.y = grid_y * tile_size
        self.target_x = self.x
        self.target_y = self.y
        self.speed = 4
        self.is_moving = False

        # Estado y atributos del jugador
        self.state = PlayerState.IDLE
        self.health = 100
        self.bombs = []
        self.bomb_limit = 3
        self.invulnerable = False

        # Configuración del sprite
        self.image = pygame.Surface((tile_size - 6, tile_size - 6))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.update_rect_position()

        # Árbol de comportamiento
        self.setup_behavior_tree()

    def setup_behavior_tree(self):
        """Configura el árbol de comportamiento completo"""
        self.comportamiento = Selector()

        # Crear las secuencias principales
        secuencia_danado = Secuencia()
        secuencia_movimiento = Secuencia()
        secuencia_bomba = Secuencia()
        secuencia_idle = Secuencia()

        # Agregar secuencias al selector principal
        self.comportamiento.agregar_hijo(secuencia_danado)
        self.comportamiento.agregar_hijo(secuencia_bomba)
        self.comportamiento.agregar_hijo(secuencia_movimiento)
        self.comportamiento.agregar_hijo(secuencia_idle)

        # Configurar secuencia de daño
        esta_danado = Accion(lambda: self.state == PlayerState.DAMAGED)
        timer_invulnerable = Timer(60)
        timer_invulnerable.agregar_hijo(Accion(self.end_invulnerability))
        secuencia_danado.agregar_hijo(esta_danado)
        secuencia_danado.agregar_hijo(timer_invulnerable)

        # Configurar secuencia de movimiento
        hay_input_movimiento = Accion(self.check_movement_input)
        ejecutar_movimiento = Accion(self.move)
        secuencia_movimiento.agregar_hijo(hay_input_movimiento)
        secuencia_movimiento.agregar_hijo(ejecutar_movimiento)

        # Configurar secuencia de bomba
        puede_poner_bomba = Accion(self.can_plant_bomb)
        plantar_bomba = Accion(self.plant_bomb)
        secuencia_bomba.agregar_hijo(puede_poner_bomba)
        secuencia_bomba.agregar_hijo(plantar_bomba)

        # Configurar secuencia idle
        secuencia_idle.agregar_hijo(Accion(self.idle))

    def update_rect_position(self):
        """Actualiza la posición del rectángulo de colisión"""
        self.rect.x = self.x + 3
        self.rect.y = self.y + 3

    def check_movement_input(self):
        """Verifica si hay input de movimiento válido"""
        if self.is_moving:
            return False
        keys = pygame.key.get_pressed()
        return any([keys[pygame.K_LEFT], keys[pygame.K_RIGHT],
                   keys[pygame.K_UP], keys[pygame.K_DOWN]])

    def move(self):
        """Ejecuta el movimiento del jugador"""
        if self.is_moving:
            # Continuar movimiento actual
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance < self.speed:
                # Llegada al destino
                self.x = self.target_x
                self.y = self.target_y
                self.is_moving = False
                self.grid_x = self.x // self.tile_size
                self.grid_y = self.y // self.tile_size
            else:
                # Movimiento continuo
                move_x = (dx / distance) * self.speed
                move_y = (dy / distance) * self.speed
                self.x += move_x
                self.y += move_y
        else:
            # Iniciar nuevo movimiento
            keys = pygame.key.get_pressed()
            new_grid_x = self.grid_x
            new_grid_y = self.grid_y

            if keys[pygame.K_LEFT]:
                new_grid_x -= 1
            elif keys[pygame.K_RIGHT]:
                new_grid_x += 1
            elif keys[pygame.K_UP]:
                new_grid_y -= 1
            elif keys[pygame.K_DOWN]:
                new_grid_y += 1

            # Verificar si la nueva posición es válida
            if (0 <= new_grid_x < self.map.grid_width and
                0 <= new_grid_y < self.map.grid_height and
                    self.map.is_walkable(new_grid_x, new_grid_y)):

                self.target_x = new_grid_x * self.tile_size
                self.target_y = new_grid_y * self.tile_size
                self.is_moving = True
                self.state = PlayerState.MOVING

        self.update_rect_position()

    def can_plant_bomb(self):
        """Verifica si se puede plantar una bomba"""
        if self.is_moving:
            return False
        return (len(self.bombs) < self.bomb_limit and
                pygame.key.get_pressed()[pygame.K_SPACE])

    def plant_bomb(self):
        """Planta una bomba en la posición actual"""
        bomb = Bomb(self.grid_x, self.grid_y, self.tile_size)
        self.bombs.append(bomb)
        self.state = PlayerState.PLANTING_BOMB
        return True

    def take_damage(self, damage):
        """Procesa el daño recibido"""
        if not self.invulnerable:
            self.health -= damage
            self.invulnerable = True
            self.state = PlayerState.DAMAGED
            return True
        return False

    def end_invulnerability(self):
        """Finaliza el estado de invulnerabilidad"""
        self.invulnerable = False
        self.state = PlayerState.IDLE
        return True

    def idle(self):
        """Estado de reposo"""
        if not self.is_moving:
            self.state = PlayerState.IDLE
        return True

    def update_bombs(self):
        """Actualiza el estado de las bombas"""
        for bomb in self.bombs[:]:
            bomb.update()
            if bomb.should_explode():
                self.bombs.remove(bomb)

    def get_position_for_astar(self):
        """Obtiene la posición para el algoritmo A*"""
        return (self.grid_x, self.grid_y)

    def draw(self, screen):
        """Dibuja el jugador en la pantalla"""
        color = (255, 0, 0) if self.invulnerable else (0, 255, 0)
        pygame.draw.rect(screen, color, self.rect)

    def update(self):
        """Actualiza el estado del jugador"""
        self.comportamiento.ejecutar()
        self.update_bombs()
