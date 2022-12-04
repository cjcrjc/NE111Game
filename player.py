import pygame
from pygame import *
from constants import *
from enemy import *
from wall import *
from enum import Enum

#SSL if puffy player touches any enemy
def test_collision(sprite1, sprite2):
    if sprite1 != sprite2:
        collide_rect = sprite1.rect.inflate(TILESIZE*2, TILESIZE*2)
        return sprite2.colliderect(collide_rect)
    else:
        return False
class Direction(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3


class Player(sprite.Sprite):
    # initiallizing the player
    def __init__(self, group, x, y, ss):
        super().__init__(group)
        # Animations arrays
        self.anim_step = 0
        self.down_anim = ss.load_strip((SSTILESIZE * 4, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), 2, colorkey=BLACK)
        self.down_anim.append(ss.image_at((0, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), colorkey=BLACK))
        self.up_anim = ss.load_strip((SSTILESIZE * 6, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), 2, colorkey=BLACK)
        self.up_anim.append(ss.image_at((SSTILESIZE, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), colorkey=BLACK))
        self.right_anim = ss.load_strip((SSTILESIZE * 8, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), 2, colorkey=BLACK)
        self.right_anim.append(ss.image_at((SSTILESIZE*2, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), colorkey=BLACK))
        self.left_anim = [transform.flip(self.right_anim[0], True, False), transform.flip(self.right_anim[1], True, False), transform.flip(self.right_anim[2], True, False)]
        self.animation = [self.up_anim, self.down_anim, self.right_anim, self.left_anim]

        # here is where we define character graphics for now its basic
        self.image = transform.scale(self.down_anim[self.anim_step], (TILESIZE, TILESIZE))
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.direction = Direction.DOWN
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * SSTILESIZE, y * SSTILESIZE)

        # SSL Adding Player characteristics
        self.health = PLAYERHEALTH

    # checks for collisions between player and wall sprites in future direction
    def check_collide(self):
        for thing in self.groups()[0]:
            if isinstance(thing, Wall) and (thing.x == self.x + self.dx and thing.y == self.y + self.dy):
                return True
        return False

    # makes the player coordinates into actual sprite properties
    def make_cam_pos(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    # self-explanatory
    def move(self):
        self.x += self.dx
        self.y += self.dy

    # SSL
    # when player and enemy are within certain distance, freeze both and make them fight each other
    def should_start_battle(self, all_enemies):
        # Detect proximity with enemy to decide if battle starts
        enemy = pygame.sprite.spritecollideany(self, all_enemies, collided=test_collision)
        return enemy

    # SSL
    def take_damage(self, damage):
        if (damage >= self.health):
            self.damage = 0
        else:
            self.health - damage

    # SSL
    def is_dead(self):
        if self.health == 0:
            return True
        else:
            return False
