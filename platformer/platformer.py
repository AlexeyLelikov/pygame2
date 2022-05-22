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
    def __init__(self,x,y,img,speed,Anim):
        super().__init__(x,y,img)
        self.speed = speed
        self.imgGoAnim = Anim
        self.cadr = 0


