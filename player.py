from pygame import *
from constants import *
from enemy import *
from wall import *

class Player(sprite.Sprite):


    # initiallizing the player
    def __init__(self, group, x, y):
        super().__init__(group)
        #here is where we define character graphics for now its basic
        self.image = image.load("Characters_V3_Colour.png").convert_alpha()
        self.x = x + 0.25
        self.y = y + 0.25
        self.dx = 0
        self.dy = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILESIZE/2, y * TILESIZE/2)

        # SSL Adding Player characteristics
        self.health = PLAYERHEALTH

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

# SSL
# when player and enemy are within certain distance, freeze both and make them fight each other
    def should_start_battle(self, enemy):
        # Detect proximity with enemy to decide if battle starts
        return False

    #SSL
    def take_damage(self, damage):
        if (damage >= self.health):
            self.damage = 0
        else:
            self.health - damage

    #SSL
    def is_dead(self):
        if self.health == 0:
            return True
        else:
            return False
