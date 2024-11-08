# Leticia Encarnacion Lopez (22-SISN-2-008)

import pygame
import math
from enum import Enum
from entities.bomb import Bomb
from ai.nodo import Selector, Secuencia, Accion, Timer
from utils.assets import Assets


class Direction(Enum):
    FRONT = 1
    BACK = 2
    LEFT = 3
    RIGHT = 4


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
        self.speed = 1
        self.is_moving = False

        # Dirección actual
        self.direction = Direction.FRONT

        # Estado y atributos del jugador
        self.state = PlayerState.IDLE
        self.health = 100
        self.bombs = []
        self.bomb_limit = 3
        self.invulnerable = False

        # Configuración de animaciones
        self.animation_frame = 0
        self.animation_speed = 0.2
        self.animation_timer = 0

        # sonido

        self.sound_player = pygame.mixer.Sound(Assets.SONIDO_PERSONAJE_RUGIDO)

        # Cargar sprites
        self.sprites = self.load_sprites()

        # Configurar imagen inicial
        self.image = self.sprites['front'][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x + 3  # Centrar el sprite
        self.rect.y = self.y + 3

        # Árbol de comportamiento
        self.setup_behavior_tree()

    def load_sprites(self):
        sprites = {
            'front': [],
            'back': [],
            'right': [],
            'left': []
        }

        # Cargar sprites frontales
        front_paths = [Assets.PERSONAJE_FRENTE_1, Assets.PERSONAJE_FRENTE_2, Assets.PERSONAJE_FRENTE_3,
                       Assets.PERSONAJE_FRENTE_4, Assets.PERSONAJE_FRENTE_5, Assets.PERSONAJE_FRENTE_6]
        for path in front_paths:
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(
                image, (self.tile_size - 2, self.tile_size - 2))
            sprites['front'].append(image)

        # Cargar sprites traseros
        back_paths = [Assets.PERSONAJE_ATRAS_1, Assets.PERSONAJE_ATRAS_2, Assets.PERSONAJE_ATRAS_3,
                      Assets.PERSONAJE_ATRAS_4, Assets.PERSONAJE_ATRAS_5, Assets.PERSONAJE_ATRAS_6]
        for path in back_paths:
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(
                image, (self.tile_size - 2, self.tile_size - 2))
            sprites['back'].append(image)

        # Cargar sprites derechos
        right_paths = [Assets.PERSONAJE_DERECHA_1, Assets.PERSONAJE_DERECHA_2, Assets.PERSONAJE_DERECHA_3,
                       Assets.PERSONAJE_DERECHA_4, Assets.PERSONAJE_DERECHA_5, Assets.PERSONAJE_DERECHA_6]
        for path in right_paths:
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(
                image, (self.tile_size - 2, self.tile_size - 2))
            sprites['right'].append(image)

        # Cargar sprites izquierdos
        left_paths = [Assets.PERSONAJE_IZQUIERDA_1, Assets.PERSONAJE_IZQUIERDA_2, Assets.PERSONAJE_IZQUIERDA_3,
                      Assets.PERSONAJE_IZQUIERDA_4, Assets.PERSONAJE_IZQUIERDA_5, Assets.PERSONAJE_IZQUIERDA_6]
        for path in left_paths:
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(
                image, (self.tile_size - 2, self.tile_size - 2))
            sprites['left'].append(image)

        return sprites

    def update_animation(self):
        self.animation_timer += self.animation_speed

        if self.animation_timer >= 1:
            self.animation_timer = 0
            if self.is_moving or self.state == PlayerState.MOVING:
                self.animation_frame = (self.animation_frame + 1) % 6
            else:
                self.animation_frame = 0

        # Seleccionar sprite según dirección y estado
        direction_map = {
            Direction.FRONT: 'front',
            Direction.BACK: 'back',
            Direction.RIGHT: 'right',
            Direction.LEFT: 'left'
        }

        direction_key = direction_map[self.direction]
        self.image = self.sprites[direction_key][self.animation_frame]

    def update_rect_position(self):
        """Actualiza la posición del rectángulo del sprite"""
        self.rect.x = self.x + 3  # Ajuste para centrar
        self.rect.y = self.y + 3

    def setup_behavior_tree(self):
        # Acciones básicas
        mover = Accion(self.move)
        actualizar_animacion = Accion(self.update_animation)

        # Crear la secuencia y agregar los hijos individualmente
        secuencia_movimiento = Secuencia()
        secuencia_movimiento.agregar_hijo(mover)
        secuencia_movimiento.agregar_hijo(actualizar_animacion)

        # Timer para control de animación
        timer_animacion = Timer(0.1)

        # Selector principal
        self.comportamiento = Selector()
        self.comportamiento.agregar_hijo(secuencia_movimiento)
        self.comportamiento.agregar_hijo(timer_animacion)

    def draw(self, screen):
        if self.invulnerable:
            if pygame.time.get_ticks() % 200 < 100:
                screen.blit(self.image, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def update(self):
        self.comportamiento.ejecutar()
        self.update_animation()
        # self.update_bombs()

    def get_position_for_astar(self):
        """Retorna la posición actual del jugador en coordenadas de la cuadrícula para el pathfinding"""
        return (self.grid_x, self.grid_y)

    def move(self):
        if self.is_moving:
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance < self.speed:
                self.x = self.target_x
                self.y = self.target_y
                self.is_moving = False
                self.grid_x = self.x // self.tile_size
                self.grid_y = self.y // self.tile_size
                self.state = PlayerState.IDLE
            else:
                move_x = (dx / distance) * self.speed
                move_y = (dy / distance) * self.speed
                self.x += move_x
                self.y += move_y
        else:
            keys = pygame.key.get_pressed()
            new_grid_x = self.grid_x
            new_grid_y = self.grid_y

            if keys[pygame.K_LEFT]:
                new_grid_x -= 1
                self.direction = Direction.LEFT
            elif keys[pygame.K_RIGHT]:
                new_grid_x += 1
                self.direction = Direction.RIGHT
            elif keys[pygame.K_UP]:
                new_grid_y -= 1
                self.direction = Direction.BACK
            elif keys[pygame.K_DOWN]:
                new_grid_y += 1
                self.direction = Direction.FRONT

            if (0 <= new_grid_x < self.map.grid_width and
                0 <= new_grid_y < self.map.grid_height and
                    self.map.is_walkable(new_grid_x, new_grid_y)):

                self.target_x = new_grid_x * self.tile_size
                self.target_y = new_grid_y * self.tile_size
                self.is_moving = True
                self.state = PlayerState.MOVING

        self.update_rect_position()

    def move_with_joystick(self, axis_x, axis_y):
        if not self.is_moving:
            new_grid_x = self.grid_x
            new_grid_y = self.grid_y

            if axis_x < -0.1:
                new_grid_x -= 1
                self.direction = Direction.LEFT
            elif axis_x > 0.1:
                new_grid_x += 1
                self.direction = Direction.RIGHT
            if axis_y < -0.1:
                new_grid_y -= 1
                self.direction = Direction.BACK
            elif axis_y > 0.1:
                new_grid_y += 1
                self.direction = Direction.FRONT

            if (0 <= new_grid_x < self.map.grid_width and
                0 <= new_grid_y < self.map.grid_height and
                    self.map.is_walkable(new_grid_x, new_grid_y)):

                self.target_x = new_grid_x * self.tile_size
                self.target_y = new_grid_y * self.tile_size
                self.is_moving = True
                self.state = PlayerState.MOVING

        self.update_rect_position()
