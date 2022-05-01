import pygame
window = pygame.display.set_mode((720,480))
player = pygame.image.load('player.png')
player = pygame.transform.scale(player,(80,150))
x = 100
y = 100
game = True
while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    elif keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_UP]:
        y -= 1
    elif keys[pygame.K_DOWN]:
        y += 1
    window.fill((0,0,0,))
    window.blit(player,(x,y))
    pygame.display.update()
pygame.quit()