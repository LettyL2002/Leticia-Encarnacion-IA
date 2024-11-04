import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Credits")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 36)

# Credits text
credits = [
    "Con el dolor de mi alma",
    "me puse a programar",
    "y este jueguito salió",
    "espero que lo disfruten",
    "porque me costó un montón",
    "y no sé qué más poner",
    "Gracias a mi familia\n",
    "Leticia Encarnación Lopez",
    "22-SISN-2-008"
]

# Function to render text


def render_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)


def credits_screen():
    clock = pygame.time.Clock()
    scroll_y = HEIGHT

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Exit the credits screen

        screen.fill(BLACK)

        # Render credits
        y = scroll_y
        for line in credits:
            render_text(line, font, WHITE, screen, WIDTH // 2, y)
            y += 40

        scroll_y -= 1
        if y < 0:
            scroll_y = HEIGHT

        pygame.display.flip()
        clock.tick(60)
