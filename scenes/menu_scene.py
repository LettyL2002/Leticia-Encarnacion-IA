import pygame
import sys
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

# OPTIONS
selected_option = 0


def draw_menu():
    screen.fill(Constants.BLACK)
    title_text = font.render("Bomberman", True, Constants.WHITE)
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


def handle_events():
    global selected_option
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            handle_keydown(event.key)


def handle_keydown(key):
    global selected_option
    if key == pygame.K_UP:
        selected_option = (selected_option - 1) % len(STRINGS.MENU_OPCIONES)
    elif key == pygame.K_DOWN:
        selected_option = (selected_option + 1) % len(STRINGS.MENU_OPCIONES)
    elif key == pygame.K_RETURN:
        handle_selection()


def handle_selection():
    if selected_option == 0:
        game = Game(screen)
        game.run()
    elif selected_option == 1:
        print("Options selected")
    elif selected_option == 2:
        pygame.quit()
        sys.exit()


def main_menu():
    while True:
        handle_events()
        draw_menu()
