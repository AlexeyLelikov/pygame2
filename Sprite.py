import pygame # импорт библиотеки
class Sprite: # Создаем Класс
    def __init__(self,x,y,img): # конструктор класса
        self.x = x
        self.y = y
        self.image = pygame.image.load(img)
        self.speed = 1
window = pygame.display.set_mode((720,480)) # создаем окно
player = Sprite(100,100,'player.png') # создаем экземляр класса(объект) Sprite
game = True
while game: # Игровой цикл
    for ev in pygame.event.get(): # выход из игры
        if ev.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: # событие нажатия кнопки вправо
        player.x += player.speed
    if keys[pygame.K_LEFT]:
        player.x -= player.speed # событие нажатия кнопки влево
    if keys[pygame.K_UP]: # событие нажатия кнопки вверх
        player.y -= player.speed
    if keys[pygame.K_DOWN]:
        player.y += player.speed # событие нажатия кнопки вниз
    window.fill((0,0,0)) # заливка окна в белый цвет
    window.blit(player.image,(player.x,player.y),(64,84)) # отрисовка поверхности игрока на окне
    pygame.display.update()
pygame.quit()
