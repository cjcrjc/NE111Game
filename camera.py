from pygame import *
from constants import *


# CC
class CameraGroup(sprite.Group):
    # initializes sprite group
    def __init__(self):
        super().__init__()
        # making offset vector that will allow for camera to follow player
        self.offset = math.Vector2()

    def custom_draw(self, target):
        # offset is adjusted every frame to make player in center
        self.offset.x = target.rect.centerx - SCREENWIDTH/2
        self.offset.y = target.rect.centery - SCREENHEIGHT/2
        # for each sprite you draw it but at the offset position to keep everything in fixed position relative to each other
        for member in sorted(self.sprites(), key=lambda member: member.rect.centery):
            offset_pos = member.rect.topleft - self.offset
            display.get_surface().blit(member.image, offset_pos)

    def draw_grid(self):
        # draws x and y lines separated by tile size
        for x in range(0, SCREENWIDTH, TILESIZE):
            draw.line(display.get_surface(), GREY, (x - self.offset.x, 0), (x - self.offset.x, SCREENHEIGHT))
        for y in range(0, SCREENHEIGHT, TILESIZE):
            draw.line(display.get_surface(), GREY, (0, y - self.offset.y), (SCREENWIDTH, y - self.offset.y))
