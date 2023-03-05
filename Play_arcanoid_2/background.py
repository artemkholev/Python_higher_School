import pygame

class Background(pygame.sprite.Sprite):
    '''фон'''
    def __init__(self, screen):
        '''создаём фон'''
        self.screen = screen
        self.image = pygame.image.load('photo/fon.jpg')
        self.rect = self.image.get_rect()

    def draw_background(self):
        '''отрисовка фона'''
        self.screen.blit(self.image, self.rect)