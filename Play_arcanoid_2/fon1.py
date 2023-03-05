import pygame

class Fon():
    def __init__(self, screen):
        '''фон начала игры'''
        self.screen = screen
        self.image = pygame.image.load('photo/fon1.jpg')
        self.rect = self.image.get_rect()

    def draw_fon(self):
        self.screen.blit(self.image, self.rect)

class Tab_play():
    '''кнопка плэй'''
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('photo/press play.png')
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

    def draw_tab_play(self):
        self.screen.blit(self.image, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
