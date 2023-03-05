import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)

class Enemy(pygame.sprite.Sprite):
    '''инициализация монстров'''
    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('photo/enemy1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_enemy(self):
        '''отрисовка монстра'''
        self.screen.blit(self.image, self.rect)