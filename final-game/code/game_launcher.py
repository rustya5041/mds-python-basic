import pygame
from pygame.sprite import Group
import settings
from programmer import *
from redbull import *
from logs import *

def launch():
    """game initialisation"""
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("Surviving HSE deadlines")
    bg_color = (254, 254, 254)  # white, (0, 0, 0) for black
    programmer = Programmer(screen)
    redbulls = Group()
    deadlines = Group()
    settings.create_session(screen, deadlines)
    logs = Logs()
    score = Score(screen, logs)

    while True:
        settings.actions(screen, programmer, redbulls)
        if logs.continue_game:
            programmer.get_programmer_position()
            redbulls.update()
            settings.refresh_screen(bg_color, screen, logs, score, programmer, deadlines, redbulls)
            settings.remove_redbulls(screen, logs, score, deadlines, redbulls)
            settings.update_session(logs, screen, programmer, deadlines, redbulls)
            score.show_score()


launch()

