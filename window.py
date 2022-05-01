import pygame
window = pygame.display.set_mode((640,480))
game = True
while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
pygame.quit()