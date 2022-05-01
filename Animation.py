import pygame
class Sprite:
    def __init__(self,img,x,y,speed):
        self.image = pygame.image.load(img)
        self.x = x
        self.y = y
        self.speed = speed
w = pygame.display.set_mode((900,600))
player = Sprite('GoAnim/b1.png',100,100,10)
ImgPlayerGoR = [pygame.image.load('GoAnim/b1.png'),
               pygame.image.load('GoAnim/b2.png'),
               pygame.image.load('GOAnim/b3.png'),
               pygame.image.load('GOAnim/b4.png'),
               pygame.image.load('GOAnim/b5.png')]
ImgPlayerGoL = []
for img in ImgPlayerGoR:
    ImgPlayerGoL.append(pygame.transform.flip(img,True,False))
Ncadr = 0
clock = pygame.time.Clock()
game = True
while game:
    clock.tick(15)
    for ev in pygame.event.get(): # выход из игры
        if ev.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: # событие нажатия кнопки вправо
        player.x += player.speed
        player.image = ImgPlayerGoR[Ncadr % 5]
    if keys[pygame.K_LEFT]:
        player.x -= player.speed
        player.image = ImgPlayerGoL[Ncadr % 5]  # событие нажатия кнопки влево
    w.fill((0,0,0))
    rect = pygame.Rect((player.x,player.y),(64,84))
    w.blit(player.image,rect)
    Ncadr += 1
    pygame.display.update()
pygame.quit()