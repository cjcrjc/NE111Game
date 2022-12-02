
# SSL made a basic Enemy, didn't do much, but wanted to set the health
from pygame import *
from constants import *
from wall import *

class Enemy(sprite.Sprite):

    # initiallizing the enemy
    def __init__(self, group, x, y, type):
        super().__init__(group)
        #here is where we define character graphics for now its basic
        self.image = Surface((16, 16))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * 16, y * 16)
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

        # SSL Adding Player characteristics
        self.mob_type = TYPES_OF_MOBS[type]
        self.health = self.mob_type[MOB_HEALTH]
        self.hit_rate = self.mob_type[MOB_HIT_RATE]
        self.damage = self.mob_type[MOB_DAMAGE]

        # Fill in later

#SSL random mob generator basically
def get_mob_type():
    from random import seed
    from random import randint
    seed(1)
    return randint(0, 2)

#SSL
def take_damage(damage):
    if (damage >= self.health):
        self.damage = 0
    else:
        self.health - damage

#SSL
def is_dead():
    if self.health = 0:
        return True
    else:
        return False
