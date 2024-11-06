from enum import Enum
import math
import pygame
from ai.astar import AStar
from entities.bomb import Bomb
from ai.nodo import Accion, Secuencia, Selector, Timer
from utils.assets import Assets


class EnemyState(Enum):
    PATROL = 1
    CHASE = 2
    ATTACK = 3
    RETURN = 4


class Enemy:
    def __init__(self, x, y, game_map, patrol_points=None, tile_size=30):
        # Atributos básicos
        self.grid_x = x // tile_size
        self.grid_y = y // tile_size
        self.x = self.grid_x * tile_size
        self.y = self.grid_y * tile_size
        self.map = game_map
        self.tile_size = tile_size
        self.is_moving = False
        self.target_x = self.x
        self.target_y = self.y
        self.state = EnemyState.PATROL
        self.detection_range = 5
        self.path = []
        self.current_patrol_point = 0
        self.target = None
        self.pathfinder = AStar(game_map)
        self.move_cooldown = 0

        # Ajusta este valor para controlar la velocidad (frames entre movimientos)
        self.move_delay = 15

        # Puntos de patrulla
        self.patrol_points = patrol_points or [
            (1, 1),
            (game_map.grid_width-2, 1),
            (game_map.grid_width-2, game_map.grid_height-2),
            (1, game_map.grid_height-2)
        ]

        # Configuración visual
        self.image = pygame.Surface((tile_size-6, tile_size-6))
        self.image.fill((255, 0, 0))
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
        timer_ataque = Timer(60)
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
        
        #sonido
        var = pygame.mixer.Sound(Assets.SONIDO_ENEMIGO_ATAQUE)
        var.play(atacar)

    def update_rect_position(self):
        self.rect.x = self.x + 3
        self.rect.y = self.y + 3

    def detect_player(self):
        if self.target is None:
            return False

        player_pos = self.target.get_position_for_astar()
        distance = math.sqrt((player_pos[0] - self.grid_x)**2 +
                             (player_pos[1] - self.grid_y)**2)

        if distance <= self.detection_range:
            self.state = EnemyState.CHASE
            return True
        return False

    def update_chase_path(self):
        if self.target is None:
            return False

        start = (self.grid_x, self.grid_y)
        goal = self.target.get_position_for_astar()

        self.path = self.pathfinder.find_path(start, goal)
        return len(self.path) > 0

    def update_patrol_path(self):
        start = (self.grid_x, self.grid_y)
        goal = self.patrol_points[self.current_patrol_point]

        if start == goal:
            self.current_patrol_point = (
                self.current_patrol_point + 1) % len(self.patrol_points)
            goal = self.patrol_points[self.current_patrol_point]

        self.path = self.pathfinder.find_path(start, goal)
        return True

    def move_along_path(self):
        if not self.path or len(self.path) < 2:
            return False

        # Control de velocidad de movimiento
        if self.move_cooldown > 0:
            self.move_cooldown -= 1
            return True

        # Obtener siguiente posición en el camino
        next_pos = self.path[1]
        target_x = next_pos[0] * self.tile_size
        target_y = next_pos[1] * self.tile_size

        # Verificar si podemos movernos a la siguiente posición
        temp_rect = pygame.Rect(target_x + 3, target_y + 3,
                                self.rect.width, self.rect.height)

        if not self.map.get_colliding_blocks(temp_rect):
            # Actualizar posición
            self.x = target_x
            self.y = target_y
            self.grid_x = next_pos[0]
            self.grid_y = next_pos[1]
            self.path.pop(0)
            self.update_rect_position()
            self.move_cooldown = self.move_delay
            return True

        # Si hay colisión, recalcular ruta
        self.path = []
        return False

    def is_in_attack_range(self):
        if self.target is None:
            return False

        player_pos = self.target.get_position_for_astar()
        return math.sqrt((player_pos[0] - self.grid_x)**2 +
                         (player_pos[1] - self.grid_y)**2) <= 1.5

    def attack(self):
        if self.target is None:
            return False

        # Plantar una bomba
        Bomb = Bomb(self.grid_x, self.grid_y, self.tile_size)
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
