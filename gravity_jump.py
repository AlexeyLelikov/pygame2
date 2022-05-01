import pygame
Screen_width = 900
Screen_height = 600
# класс родитель
def collide(Sprite1, Sprite2):
    if ((     Sprite1.x <=  Sprite2.x  <= Sprite1.x + Sprite1.width
        and   Sprite1.y <= Sprite2.y <= Sprite1.y + Sprite1.height)
        or   (Sprite1.x <= Sprite2.x + Sprite2.width  <= Sprite1.x + Sprite1.width
        and   Sprite1.y <= Sprite2.y + Sprite2.height <= Sprite1.y + Sprite1.height)
        or   (Sprite2.x <= Sprite1.x + Sprite1.width  <= Sprite2.x + Sprite2.width
        and   Sprite2.y <= Sprite1.y <= Sprite2.y + Sprite2.height)
        or   (Sprite2.x <= Sprite1.x <= Sprite2.x + Sprite2.width
        and   Sprite2.y <= Sprite1.y + Sprite1.height <= Sprite2.y + Sprite2.height)):
        return  True
    else:
        return False
class Sprite:
    def __init__(self,img,x,y):
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft=(x, y))
class Player(Sprite):
    def __init__(self,img,x,y,speedx):
        Sprite.__init__(self,img,x,y)
        self.speedx = speedx
        self.speedy = 0
        self.jump = 5
class Platform(Sprite):
    def __init__(self,img,x,y,speedy):
        Sprite.__init__(self, img, x, y)
        self.image = pygame.transform.scale(self.image,(500,150))
        self.speedy = speedy
class Const:
    def __init__(self,value):
        self.value = value
# Объекты
w = pygame.display.set_mode((Screen_width,Screen_height))
pl = Platform("ground.png",300,300,5)
player = Player('GoAnim/b1.png',300,150,2)
g = Const(1)
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
Timer = 0
while game:
    clock.tick(15)
    for ev in pygame.event.get():  # выход из игры
        if ev.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: # событие нажатия кнопки вправо
        player.rect.x += player.speedx
        player.image = ImgPlayerGoR[Ncadr % 5]
    if keys[pygame.K_LEFT]:
        player.rect.x -= player.speedx
        player.image = ImgPlayerGoL[Ncadr % 5]  # событие нажатия кнопки влево
    if keys[pygame.K_SPACE]:
        player.speedy -= player.jump
    if collide(player.rect, pl.rect):
        if player.speedy > 0:
            player.speedy = 0
        Timer += 1
        if Timer > 75:
           pl.rect.y += pl.speedy
    else:
        player.speedy += g.value
    player.rect.y += player.speedy
    w.fill((0,0,0))
    w.blit(player.image,player.rect)
    w.blit(pl.image, pl.rect)
    Ncadr += 1
    pygame.display.update()
pygame.quit()



