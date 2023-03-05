import pygame, sys, controls
from ball import Ball
from lose import Lose
from win import Win
from enemy import Enemy
import time

def events(platform, tab_play, screen, enemy_s, win, ball, lose):
    '''обработка событий'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if tab_play.collidepoint(x, y):
                    play_first(screen, enemy_s, win, lose, ball)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                '''вправо'''
                platform.m_right = True
            if event.key == pygame.K_LEFT:
                '''влево'''
                platform.m_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                '''вправо'''
                platform.m_right = False
            if event.key == pygame.K_LEFT:
                '''влево'''
                platform.m_left = False

def play_first(screen, enemy_s, win, lose, ball):
    lose.play_lose()
    controls.drawing_monsters_on_the_screen(screen, enemy_s)
    ball.pos_ball_first()
    win.win = False

def update_film(screen, background, platform, ball, lose, enemys):
    '''обновление экрана'''
    if lose.lose == False:
        '''проигрышь'''
        lose.draw_lose()
        pygame.display.flip()
        time.sleep(1)
    if lose.lose == True:
        '''игровой процесс'''
        background.draw_background()
        platform.draw_platform()
        ball.draw_ball()
        enemys.draw(screen)
        pygame.display.flip()

def lose(fon, tab_play):
    '''начальная заставка игры'''
    fon.draw_fon()
    tab_play.draw_tab_play()
    pygame.display.flip()

def win_fon(enemy_s, win):
    '''отрисовка выигрыша'''
    if len(enemy_s) == 0:
        win.draw_fon_win()
        pygame.display.flip()
        time.sleep(2)
        win.win = True

def update_ball_in_film(ball, platform, lose):
    '''обновление позиции мяча'''
    ball.update_ball(lose)
    colisions_platfom = pygame.sprite.collide_mask(platform, ball)
    if colisions_platfom:
        ball.speed_y *= -1

def drawing_monsters_on_the_screen(screen, enemy_s):
    '''создание монстров на экране ряды'''
    enemy = Enemy(screen)
    number_enemy_x = (800 // (enemy.rect.width))
    number_enemy_y = 3
    for y in range(number_enemy_y):
        # for x in range(1):
        for x in range(number_enemy_x - y * 2 - 9):
            enemy = Enemy(screen)
            enemy.x = x * 65 + enemy.rect.width * y + 20
            enemy.y = y * enemy.rect.height + 15 + y * 4
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.y
            enemy_s.add(enemy)

def update_enemy_s(ball, enemy_s):
    '''обновлкние мрнстров, чбирает если произошло столкновение'''
    colisions_enemy = pygame.sprite.spritecollide(ball, enemy_s, True)
    if colisions_enemy:
        ball.speed_y *= - 1
        ball.music_bom.play()