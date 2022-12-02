from pygame import *
from constants import *
from pytmx import *


class CameraGroup(sprite.Group):
    #initiallizes sprite group
    def __init__(self):
        super().__init__()
        #making offect vector that will allow for camera to follow player
        self.offset = math.Vector2()

    def custom_draw(self, target):
        #offset is adjusted every frame to make player in center
        self.offset.x = target.rect.centerx - SCREENWIDTH/2
        self.offset.y = target.rect.centery - SCREENHEIGHT/2
        #for each sprite you draw it but at the offset position to keep everything in fixed position relative to each other
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            display.get_surface().blit(sprite.image, offset_pos)

    def draw_grid(self):
        #draws x and y lines seperated by tilesize
        for x in range(0, SCREENWIDTH, TILESIZE):
            draw.line(display.get_surface(), GREY, (x - self.offset.x, 0), (x - self.offset.x, SCREENHEIGHT))
        for y in range(0, SCREENHEIGHT, TILESIZE):
            draw.line(display.get_surface(), GREY, (0, y - self.offset.y), (SCREENWIDTH, y - self.offset.y))
