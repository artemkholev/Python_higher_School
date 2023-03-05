import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen):
        '''инициализация мяча'''
        self.screen = screen
        self.rect_screen = screen.get_rect()
        self.image = pygame.image.load('photo/ball1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height + int(self.rect_screen.bottom / 2) - 100
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed_x = random.uniform(0.8, 1)
        self.speed_y = random.uniform(0.8, 1)
        self.music_bom = pygame.mixer.Sound('музыка/столкновение.wav')

    def draw_ball(self):
        '''отрисовка мяча'''
        self.screen.blit(self.image, self.rect)

    def update_ball(self, lose):
        if self.rect.bottom >= self.rect_screen.bottom - 12:
            lose.lose = False
            self.x = self.rect.width
            self.y = self.rect.height + int(self.rect_screen.bottom / 2) - 100
        if self.rect.left <= self.rect_screen.left or self.rect.right >= self.rect_screen.right:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1
        self.x += (self.speed_x)
        self.y += (self.speed_y)
        self.rect.x = self.x
        self.rect.y = self.y

    def pos_ball_first(self):
        self.x = self.rect.width + 100
        self.y = self.rect.height + int(self.rect_screen.bottom / 2) - 80
        self.speed_x = random.uniform(0.8, 1)
        self.speed_y = random.uniform(0.8, 1)