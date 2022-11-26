#this file is all under SK (Sam Krysko) for now.

#imports needed for map creation and for reading tilemap files
#import pytmx to manipulate and interpret the tilemap files 
#being used for the game map
from pytmx import *

#create a map class that loads the .tmx map files from
#Tiled, the tilemap editor and creator.
class TiledMap:
    def __init__(self, filename):
        #this function initializes the map file, and the variable (tm)
        #created loads the .tmx map file with pygame.
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        #set the size of the map, which is 100 tiles * 16 pixels/tile
        self.width = tm.width * tm.tilewidth
        #set the tile height of the map, which is 80 tiles * 16 pixels/tile
        self.height = tm.height * tm.tileheight
        #create a variable to store this initialization
        self.tmxdata = tm
    
    def render(self, surface):
        #this function will take the map .tmx file and read the .txt file
        #first, make a variable for taking a tile by its global id, less writing
        ti = self.tmxdata.get_tile_image_by_gid
        #run through each visible layer in the .tmx file
        for layer in self.tmxdata.visible.layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                #run through each tile in the layer
                for x, y, gid, in layer:
                    tile = ti(gid)
                    #if the tile is a visible tile, we draw it
                    if tile:
                        surface.blit(tile, (x*self.tmx.tilewidth, y*self.tmx.tileheight))

    #make a final function in the class to make the map as temp_surface variable
    def make_map(self):
        temp_surface = pg.Surface((self.width,self.height))
        self.render(temp_surface)
        return temp_surface