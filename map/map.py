# map.py
import pygame
import random
from map.tile import Block
from utils.assets import Assets
from utils.constants import Constants


class Map:
    """_summary_
            tile_size = Tamaño de los tiles
            grid_width = Ancho de la grilla
            grid_height = Alto de la grilla
    """

    def __init__(self, tile_size=30, grid_width=Constants.GRID_WIDTH, grid_height=Constants.GRID_HEIGHT):
        # Configuración del mapa
        self.tile_size = tile_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.width = grid_width * tile_size
        self.height = grid_height * tile_size

        # Inicializar la grilla y el grupo de sprites
        self.grid = [[0 for _ in range(grid_width)]
                     for _ in range(grid_height)]
        self.block_sprites = pygame.sprite.Group()

        # Cargar imágenes
        self.load_images()

        # Generar el mapa
        self.generate_map()

    def load_images(self):
        """Carga y escala todas las imágenes necesarias"""
        self.background = pygame.image.load(Assets.FONDO_MAPA)
        self.background = pygame.transform.scale(
            self.background, (self.width, self.height))

        # Definimos los tipos de bloques y sus imágenes
        self.tile_types = {
            1: ("piedra", "bloque_piedra.png"),
            2: ("madera", "Caja_madera.png")
        }

    def generate_map(self):
        """Genera un mapa aleatorio con bloques de piedra y madera"""
        self.block_sprites.empty()  # Limpiamos los sprites existentes

        for y in range(self.grid_height):
            for x in range(self.grid_width):
                rand = random.random()
                if rand < 0.2:  # 20% probabilidad de piedra
                    self.grid[y][x] = 1
                    self._create_block(x, y, "piedra")
                elif rand < 0.4:  # 20% probabilidad de madera
                    self.grid[y][x] = 2
                    self._create_block(x, y, "madera")

    def _create_block(self, x, y, block_type):
        """Crea un nuevo bloque y lo añade al grupo de sprites"""
        new_block = Block(x, y, block_type)
        self.block_sprites.add(new_block)

    def get_tile_type(self, x, y):
        """Retorna el tipo de tile en una posición de la grilla"""
        grid_x = x // self.tile_size
        grid_y = y // self.tile_size
        return self.grid[grid_y][grid_x]

    def is_walkable(self, grid_x, grid_y):
        """Verifica si una posición es transitable"""
        if 0 <= grid_x < self.grid_width and 0 <= grid_y < self.grid_height:
            return self.grid[grid_y][grid_x] == 0
        return False

    def get_colliding_blocks(self, rect):
        """Retorna los bloques que colisionan con un rectángulo dado"""
        colliding_blocks = []
        for sprite in self.block_sprites:
            if sprite.rect.colliderect(rect):
                colliding_blocks.append(sprite)
        return colliding_blocks

    def find_valid_spawn_position(self, occupied_positions=None):
        """
        Encuentra una posición válida para spawn que no esté ocupada por bloques
        u otras entidades.

        Args:
            occupied_positions: Lista de tuplas (x,y) que ya están ocupadas por otras entidades

        Returns:
            tuple: (x,y) coordenadas válidas para spawn
        """
        if occupied_positions is None:
            occupied_positions = []

        # Crear lista de todas las posiciones posibles
        all_positions = [(x, y)
                         for x in range(1, self.grid_width-1)
                         for y in range(1, self.grid_height-1)]

        # Filtrar posiciones válidas
        valid_positions = [
            pos for pos in all_positions
            if self.is_walkable(pos[0], pos[1]) and pos not in occupied_positions
        ]

        if not valid_positions:
            raise ValueError(
                "No hay posiciones válidas disponibles para spawn")

        # Ordenar posiciones por distancia al centro para mejor distribución
        center_x = self.grid_width // 2
        center_y = self.grid_height // 2
        valid_positions.sort(key=lambda pos: (
            abs(pos[0] - center_x) + abs(pos[1] - center_y)
        ))

        # Retornar la primera posición válida
        return valid_positions[0]

    def get_safe_spawn_positions(self, min_distance=5):
        """
        Encuentra múltiples posiciones de spawn seguras y separadas entre sí.

        Args:
            min_distance: Distancia mínima entre spawns

        Returns:
            list: Lista de tuplas (x,y) con posiciones válidas
        """
        spawns = []
        occupied = []

        # Encontrar primera posición para el jugador
        player_pos = self.find_valid_spawn_position()
        spawns.append(player_pos)
        occupied.append(player_pos)

        # Encontrar posición para el enemigo
        try:
            # Filtrar posiciones que estén muy cerca del jugador
            enemy_pos = self.find_valid_spawn_position(occupied)
            while (abs(enemy_pos[0] - player_pos[0]) +
                   abs(enemy_pos[1] - player_pos[1])) < min_distance:
                occupied.append(enemy_pos)
                enemy_pos = self.find_valid_spawn_position(occupied)
            spawns.append(enemy_pos)
        except ValueError:
            # Si no hay posición válida, usar una más cercana
            enemy_pos = self.find_valid_spawn_position(occupied[:1])
            spawns.append(enemy_pos)

        return spawns

    def draw(self, screen):
        """Dibuja el mapa completo"""
        # Dibujar background
        screen.blit(self.background, (0, 0))
        # Dibujar todos los sprites de bloques
        self.block_sprites.draw(screen)
