import pygame

class Area():
    def __init__(self, x=0, y=0, width=5, hight=5, color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, width, hight)
        self.fill_color = color

    def color(self, newcolor):
        self.fill_color = newcolor

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frime_color, thickness):
        pygame.draw.rect(window, frime_color, self.rect, thickness)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


# Объекты рисунки
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, hight=10):
        super().__init__(x=x, y=y, width=width, hight=hight, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Label(Area):
    def set_text(self, txt, mach=15, coloe=(0, 0, 0)):
        self.image = pygame.font.Font(None, mach).render(txt, True, coloe)

    def pouring(self, s_x=0, s_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + s_x, self.rect.y + s_y))