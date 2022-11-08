from pygame import *
from constants import *
from wall import *

class Player(sprite.Sprite):

    # initiallizing the player
    def __init__(self, group, x, y):
        super().__init__(group)
        #here is where we define character graphics for now its basic
        self.image = Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILESIZE, y * TILESIZE)
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    #checks for collisions between player and wall sprites in future direction
    def check_collide(self):
        for object in self.groups()[0]:
            if isinstance(object, Wall) and (object.x == self.x + self.dx and object.y == self.y + self.dy):
                return True
        return False

    # makes the player coordinates into actual sprite properties
    def make_cam_pos(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    #self explanatory
    def move(self):
        self.x += self.dx
        self.y += self.dy
