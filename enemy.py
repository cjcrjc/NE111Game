import pygame
# SSL made a basic Enemy, didn't do much, but wanted to set the health
from pygame import *
from constants import *
from wall import *
from random import *


class Enemy(sprite.Sprite):

    # initiallizing the enemy
    def __init__(self, group, x, y, ss):
        super().__init__(group)
         # Animations arrays
        self.anim_step = 2
        self.down_anim = ss.load_strip((SSTILESIZE * 4, SSENEMYLOCATION*SSTILESIZE, SSTILESIZE, SSTILESIZE), 2, colorkey=BLACK)
        self.down_anim.append(ss.image_at((0, SSENEMYLOCATION*SSTILESIZE, SSTILESIZE, SSTILESIZE), colorkey=BLACK))
        self.up_anim = ss.load_strip((SSTILESIZE * 6, SSENEMYLOCATION*SSTILESIZE, SSTILESIZE, SSTILESIZE), 2, colorkey=BLACK)
        self.up_anim.append(ss.image_at((SSTILESIZE, SSENEMYLOCATION*SSTILESIZE, SSTILESIZE, SSTILESIZE), colorkey=BLACK))
        self.right_anim = ss.load_strip((SSTILESIZE * 8, SSENEMYLOCATION*SSTILESIZE, SSTILESIZE, SSTILESIZE), 2, colorkey=BLACK)
        self.right_anim.append(ss.image_at((SSTILESIZE*2, SSENEMYLOCATION*SSTILESIZE, SSTILESIZE, SSTILESIZE), colorkey=BLACK))
        self.left_anim = [transform.flip(self.right_anim[0], True, False), transform.flip(self.right_anim[1], True, False), transform.flip(self.right_anim[2], True, False)]
        self.animation = [self.up_anim, self.down_anim, self.right_anim, self.left_anim]

        # here is where we define character graphics for now its basic
        self.image = transform.scale(self.down_anim[self.anim_step], (TILESIZE, TILESIZE))
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

        self.rect = self.image.get_rect()
        self.rect.topleft = (x * SSTILESIZE, y * SSTILESIZE)

        # SSL Adding Player characteristics
        self.type = randint(0, 2)
        self.mob_type = TYPES_OF_MOBS[self.type]
        self.max_health = self.mob_type[MOB_HEALTH]
        self.health = self.max_health
        self.hit_rate = self.mob_type[MOB_HIT_RATE]
        self.damage = self.mob_type[MOB_DAMAGE]
        self.health_bar = None
        self.can_attack = True

        # Fill in later
#SSL rectangles around enemy sprites
    def make_cam_pos(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def draw_health(self, targets_dir):
        if targets_dir.value == 0:
            opposite_dir = 1
        elif targets_dir.value == 1:
            opposite_dir = 0
        elif targets_dir.value == 2:
            opposite_dir = 3
        else:
            opposite_dir = 2
        self.image = transform.scale(self.animation[opposite_dir][self.anim_step], (TILESIZE, TILESIZE))
        if self.health > 70:
            col = GREEN
        elif self.health > 40:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.health/self.max_health)
        if width == 0:
            width += 1
        self.health_bar = Rect(-3, 0, width, 5)
        draw.rect(self.image, col, self.health_bar)

    # SSL enemy damage function
    def take_damage(self, damage):
        if damage >= self.health:
            self.health = 0
        else:
            self.health -= damage

    # SSL enemy death function
    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

