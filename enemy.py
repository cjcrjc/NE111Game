
# SSL made a basic Enemy, didn't do much, but wanted to set the health
from pygame import *
from constants import *
from wall import *

class Enemy(sprite.Sprite):

    # initiallizing the enemy
    def __init__(self, group, x, y):
        super().__init__(group)

        # SSL Adding Player characteristics
        self.health = ENEMYHEALTH

        # Fill in later

