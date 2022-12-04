
# SSL made a basic Enemy, didn't do much, but wanted to set the health
from pygame import *
from constants import *
from wall import *

# SSL random mob generator basically
def get_mob_type():
    from random import seed
    from random import randint
    seed(1)
    return randint(0, 2)


class Enemy(sprite.Sprite):

    # initiallizing the enemy
    def __init__(self, group, x, y, ss, type):
        super().__init__(group)
         # Animations arrays
        self.anim_step = 2
        self.down_anim = ss.load_strip((SSTILESIZE * 4, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), 2, colorkey=BLACK)
        self.down_anim.append(ss.image_at((0, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), colorkey=BLACK))
        self.up_anim = ss.load_strip((SSTILESIZE * 6, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), 2, colorkey=BLACK)
        self.up_anim.append(ss.image_at((SSTILESIZE, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), colorkey=BLACK))
        self.right_anim = ss.load_strip((SSTILESIZE * 8, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), 2, colorkey=BLACK)
        self.right_anim.append(ss.image_at((SSTILESIZE*2, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), colorkey=BLACK))
        self.left_anim = [transform.flip(self.right_anim[0], True, False), transform.flip(self.right_anim[1], True, False), transform.flip(self.right_anim[2], True, False)]
        self.animation = [self.up_anim, self.down_anim, self.right_anim, self.left_anim]

        # here is where we define character graphics for now its basic
        # here is where we define character graphics for now its basic
        self.image = transform.scale(self.down_anim[self.anim_step], (TILESIZE, TILESIZE))
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

        self.rect = self.image.get_rect()
        self.rect.topleft = (x * SSTILESIZE, y * SSTILESIZE)


        # SSL Adding Player characteristics
        self.mob_type = TYPES_OF_MOBS[type]
        self.health = self.mob_type[MOB_HEALTH]
        self.hit_rate = self.mob_type[MOB_HIT_RATE]
        self.damage = self.mob_type[MOB_DAMAGE]

        # Fill in later

    def make_cam_pos(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    # SSL
    def take_damage(self, damage):
        if damage >= self.health:
            self.health = 0
        else:
            self.health = self.health - damage
            test = True

    # SSL
    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

