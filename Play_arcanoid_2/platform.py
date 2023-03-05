import pygame
from pygame.sprite import Sprite

class Platform(Sprite):
    '''инициализация платформы'''
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('photo/platform.png')
        self.rect = self.image.get_rect()
        self.rect_screen = screen.get_rect()
        self.rect.centerx = self.rect_screen.centerx
        self.center_screen = float(self.rect.centerx)
        self.rect.bottom = self.rect_screen.bottom - 40
        self.m_right = False
        self.m_left = False
        self.speed_platform = 1.5

    def draw_platform(self):
        '''отрисовка платформы'''
        self.screen.blit(self.image, self.rect)

    def update_platform(self):
        if self.m_right and self.rect_screen.right > self.rect.right:
            self.center_screen += self.speed_platform
        elif self.m_left and self.rect_screen.left < self.rect.left:
            self.center_screen -= self.speed_platform
        self.rect.centerx = self.center_screen

