from pygame import *
from constants import *


# CC
class Damaged(sprite.Sprite):
    def __init__(self, group, x, y, rad):
        super().__init__(group)
        self.image = Surface([rad,rad])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.x = x
        self.y = y
        self.rad = rad

    def update(self):
        self.rad -= 0.05
        if self.rad <= 0:
            self.kill()
