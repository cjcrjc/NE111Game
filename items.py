from pygame import *
from constants import *


class Heal(sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = image.load("Heal Potion.png")
        self.image = transform.scale(self.image, (TILESIZE/2, TILESIZE/2))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x * TILESIZE, y * TILESIZE)

    def test_collision(self, sprite2):
        if self != sprite2:
            collide_rect = self.rect.inflate(TILESIZE / 4, TILESIZE / 4)
            return sprite2.rect.colliderect(collide_rect)
        else:
            return False