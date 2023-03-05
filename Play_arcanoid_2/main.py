import pygame, controls
import sys
from background import Background
from platform import Platform
from ball import Ball
from pygame.sprite import Group
from lose import Lose
from fon1 import *
from win import Win

def run_game(play):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption('Арканоид')
    background = Background(screen)
    platform = Platform(screen)
    ball = Ball(screen)
    lose = Lose(screen)
    fon = Fon(screen)
    tab_play = Tab_play(screen)
    enemy_s = Group()
    win = Win(screen)


    while play:
        controls.events(platform, tab_play, screen, enemy_s, win, ball, lose)
        if lose.lose and win.win == False:
            platform.update_platform()
            controls.update_ball_in_film(ball, platform, lose)
            controls.win_fon(enemy_s, win)
            controls.update_enemy_s(ball, enemy_s)
            controls.update_film(screen, background, platform, ball, lose, enemy_s)
        elif lose.lose == False or win.win == True:
            controls.lose(fon, tab_play)

play = True
run_game(play)
