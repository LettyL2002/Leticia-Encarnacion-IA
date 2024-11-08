# Leticia Encarnacion Lopez (22-SISN-2-008)

from re import S
import pygame
import sys
from pathlib import Path
from scenes.creditos import credits_screen
from utils.constants import Constants
from utils.assets import Assets
from scenes.game import Game
from utils.strings import STRINGS
from map.map import Map

# Set up the display
screen = pygame.display.set_mode((Constants.ANCHO_MENU, Constants.ALTO_MENU))
pygame.display.set_caption(STRINGS.TITLE_VENTANA)

# Set up the fonts
pygame.font.init()
font = Constants.FUENTE_PRINCIPAL_MENU
small_font = Constants.FUENTE_PEQUENA_MENU
axis_handled = False

# sonido de fondo
pygame.mixer.music.load(Assets.MUSICA_FONDO)

SONIDO_BOTTOM = pygame.mixer.Sound(Assets.SONIDO_BOTON)


# Load and scale background image
background_image = pygame.image.load(Assets.FONDO_MENU)
background_image = pygame.transform.scale(
    background_image, (Constants.ANCHO_MENU, Constants.ALTO_MENU))

# Initialize joystick
pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

# OPTIONS
selected_option = 0

# Add these variables near the other globals
JOYSTICK_COOLDOWN = 200  # milliseconds
last_joystick_movement = 0


def draw_menu():
    screen.blit(background_image, (0, 0))  # Draw the background image
    title_text = font.render("Dragon’s Bombardment", True, Constants.WHITE)
    screen.blit(title_text, (Constants.ANCHO_MENU // 2 -
                title_text.get_width() // 2, 100))

    for index, option in enumerate(STRINGS.MENU_OPCIONES):
        if index == selected_option:
            option_text = small_font.render(option, True, Constants.WHITE)
        else:
            option_text = small_font.render(option, True, (100, 100, 100))
        screen.blit(option_text, (Constants.ANCHO_MENU // 2 -
                    option_text.get_width() // 2, 300 + index * 50))

    pygame.display.flip()


def handle_keydown(key):
    global selected_option
    if key == pygame.K_UP:
        selected_option = (selected_option - 1) % len(STRINGS.MENU_OPCIONES)
    elif key == pygame.K_DOWN:
        selected_option = (selected_option + 1) % len(STRINGS.MENU_OPCIONES)


def handle_events():
    global selected_option, last_joystick_movement
    try:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(STRINGS.MENU_OPCIONES)
                    SONIDO_BOTTOM.play()
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(STRINGS.MENU_OPCIONES)
                    SONIDO_BOTTOM.play()
                elif event.key == pygame.K_RETURN:
                    handle_selection()
            elif event.type == pygame.JOYAXISMOTION and joystick:
                if event.axis == 1:  # Vertical axis
                    # Only process joystick input if enough time has passed
                    if current_time - last_joystick_movement > JOYSTICK_COOLDOWN:
                        if event.value < -0.5:
                            selected_option = (selected_option - 1) % len(STRINGS.MENU_OPCIONES)
                            SONIDO_BOTTOM.play()
                            last_joystick_movement = current_time
                        elif event.value > 0.5:
                            selected_option = (selected_option + 1) % len(STRINGS.MENU_OPCIONES)
                            SONIDO_BOTTOM.play()
                            last_joystick_movement = current_time
            elif event.type == pygame.JOYBUTTONDOWN and joystick:
                if event.button == 0:  # A button
                    handle_selection()

    except Exception as e:
        print(f"Error handling events: {e}")
        pygame.event.clear()  # Clear event queue if there's an error


def handle_selection():
    if selected_option == 0:
        game = Game(screen)
        game.run()
    elif selected_option == 1:
        credits_screen()
    elif selected_option == 2:
        pygame.quit()
        sys.exit()


def main_menu():
    global axis_handled
    axis_handled = False
    clock = pygame.time.Clock()
    pygame.mixer.music.play(-1)
    
    while True:
        handle_events()
        draw_menu()
        clock.tick(60)  # Control frame rate
        axis_handled = False
