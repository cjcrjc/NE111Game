from pygame import *
from constants import *


# CC
class SpriteSheet(object):
    def __init__(self, filename):
        self.sheet = image.load(filename)

    # Load a specific image from a specific rectangle
    def load_single_image(self, rectangle, colorkey=BLACK):
        # Loads image from x,y,x+offset,y+offset
        sprite_rect = Rect(rectangle)
        sprite_image = Surface(sprite_rect.size).convert()
        sprite_image.blit(self.sheet, (0, 0), sprite_rect)
        if colorkey is not None:
            sprite_image.set_colorkey(colorkey)
        return sprite_image

    # Load a whole strip of images
    def load_multi_image(self, rect, image_count, colorkey=BLACK):
        # Loads a strip of images and returns them as a list
        rect_collection = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return [self.load_single_image(sprite_rect, colorkey) for sprite_rect in rect_collection]


