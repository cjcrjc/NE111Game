#Group is Cameron (CC), Sam (SK), Sophia, (SSL), Dev (DL or other)

#Imports
import pygame.event
from pygame import *
from constants import *
from camera import *
from player import *
from wall import *
from os import path

#Loading in map file
map_setup = []
map_file = open(path.join(path.dirname(__file__), 'map.txt'))
for line in map_file:
    map_setup.append(line)

#Variable Setup
running = True
init()
Display = display.set_mode((SCREENWIDTH, SCREENHEIGHT))
Display.fill(WHITE)
FPS = time.Clock()
camera_group = CameraGroup()
movable_event = USEREVENT + 1
movable = True

#Map Setup
rownum = 0
for row in map_setup:
    entrynum = 0
    for entry in row:
        if entry == 'W':
            Wall(camera_group, entrynum, rownum)
        elif entry == 'P':
            player = Player(camera_group, entrynum, rownum)
        entrynum += 1
    rownum += 1

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
    #updates rect of each sprite to resolution coords not grid coords
    for sprite in camera_group:
        sprite.make_cam_pos()

#draw logic
    Display.fill(BG_COLOUR)
    #camera_group.draw(Display)
    camera_group.custom_draw(player)
    camera_group.draw_grid()
    display.update()
    FPS.tick(FRAMERATE)