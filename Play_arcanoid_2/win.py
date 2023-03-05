import pygame

class Win(pygame.sprite.Sprite):
    '''инициализация фона для выигрыша'''
    def __init__(self, screen):
        self.screen = screen
        self.imege = pygame.image.load('photo/win.jpg')
        self.rect = self.imege.get_rect()
        self.win = False

    def draw_fon_win(self):
        self.screen.blit(self.imege, self.rect)