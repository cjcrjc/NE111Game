#Group is Cameron (CC), Sam (SK), Sophia, (SSL), Dev (DL)

#Imports#
import pygame.event
from pygame import *
from constants import *
from camera import *
from player import *
from wall import *
from os import path
from pytmx import *
from pytmx.util_pygame import load_pygame

#Variable Setup
running = True
init()
Display = display.set_mode((SCREENWIDTH,SCREENHEIGHT))
Display.fill(WHITE)
FPS = time.Clock()
movable_event = USEREVENT + 1
movable = True
camera_group = CameraGroup()
tmxdata = load_pygame('demomap.tmx')
player = Player(camera_group, 1, 1)

#example
#SSL added to this
# This shows how you can create a list of enemies.  First it creates a list with the first enemy
# Then is adds a second enemy to the list with .append().
# The reason for this example is if the enemies get read from the map file it might be good to have a list of
# all the enemies later.  Don't know if it's helpful but tried it

# get_mob_type creates a random number that is used to decide what type of mob to create
# ListOfEnemyies = [Enemy(camera_group, 5, 5, get_mob_type())]
# ListOfEnemyies.append(Enemy(camera_group, 5, 5, get_mob_type()))

def blit_all_tiles(tmxdata,target):
        #blits the map using the display(screen), pytmx module for loading .tmx files, and the camera position
        tile_offset = math.Vector2()
        tile_offset.x = target.rect.centerx - SCREENWIDTH/2
        tile_offset.y = target.rect.centery - SCREENHEIGHT/2
        for layer in tmxdata:
            for tile in layer.tiles():
                #tile[0] is the x location on the gird
                #tile[1] is the y location
                #tile[2] is the image data for blitting
                tile_image = pygame.transform.scale(tile[2],(TILESIZE,TILESIZE))
                #tile_image = tile[2]
                x_pixel = tile[0] * TILESIZE - tile_offset.x
                y_pixel = tile[1] * TILESIZE - tile_offset.y
                display.get_surface().blit(tile_image, (x_pixel,y_pixel))

# #Loading in map file
# map_setup = []
# map_file = open(path.join(path.dirname(__file__), 'map.txt'))
# for line in map_file:
#    map_setup.append(line)
# #Map setup
# rownum = 0
# for row in map_setup:
#     entrynum = 0
#     for entry in row:
#         if entry == 'W':
#             Wall(camera_group, entrynum, rownum)
#         elif entry == 'P':
#             player = Player(camera_group, entrynum, rownum)
#         entrynum += 1
#     rownum += 1


#game logic in loop for while the game is running
while running:
    keys_pressed = key.get_pressed()
    player.dx, player.dy = 0, 0
    if (keys_pressed[K_w] or keys_pressed[K_UP]) and player.y > 0 and player.dx == 0: # can remove dx == 0 for each condition if we want diagonal movement
        player.dy = -1
    if (keys_pressed[K_s] or keys_pressed[K_DOWN]) and player.y < (HEIGHT - 1) and player.dx == 0:
        player.dy = 1
    if (keys_pressed[K_a] or keys_pressed[K_LEFT]) and player.x > 0 and player.dy == 0:
        player.dx = -1
    if (keys_pressed[K_d] or keys_pressed[K_RIGHT]) and player.x < (WIDTH - 1) and player.dy == 0:
        player.dx = 1
    #allows player to exit game
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            exit()
        elif event.type == movable_event:
            movable = True

#update logic
    #if it can move and isnt gonna go into anything:
    if movable and not player.check_collide():
        #check sequence to see if player moved
        prev_pos = player.x*3 + player.y
        player.move()
        #if they did move then dont let them move for another little bit
        if prev_pos != player.x*3 + player.y:
            movable = False
            time.set_timer(movable_event, MOVESPEED)

        # SSL Check if the player and enemy is within proximity to fight
        # if player.should_start_battle(enemy):
            # Do the Battely stuff here
            # todo

    #updates rect of each sprite to resolution coords not grid coords
    for sprite in camera_group:
        sprite.make_cam_pos()

#draw logic
    Display.fill(BG_COLOUR)
    #SK: blit the tiles from the .tmx file on top of display 
    blit_all_tiles(tmxdata,player)
    #camera_group.draw(Display)
    camera_group.custom_draw(player)
    camera_group.draw_grid()
    display.update()
    FPS.tick(FRAMERATE)
