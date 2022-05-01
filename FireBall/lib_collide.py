# функция пересечение спрайтов
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