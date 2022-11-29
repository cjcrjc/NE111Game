#this file is all under SK (Sam Krysko) for now

#imports needed for map creation and for reading tilemap files
#import pytmx to manipulate and interpret the tilemap files
#being used for the game map
from pytmx import *
from constants import *
from pygame import *
from main import *
from camera import *

#create a map class that loads the .tmx map files from
#Tiled, the tilemap editor and creator.

def blit_all_tiles(Display,tmxdata,offset_pos):
    #blits the map using the display(screen), pytmx module for loading .tmx files, and the camera position
    for layer in tmxdata:
        for tile in layer.tiles():
            #tile[0] is the x location on the gird
            #tile[1] is the y location
            #tile[2] is the image data for blitting
            x_pixel = tile[0] * TILESIZE + offset_pos[0]
            y_pixel = tile[1] * TILESIZE + offset_pos[1]
            Display.blit(tile[2], (x_pixel,y_pixel))

