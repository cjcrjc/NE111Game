#GAME CONSTANTS
SCREENWIDTH = 1024
SCREENHEIGHT = 768
TILESIZE = 32
HEIGHT = SCREENHEIGHT/TILESIZE
WIDTH = SCREENWIDTH/TILESIZE
FRAMERATE = 60
MOVESPEED = 40

#COLOUR TUPLE CONSTANTS
BLACK = (0, 0, 0)         # Black
WHITE = (255, 255, 255)   # White
GREY = (128, 128, 128)   # Grey
RED = (255, 0, 0)       # Red
BLUE = (0, 0, 255)      # Blue
BG_COLOUR = (14,135,204)  # BLUEISH WATER COLOUR

#HEALTH CONSTANTS SSL
PLAYERHEALTH = 100 #both have same health but will have different dmg and swing rates
ENEMYHEALTH = 100

#BATTLE CONSTANTS SSL
PLAYERHITDMG = 30 #how fast player swings sword, faster than enemy
ENEMYHITDMG = 10 #im thinking swords cuz thats cool, like how fast enemy swings sword
PLAYERHITRATE = 100 #how fast player can hit enemy in battle sequence
ENEMYHITRATE = 200 #how fast enemy can hit player in battle sequence, enemy hits slower than player
