# Group is Cameron Chin (CC), Sam Krysko (SK), Sophia St. Laurent (SSL), Devaney Lakshman(DL)

# Imports
# Required downloads: pygame, pytmx, spritesheet (pip install ____)
import pygame.event
from pygame import *
from constants import *
from camera import *
from player import *
from wall import *
from pytmx.util_pygame import load_pygame
from pytmx.pytmx import *
import spritesheet
from enemy import *
from os import path
import damageblob
import random

# Variable Setup
running = True
init()
Display = display.set_mode((SCREENWIDTH, SCREENHEIGHT))
Display.fill(WHITE)
FPS = time.Clock()
movable_event = USEREVENT + 1
#SSL
enemy_hits_event = USEREVENT + 2
player_canattack_event = USEREVENT + 3
movable = True
camera_group = CameraGroup()
damage_particles_group = sprite.Group()
mapdata = load_pygame('demomap.tmx')
ss = spritesheet.spritesheet("Characters_V3_Colour.png")
player_ss_location = (0, 0, SSTILESIZE, SSTILESIZE)
player = Player(camera_group, 1, 1, ss)
battle = False
collided_enemy = None
playercanattack = True

#SK: initializing the walls
walls_setup = []
walls_file = open(path.join(path.dirname(__file__), 'walls.txt'))
#draws a line on the map for each line in the 'walls.txt' file
for line in walls_file:
    walls_setup.append(line)

#SK: setting up a map for the walls
rownum = 0
#SK: goes through each row in 'walls.txt' and checks for 'W's for wall positions, then makes a wall sprite there
#after sprite is made, the next row and/or entry in the 'walls.txt' file is checked
for row in walls_setup:
    entrynum = 0
    for entry in row:
        if entry == 'W':
            Wall(camera_group, entrynum, rownum)
        elif entry == "E":
            Enemy(camera_group, entrynum, rownum, ss)
        entrynum += 1
    rownum += 1

#SSL exits game upon player death
def end_of_game():
    #can do any screen here, made it for a func below
    exit()

# created by SK, debugged by CC
def blit_all_tiles(mapdata, target):
    # blits the map using the display(screen), pytmx module for loading .tmx files, and the camera position
    tile_offset = math.Vector2()
    tile_offset.x = target.rect.centerx - SCREENWIDTH / 2
    tile_offset.y = target.rect.centery - SCREENHEIGHT / 2
    # runs through every layer in the .tmx files, and, then runs through every tile and blits it on the display
    for layers in mapdata:
        for tile in layers.tiles():
            # tile[0] is the x location on the gird
            # tile[1] is the y location
            # tile[2] is the image data for blitting
            tile_image = transform.scale(tile[2], (TILESIZE, TILESIZE))
            # tile_image = tile[2]
            x_pixel = tile[0] * TILESIZE - tile_offset.x
            y_pixel = tile[1] * TILESIZE - tile_offset.y
            # the actual blit command
            display.get_surface().blit(tile_image, (x_pixel, y_pixel))

# game logic in loop for while the game is running
while running:
    keys_pressed = key.get_pressed()
    player.dx, player.dy = 0, 0
    if (keys_pressed[K_w] or keys_pressed[K_UP]) and player.y > 0 and player.dx == 0 and not battle:
        player.dy = -1
        player.direction = Direction.UP
    if (keys_pressed[K_s] or keys_pressed[K_DOWN]) and player.y < (50 - 1) and player.dx == 0 and not battle:
        player.dy = 1
        player.direction = Direction.DOWN
    if (keys_pressed[K_a] or keys_pressed[K_LEFT]) and player.x > 0 and player.dy == 0 and not battle:
        player.dx = -1
        player.direction = Direction.LEFT
    if (keys_pressed[K_d] or keys_pressed[K_RIGHT]) and player.x < (50 - 1) and player.dy == 0 and not battle:
        player.dx = 1
        player.direction = Direction.RIGHT
    
    # allows player to exit game
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            exit()
        elif event.type == movable_event and not battle:
            movable = True
        elif event.type == player_canattack_event and battle:
            playercanattack = True
        # SSL
        elif event.type == enemy_hits_event and battle:
        # SSL if player dies then end game, take damage
            if collided_enemy is not None:
                player.take_damage(collided_enemy.damage)
                for i in range(3):
                    damageblob.Damaged(damage_particles_group, player.rect.left + randrange(TILESIZE/4, TILESIZE*3/4, 4), player.rect.top + randrange(TILESIZE/4, TILESIZE*3/4, 4), 5)
                if player.is_dead():
                    battle = False
                    end_of_game()
                else:
                    time.set_timer(enemy_hits_event, collided_enemy.hit_rate)

    # SSL Check if the player and enemy is within proximity to fight
    collided_enemy = None
    for enemy in camera_group:
        if isinstance(enemy, Enemy) and player.test_collision(enemy):
            collided_enemy = enemy
    if collided_enemy is not None:
        battle = True
        movable = False
        player.image = transform.scale(player.animation[player.direction.value][2], (TILESIZE, TILESIZE))
        player.draw_health()
        if collided_enemy.can_attack:
            collided_enemy.can_attack = False
            player.take_damage(collided_enemy.damage)
            time.set_timer(enemy_hits_event, collided_enemy.hit_rate)
    print(battle)
    # SSL when player can attack, space bar for attack, how often player can attack and enemy death
    if battle:
        if (keys_pressed[K_SPACE]) and playercanattack:
            #draw attack
            collided_enemy.take_damage(player.damage)
            for i in range(3):
                damageblob.Damaged(damage_particles_group, collided_enemy.rect.left + randrange(TILESIZE/4, TILESIZE*3/4, 4), collided_enemy.rect.top + randrange(TILESIZE/4, TILESIZE*3/4, 4), 5)
            playercanattack = False
            time.set_timer(player_canattack_event, PLAYERHITRATE)
            if collided_enemy.is_dead():
                collided_enemy.remove()
                collided_enemy.kill()
                collided_enemy = None
                movable = True
                battle = False

    # update logic
    # if it can move and isnt gonna go into anything:
    if movable and not player.check_collide():
        # check sequence to see if player moved
        prev_pos = player.x * 10 + player.y
        player.move()
        # if they did move then dont let them move for another little bit
        if prev_pos != player.x * 10 + player.y:
            # change animation image
            if player.anim_step == 0:
                player.anim_step += 1
            else:
                player.anim_step -= 1
            player.image = transform.scale(player.animation[player.direction.value][player.anim_step], (TILESIZE, TILESIZE))
            player.draw_health()
            # make the player not able to move
            movable = False
            time.set_timer(movable_event, MOVESPEED)
        else:
            player.anim_step = 2
            player.image = transform.scale(player.animation[player.direction.value][player.anim_step], (TILESIZE, TILESIZE))
            player.draw_health()

    # updates rect of each sprite to resolution coords not grid coords
    for sprite in camera_group:
        sprite.make_cam_pos()

    # DRAW LOGIC
    Display.fill(BG_COLOUR)
    # SK: blit the tiles from the .tmx file on the display
    blit_all_tiles(mapdata, player)

    if collided_enemy is not None:
        collided_enemy.draw_health(player.direction)

    camera_group.custom_draw(player)
    for particle in damage_particles_group:
        draw.circle(display.get_surface(), RED, (particle.x-camera_group.offset.x, particle.y-camera_group.offset.y), radius=particle.rad)
        particle.update()
    display.update()
    FPS.tick(FRAMERATE)
