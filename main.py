#Group is Cameron (CC), Sam (SK), Sophia, (SSL), Dev (Dsmth or other)
import pygame.event
from pygame import *
from constants import *
from player import *

running = True
init()
Display = display.set_mode((SCREENWIDTH, SCREENHEIGHT))
Display.fill(WHITE)
FPS = time.Clock()

player = Player()
#enemy = Enemy()

#game logic in loop for while the game is running
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            exit()

    #update logic
    player.move()
    #enemy.move()

    #draw logic
    Display.fill(WHITE)
    player.draw(Display)
    #enemy.draw(Display)

    display.update()
    FPS.tick(FRAMERATE)