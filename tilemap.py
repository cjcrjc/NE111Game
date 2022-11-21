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
        #this function will take the map .tmx file and read the txt file
        pass