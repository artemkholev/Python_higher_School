from random import randint
import pygame
from time import sleep
import sys
import os
# name = input('Введите своё имя: ')
pygame.init()
pygame.mixer.pre_init(44100, -16, 1, 512)
# Фотогафии и музыка
platform = pygame.image.load(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\photo\platform.png')
boll1 = pygame.image.load(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\photo\ball1.png')
enemy = pygame.image.load(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\photo\enemy.png')
fon = pygame.image.load(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\photo\fon.jpg')
fon1 = pygame.image.load(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\photo\fon1.jpg')
pygame.mixer.music.load(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\музыка\музыка.mp3')
name_geymer = pygame.image.load(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\photo\name.png')
f = pygame.font.SysFont('arial', 20)
sound = pygame.mixer.Sound(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\музыка\столкновение.wav')

# Настройка экрана
x = 100
y = 100
os.environ['Sp_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

color = (100, 153, 100)
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dray")
window.blit(fon1, (0, 0))
pygame.display.flip()

clock = pygame.time.Clock()


RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Объекты
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

def play_game():
    window.blit(fon, (0, 0))
    pygame.mixer.music.play(-1, 0.0, 0)
    x = 300
    y = 500
    platform1 = Picture(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\photo\platform.png', x, y, 100, 15)
    boll1 = Picture(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\photo\ball1.png', 190, 220, 35, 35)
    boll2 = Picture(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\photo\ball1.png', 190, 220, 35, 35)
    platform1.draw()
    boll1.draw()

# Создание врагов
    bos = Picture(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\photo\bos.png', 320, 10, 150, 240)
    halth = 10

    s = list()
    hi_ght = 10
    enemy_count = 14
    # enemy_count = 0
    for i in range(4):
        x = 20 + i * 30
        for j in range(enemy_count):
            enemy = Picture(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\photo\enemy.png', x, hi_ght, 55, 45)
            s.append(enemy)
            x += 55
        enemy_count -= 1
        hi_ght += 45
    for i in s:
        i.draw()

    move_right = False
    move_left = False
    flPause = False

    # Скорость
    speed_x = 1.4
    speed_y = 1.4
    p = (randint(2, 4))
    m = (randint(2, 4))

    game = False

    while not game:
        if boll1.rect.y > 520:
            down = Label(0, 0, 800, 600, (230, 25, 55))
            down.set_text('Вы проиграли:(', 70, (0, 0, 0))
            down.pouring(230, 250)
            pygame.mixer.music.stop()
            pygame.display.update()
            sleep(1)
            return

        if len(s) != 0:
            for i in s:
                i.draw()
                if i.rect.colliderect(boll1.rect):
                    s.remove(i)
                    sound.play()
                    window.fill((0, 0, 0))
                    speed_y *= -1

        if len(s) == 0 and halth != 0:
            bos.draw()
            if bos.rect.colliderect(boll1.rect):
                sound.play()
                halth -= 1
                speed_y *= -1
                speed_x *= -1.2


        if len(s) == 0 and halth == 0:
            win = Label(0, 0, 800, 600, (0, 255, 0))
            win.set_text('Вы выиграли!', 70, (0, 0, 0))
            win.pouring(230, 250)
            pygame.mixer.music.stop()
            pygame.display.update()
            sleep(1)
            return

        boll1.rect.x += p * speed_x
        boll1.rect.y += m * speed_y

        if boll1.rect.x > 750 or boll1.rect.x < 4:
            speed_x *= -1
            p = (randint(1, 4))
        if boll1.rect.y < 0:
            speed_y *= -1
        if boll1.colliderect(platform1.rect):
            speed_y *= -1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    move_right = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
        if move_left and platform1.rect.x > 0:
            platform1.rect.x -= 7
        if move_right and platform1.rect.x < 700:
            platform1.rect.x += 7


        window.blit(fon, (0, 0))
        for i in s:
            i.draw()
        if halth != 0 and len(s) == 0:
            bos.draw()
        platform1.draw()
        boll1.draw()

        pygame.display.update()
        clock.tick(60)

    pygame.display.update()
    pygame.quit()

while True:
    press_play = Picture(r'C:\Users\Артем Юрьевич\PycharmProjects\pythonProject5\photo\press play.png', 50, 200, 150, 50)
    window.blit(fon1, (0, 0))
    press_play.draw()
    window.blit(name_geymer, (10, 10))
    text_tabl = f.render('Артём', 1, (0, 0, 0))
    window.blit(text_tabl, (40, 35))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                pygame.draw.circle(
                    window, RED, event.pos, 10)
                pygame.display.update()
                window.blit(fon1, (0, 0))

                if press_play.collidepoint(x, y):
                    play_game()

                pygame.display.update()
            elif event.button == 3:
                pygame.draw.circle(
                    window, BLUE, event.pos, 10)
                pygame.draw.rect(
                    window, GREEN,
                    (event.pos[0] - 5,
                     event.pos[1] - 5,
                     10, 10))
                pygame.display.update()
                window.blit(fon1, (0, 0))
                pygame.display.update()
                sys.exit()
            elif event.button == 2:
                window.fill(WHITE)
                pygame.display.update()

    pygame.time.delay(60)
    pygame.display.update()
