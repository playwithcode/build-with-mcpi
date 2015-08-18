from mcpi import minecraft, block
from random import randint

mc = minecraft.Minecraft.create()

# # # # # # # #

# As well as an id number, some types of block
# need extra data to fully describe them...
#
# The wool block (whose id is 35)
# uses an extra number to set its colour

wool = 35

# Data Values for WOOL:
white = 0
orange = 1
magenta = 2
light_blue = 3
yellow = 4
lime = 5
pink = 6
grey = 7
light_grey = 8
cyan = 9
purple = 10
blue = 11
brown = 12
green = 13
red = 14
black = 15


# # # # # # # #

# initialise previous block co-ords
prev_x = 0
prev_y = 0
prev_z = 0

# start loop
while prev_y > -10 :
    # find where the player is 
    x, y, z = mc.player.getPos()

    # get which block player is on top of 
    block_x = int(x)
    block_y = int(y-1)
    block_z = int(z)

    # has the player moved?
    player_has_moved = False

    if block_x != prev_x:
        player_has_moved = True
    if block_y != prev_y:
        player_has_moved = True
    if block_z != prev_z:
        player_has_moved = True

    if player_has_moved:
        mc.setBlock(block_x, block_y, block_z, wool, randint(0, 15))

    # update prev block
    prev_x = block_x
    prev_y = block_y
    prev_z = block_z
# end of loop

mc.postToChat("Nyan Trails stopped")

