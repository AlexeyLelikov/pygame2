import pygame
import lib_collide

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
    def update(self,keys,GroupFireball):
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speedx
            self.image = self.animGoR[self.cadr % 5]
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speedx
            self.image = self.animGoL[self.cadr % 5]
        if lib_collide.collideG(self.rect,GroupFireball):
            global game = False

class Fireball(Sprite):
    def __init__(self,img,x,y,seepdy,Anim):
        Sprite.__init__(self,img,x,y)
        self.anim = Anim
        self.speedy = speedy


