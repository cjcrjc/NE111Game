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
import spritesheet
from enemy import *

# Variable Setup
running = True
init()
Display = display.set_mode((SCREENWIDTH, SCREENHEIGHT))
Display.fill(WHITE)
FPS = time.Clock()
movable_event = USEREVENT + 1
#SSL
enemy_hits_event = USEREVENT + 2
movable = True
camera_group = CameraGroup()
mapeditdata = load_pygame('demomap.tmx')
ss = spritesheet.spritesheet("Characters_V3_Colour.png")
player_ss_location = (0, 0, SSTILESIZE, SSTILESIZE)
player = Player(camera_group, 1, 1, ss)
battle = False

#SSL
all_player = pygame.sprite.Group()
all_player.add(player)
all_enemies = pygame.sprite.Group()
# call all_enemies.add whenever creating/spawning enemy sprites

# get_mob_type creates a random number that is used to decide what type of mob to create
# add this to test
#all_enemies.add(Enemy(camera_group, 5, 5, ss, get_mob_type()))

#SSL
def end_of_game():
    #can do any screen here, made it for a func below
    exit()

# created by SK, debugged by CC
def blit_all_tiles(tmxdata, target):
    # blits the map using the display(screen), pytmx module for loading .tmx files, and the camera position
    tile_offset = math.Vector2()
    tile_offset.x = target.rect.centerx - SCREENWIDTH / 2
    tile_offset.y = target.rect.centery - SCREENHEIGHT / 2
    # runs through every layer in the .tmx files, and, then runs through every tile and blits it on the display
    for layers in tmxdata:
        for tile in layers.tiles():
            # tile[0] is the x location on the gird
            # tile[1] is the y location
            # tile[2] is the image data for blitting
            tile_image = pygame.transform.scale(tile[2], (TILESIZE, TILESIZE))
            # tile_image = tile[2]
            x_pixel = tile[0] * TILESIZE - tile_offset.x
            y_pixel = tile[1] * TILESIZE - tile_offset.y
            # the actual blit command
            display.get_surface().blit(tile_image, (x_pixel, y_pixel))


# game logic in loop for while the game is running
while running:
    keys_pressed = key.get_pressed()
    player.dx, player.dy = 0, 0
    # can remove dx == 0 for each condition if we want diagonal movement
    if (keys_pressed[K_w] or keys_pressed[K_UP]) and player.y > 0 and player.dx == 0:
        player.dy = -1
        player.direction = Direction.UP
    if (keys_pressed[K_s] or keys_pressed[K_DOWN]) and player.y < (50 - 1) and player.dx == 0:
        player.dy = 1
        player.direction = Direction.DOWN
    if (keys_pressed[K_a] or keys_pressed[K_LEFT]) and player.x > 0 and player.dy == 0:
        player.dx = -1
        player.direction = Direction.LEFT
    if (keys_pressed[K_d] or keys_pressed[K_RIGHT]) and player.x < (50 - 1) and player.dy == 0:
        player.dx = 1
        player.direction = Direction.RIGHT
    
    # allows player to exit game
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            exit()
        elif (event.type == movable_event and battle == False):
            movable = True
        #SSL
        elif (event.type == enemy_hits_event and battle == True):
        #SSL
            player.take_damage(collided_enemy.damage)
            if player.is_dead() == True:
                battle = False
                end_of_game()
            else:
                time.set_timer(enemy_hits_event, collided_enemy.hit_rate)

#SSL
    if battle == True:
        if (keys_pressed[K_SPACE]):
            #draw attack
            collided_enemy.take_damage(player.damage)
            if collided_enemy.is_dead() == True:
                all_enemies.remove(collided_enemy)
                collided_enemy = None
                movable = True
                battle = False

    # update logic
    # if it can move and isnt gonna go into anything:
    if movable and not player.check_collide():
        # check sequence to see if player moved
        prev_pos = player.x * 3 + player.y
        player.move()
        # if they did move then dont let them move for another little bit
        if prev_pos != player.x * 3 + player.y:
            # change animation image
            if player.anim_step == 0:
                player.anim_step += 1
            else:
                player.anim_step -= 1
            player.image = transform.scale(player.animation[player.direction.value][player.anim_step], (TILESIZE, TILESIZE))
            # make the player not able to move
            movable = False
            time.set_timer(movable_event, MOVESPEED)
        else:
            player.anim_step = 2
            player.image = transform.scale(player.animation[player.direction.value][player.anim_step], (TILESIZE, TILESIZE))

        # SSL Check if the player and enemy is within proximity to fight
        collided_enemy = player.should_start_battle(all_enemies)
        if collided_enemy is not None:
            battle = True
            movable = False
            time.set_timer(enemy_hits_event, collided_enemy.hit_rate)


    # updates rect of each sprite to resolution coords not grid coords
    for sprite in camera_group:
        sprite.make_cam_pos()

    # draw logic
    Display.fill(BG_COLOUR)
    # SK: blit the tiles from the .tmx file on the display
    blit_all_tiles(mapeditdata, player)
    camera_group.custom_draw(player)

    #camera_group.draw_grid()
    display.update()
    FPS.tick(FRAMERATE)
