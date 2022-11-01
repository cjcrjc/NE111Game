from pygame import *
from constants import *

class Player(sprite.Sprite):
    def __init__(self):
        super().__init__()
        #here is where we define character graphics for now its basic
        self.image = Surface((15,15))
        #self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREENWIDTH/2,SCREENHEIGHT/2)

    def draw(self, output_display):
        output_display.blit(self.image, self.rect)

    def move(self):
        keys_pressed = key.get_pressed()
        if (keys_pressed[K_w] or keys_pressed[K_UP]) and self.rect.y >= 0:
            self.rect.y -= MOVESPEED
        if (keys_pressed[K_s] or keys_pressed[K_DOWN]) and self.rect.y <= (SCREENHEIGHT - self.rect.width):
            self.rect.y += MOVESPEED
        if (keys_pressed[K_a] or keys_pressed[K_LEFT]) and self.rect.x >= 0:
            self.rect.x -= MOVESPEED
        if (keys_pressed[K_d] or keys_pressed[K_RIGHT]) and self.rect.x <= (SCREENWIDTH - self.rect.height):
            self.rect.x += MOVESPEED