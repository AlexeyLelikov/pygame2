import pygame
import random
import lib_collide
WorldWidth = 1800 # ширина игрового мира
WorldHeight = 1200 # высота игрового мира
ScreenWidth = 900 # ширина окна программы
ScreenHeight = 600 # высота окна программы


class Camera:
    def __init__(self):
       self.x = 0
       self.y = 900
    def update(self,sprite):
        if sprite.rect.x < WorldWidth - ScreenWidth / 2 and sprite.rect.x > ScreenWidth / 2:
            self.x = int(ScreenWidth / 2) - sprite.rect.x
        if sprite.rect.y < WorldHeight- ScreenHeight / 2 and sprite.rect.y > ScreenHeight / 2:
            self.y = int(ScreenHeight / 2) - sprite.rect.y

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft = (x, y))

class Player(Sprite):
    def __init__(self, x, y, img, speed):
        super().__init__(x, y, img)
        self.speed = speed
        self.cadr = 0
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:  # событие нажатия кнопки вправо
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed  # событие нажатия кнопки влево
        if keys[pygame.K_UP]:  # событие нажатия кнопки вверх
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed  # событие нажатия кнопки вниз

w = pygame.display.set_mode((ScreenWidth,ScreenHeight))
world = pygame.Surface((WorldWidth,WorldHeight))
player = Player(900,600,'player.png',3)
camera = Camera()
BG_image = pygame.image.load('bg.jpg')
BG_image = pygame.transform.scale(BG_image,(1800,1200))
game = True
while game:
    for ev in pygame.event.get():  # выход из игры
        if ev.type == pygame.QUIT:
            game = False
    player.update()
    camera.update(player)
    world.fill((0,0,0))
    world.blit(BG_image,(0,0))
    world.blit(player.image,player.rect)
    w.blit(world,(camera.x,camera.y))
    pygame.display.update()
pygame.quit()




