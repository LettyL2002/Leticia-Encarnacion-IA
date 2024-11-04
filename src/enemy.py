from enum import Enum
import math
import pygame
from astar import AStar
from bomb import Bomb
from nodo import Accion, Secuencia, Selector, Timer

# Estados del enemigo


class EnemyState(Enum):
    PATROL = 1
    CHASE = 2
    ATTACK = 3
    RETURN = 4


class Enemy:
    def __init__(self, x, y, game_map, patrol_points=None, tile_size=50):
        # Atributos básicos
        self.x = x
        self.y = y
        self.map = game_map
        self.tile_size = tile_size
        self.speed = 3
        self.state = EnemyState.PATROL
        self.detection_range = 5  # En tiles
        self.path = []
        self.current_patrol_point = 0
        self.target = None
        self.pathfinder = AStar(game_map)

        # Puntos de patrulla
        self.patrol_points = patrol_points or [
            (1, 1),
            (game_map.grid_width-2, 1),
            (game_map.grid_width-2, game_map.grid_height-2),
            (1, game_map.grid_height-2)
        ]

        # Configuración visual
        self.image = pygame.Surface((tile_size-10, tile_size-10))
        self.image.fill((255, 0, 0))  # Color rojo para el enemigo
        self.rect = self.image.get_rect()
        self.update_rect_position()

        # Configuración del árbol de comportamientos
        self.setup_behavior_tree()

    def setup_behavior_tree(self):
        self.comportamiento = Selector()

        # Secuencias principales
        secuencia_persecucion = Secuencia()
        secuencia_patrulla = Secuencia()
        secuencia_ataque = Secuencia()

        # Agregar secuencias al comportamiento principal
        self.comportamiento.agregar_hijo(secuencia_ataque)
        self.comportamiento.agregar_hijo(secuencia_persecucion)
        self.comportamiento.agregar_hijo(secuencia_patrulla)

        # Secuencia de ataque
        esta_en_rango_ataque = Accion(self.is_in_attack_range)
        atacar = Accion(self.attack)
        timer_ataque = Timer(60)  # 1 segundo entre ataques
        timer_ataque.agregar_hijo(atacar)
        secuencia_ataque.agregar_hijo(esta_en_rango_ataque)
        secuencia_ataque.agregar_hijo(timer_ataque)

        # Secuencia de persecución
        detecta_jugador = Accion(self.detect_player)
        actualizar_path = Accion(self.update_chase_path)
        mover_hacia_jugador = Accion(self.move_along_path)
        secuencia_persecucion.agregar_hijo(detecta_jugador)
        secuencia_persecucion.agregar_hijo(actualizar_path)
        secuencia_persecucion.agregar_hijo(mover_hacia_jugador)

        # Secuencia de patrulla
        actualizar_patrulla = Accion(self.update_patrol_path)
        mover_patrulla = Accion(self.move_along_path)
        secuencia_patrulla.agregar_hijo(actualizar_patrulla)
        secuencia_patrulla.agregar_hijo(mover_patrulla)

    def update_rect_position(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def detect_player(self):
        if self.target is None:
            return False

        player_pos = self.target.get_position_for_astar()
        enemy_pos = (self.x // self.tile_size, self.y // self.tile_size)

        distance = math.sqrt((player_pos[0] - enemy_pos[0])**2 +
                             (player_pos[1] - enemy_pos[1])**2)

        if distance <= self.detection_range:
            self.state = EnemyState.CHASE
            return True
        return False

    def update_chase_path(self):
        if self.target is None:
            return False

        start = (self.x // self.tile_size, self.y // self.tile_size)
        goal = self.target.get_position_for_astar()

        self.path = self.pathfinder.find_path(start, goal)
        return len(self.path) > 0

    def update_patrol_path(self):
        start = (self.x // self.tile_size, self.y // self.tile_size)
        goal = self.patrol_points[self.current_patrol_point]

        if start == goal:
            self.current_patrol_point = (
                self.current_patrol_point + 1) % len(self.patrol_points)
            goal = self.patrol_points[self.current_patrol_point]

        self.path = self.pathfinder.find_path(start, goal)
        return True

    def move_along_path(self):
        if not self.path:
            return False

        next_pos = self.path[1] if len(self.path) > 1 else self.path[0]
        target_x = next_pos[0] * self.tile_size
        target_y = next_pos[1] * self.tile_size

        dx = target_x - self.x
        dy = target_y - self.y

        distance = math.sqrt(dx**2 + dy**2)

        if distance < self.speed:
            self.x = target_x
            self.y = target_y
            self.path.pop(0)
        else:
            self.x += (dx/distance) * self.speed
            self.y += (dy/distance) * self.speed

        self.update_rect_position()
        return True

    def is_in_attack_range(self):
        if self.target is None:
            return False

        player_pos = self.target.get_position_for_astar()
        enemy_pos = (self.x // self.tile_size, self.y // self.tile_size)

        return math.sqrt((player_pos[0] - enemy_pos[0])**2 +
                         (player_pos[1] - enemy_pos[1])**2) <= 1.5

    def attack(self):
        if self.target is None:
            return False

        # Plantar una bomba
        grid_x = self.x // self.tile_size
        grid_y = self.y // self.tile_size
        bomb = Bomb(grid_x, grid_y, self.tile_size)

        # FUTURE Agregar la bomba a una lista de bombas activas en el juego
        return True

    def set_target(self, player):
        self.target = player

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

        # Debug: dibujar el path
        if self.path:
            for i in range(len(self.path)-1):
                start_pos = (self.path[i][0] * self.tile_size + self.tile_size//2,
                             self.path[i][1] * self.tile_size + self.tile_size//2)
                end_pos = (self.path[i+1][0] * self.tile_size + self.tile_size//2,
                           self.path[i+1][1] * self.tile_size + self.tile_size//2)
                pygame.draw.line(screen, (255, 255, 0), start_pos, end_pos, 2)

    def update(self):
        self.comportamiento.ejecutar()
