import pygame

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
    def __init__(self,img,x,y,speed):
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = speed
w = pygame.display.set_mode((900,600))
player = Sprite('GoAnim/b1.png',100,100,10)
tree = Sprite("tree.png",250,100,0)
tree.image = pygame.transform.scale(tree.image,(200,150))
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
    for ev in pygame.event.get():  # выход из игры
        if ev.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: # событие нажатия кнопки вправо
        player.rect.x += player.speed
        player.image = ImgPlayerGoR[Ncadr % 5]
    if keys[pygame.K_LEFT]:
        player.rect.x -= player.speed
        player.image = ImgPlayerGoL[Ncadr % 5]  # событие нажатия кнопки влево
    if collide(player.rect,tree.rect):
        tree.image = pygame.image.load('GoAnim/b1.png')
    w.fill((0,0,0))
    w.blit(player.image,player.rect)
    w.blit(tree.image,tree.rect)
    Ncadr += 1
    pygame.display.update()
pygame.quit()