import pygame

class Lose(pygame.sprite.Sprite):
    def __init__(self, screen):
        '''инициализация проигрыша'''
        self.screen = screen
        self.image = pygame.image.load('photo/lose2.png')
        self.rect = self.image.get_rect()
        self.lose = False


    def draw_lose(self):
        self.screen.blit(self.image, self.rect)
        self.lose = False

    def play_lose(self):
        self.lose = True