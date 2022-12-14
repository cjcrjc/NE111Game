from wall import *
from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3


# CC
class Player(sprite.Sprite):
    # initializing the player
    def __init__(self, group, x, y, ss):
        super().__init__(group)
        # Animations arrays
        self.anim_step = 0
        self.down_anim = ss.load_multi_image((SSTILESIZE * 4, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), 2)
        self.down_anim.append(ss.load_single_image((0, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE)))
        self.up_anim = ss.load_multi_image((SSTILESIZE * 6, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), 2)
        self.up_anim.append(ss.load_single_image((SSTILESIZE, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE)))
        self.right_anim = ss.load_multi_image((SSTILESIZE * 8, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE), 2)
        self.right_anim.append(ss.load_single_image((SSTILESIZE * 2, SSPLAYERLOCATION, SSTILESIZE, SSTILESIZE)))
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
        self.damage = PLAYERHITDMG
        self.health_bar = None

    # makes the player coordinates into actual sprite properties
    def make_cam_pos(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    # self-explanatory
    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw_health(self):
        if self.health > 100:
            self.health = 100
        if self.health > 70:
            col = GREEN
        elif self.health > 40:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.health/100)
        self.health_bar = Rect(0, 0, width, 5)
        draw.rect(self.image, col, self.health_bar)

    # SSL
    # when player and enemy are within certain distance, freeze both and make them fight each other
    def should_start_battle(self, target):
        # Detect proximity with enemy to decide if battle starts
        engaged_enemy = sprite.spritecollideany(self, target, collided=self.test_collision)
        return engaged_enemy

    # SSL, debugged by SSL
    def take_damage(self, damage):
        if damage >= self.health:
            self.health = 0
        else:
            self.health = self.health - damage

    # SSL, debugged by SSL
    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

    # checks for collisions between player and wall sprites in future direction
    def check_collide(self):
        for thing in self.groups()[0]:
            if isinstance(thing, Wall) and (thing.x == self.x + self.dx and thing.y == self.y + self.dy):
                return True
        return False

    # SSL if puffy player touches any enemy
    def test_collision(self, sprite2):
        if self != sprite2:
            collide_rect = self.rect.inflate(TILESIZE * 2, TILESIZE * 2)
            return sprite2.rect.colliderect(collide_rect)
        else:
            return False
