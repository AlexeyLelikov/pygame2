import pygame
from class_of_game import Const,Player,Fireball
# Анимация Героя
ImgPlayerGoR = [pygame.image.load('GoAnim/b1.png'),
               pygame.image.load('GoAnim/b2.png'),
               pygame.image.load('GOAnim/b3.png'),
               pygame.image.load('GOAnim/b4.png'),
               pygame.image.load('GOAnim/b5.png')]
ImgPlayerGoL = []
for img in ImgPlayerGoR:
    ImgPlayerGoL.append(pygame.transform.flip(img,True,False))
# Анимация Fireball
ImgFireBall = [pygame.image.load('GoAnim/fireball.png'),
               pygame.image.load('GoAnim/fireball1.png'),
               pygame.image.load('GOAnim/fireball2.png'),
               pygame.image.load('GOAnim/fireball3.png')]
for i in range(len(ImgFireBall)):
    scale = pygame.transform.scale(ImgFireBall[i],(180,65))
    ImgFireBall[i] = pygame.transform.rotate(scale,-90)
clock = pygame.time.Clock()
g = Const(1)
w = pygame.display.set_mode((1200,700))
GroupFireBall = pygame.sprite.Group()
player = Player('GoAnim/b1.png',550,600,5,ImgPlayerGoL,ImgPlayerGoR)
Fb = Fireball('GoAnim/fireball.png',ImgFireBall,GroupFireBall)
Fb2 = Fireball('GoAnim/fireball.png',ImgFireBall,GroupFireBall)
game = True
while (game):
    clock.tick(15)
    for ev in pygame.event.get(): # выход из игры
        if ev.type == pygame.QUIT:
            game = False
    GroupFireBall.update(g)
    keys = pygame.key.get_pressed()
    player.update(keys,GroupFireBall)
    w.fill((0,0,0))
    w.blit(player.image,player.rect)
    GroupFireBall.draw(w)
    if player.game == False:
        game = False
    pygame.display.update()
pygame.quit()




