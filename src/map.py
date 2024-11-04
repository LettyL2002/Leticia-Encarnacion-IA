import pygame
import random


class Map:
    """
    Clase que representa el mapa del juego con tiles de diferentes tipos.

    _summary_ 
           - tile_size: tamaño de los tiles
           - grid_width: ancho de la grilla
           - grid_height: alto de la grilla
    """

    def __init__(self, tile_size=30, grid_width=25, grid_height=25):
        # Configuración del mapa
        self.tile_size = tile_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.width = grid_width * tile_size
        self.height = grid_height * tile_size

        # Inicializar la grilla
        self.grid = [[0 for _ in range(grid_width)]
                     for _ in range(grid_height)]

        # Cargar imágenes
        self.load_images()

        # Generar el mapa
        self.generate_map()

    def load_images(self):
        """Carga y escala todas las imágenes necesarias"""
        # Cargar background

        FONDO = "fondo_imagen.png"
        self.background = pygame.image.load(FONDO)
        self.background = pygame.transform.scale(
            self.background, (self.width, self.height))

        TILE_MADERA = "Caja_madera.png"
        TILE_PIEDRA = "bloque_piedra.png"

        # Cargar tiles
        self.tiles = {
            0: None,  # Espacio vacío
            1: pygame.transform.scale(pygame.image.load(TILE_PIEDRA), (self.tile_size, self.tile_size)),
            2: pygame.transform.scale(pygame.image.load(TILE_MADERA), (self.tile_size, self.tile_size))
        }

    def generate_map(self):
        """Genera un mapa aleatorio con bloques de piedra y madera"""
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                rand = random.random()
                if rand < 0.2:  # 20% probabilidad de piedra
                    self.grid[y][x] = 1  # piedra
                elif rand < 0.4:  # 20% probabilidad de madera
                    self.grid[y][x] = 2  # madera
                # else: se queda en 0 (vacío)

    def get_tile_type(self, x, y):
        """Retorna el tipo de tile en una posición de la grilla"""
        if 0 <= x < self.grid_width and 0 <= y < self.grid_height:
            return self.grid[y][x]
        return None

    def is_walkable(self, x, y):
        """Verifica si una posición es transitable"""
        tile_type = self.get_tile_type(x, y)
        return tile_type == 0  # Solo es transitable si está vacío

    def draw(self, screen):
        """Dibuja el mapa completo"""
        # Dibujar background
        screen.blit(self.background, (0, 0))

        # Dibujar tiles
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                tile_type = self.grid[y][x]
                # Si no es vacío y tiene imagen
                if tile_type != 0 and self.tiles[tile_type]:
                    screen.blit(
                        self.tiles[tile_type],
                        (x * self.tile_size, y * self.tile_size)
                    )
