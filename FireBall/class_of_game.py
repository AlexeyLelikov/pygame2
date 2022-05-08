import pygame
import lib_collide
import random

class Sprite(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft=(x, y))
class Player(Sprite):
    def __init__(self,img,x,y,speedx,GoL,GoR):
        Sprite.__init__(self,img,x,y)
        self.animGoR = GoR
        self.animGoL = GoL
        self.speedx = speedx
        self.cadr = 0
        self.game = True
    def update(self,keys,GroupFireball):
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speedx
            self.image = self.animGoR[self.cadr % 5]
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speedx
            self.image = self.animGoL[self.cadr % 5]
        if lib_collide.collideG(self.rect,GroupFireball):
            self.game = False
        self.cadr += 1

class Const():
    def __init__(self,value):
        self.value = value

class Fireball(Sprite):
    def __init__(self,img, Anim, group):
        Sprite.__init__(self,img,random.randint(0,1200),0)
        self.anim = Anim
        self.speedy = 1
        self.cadr = 0
        self.add(group)
    def update(self,g):
        if self.rect.y < 700:
            self.speedy = self.speedy + g.value
            self.rect.y = self.rect.y + self.speedy
        else:
            self.rect.y = 0
            self.rect.x = random.randint(0,1200)
            self.speedy = 1
        self.image = self.anim[self.cadr % 4]
        self.cadr += 1

















