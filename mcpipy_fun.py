import mcpi.minecraft as minecraft
import mcpi.block as block

# import random
import time
# import math

from build_it_util import BuildIt
import server


########
# This program is testing a collection of functions
#  (found in the BuildIt class of build_it_util.py)
#  taken or adapted from the examples in
#  https://github.com/brooksc/mcpipy
#  by sdf ( @samuelfreeman on Twitter, soundmaking on GitHub )
# see https://github.com/playwithcode/build-with-mcpi


########
# functions added by sdf to help with testing

def diamondBlock(mc, x, y, z):
    mc.setBlock(x, y, z, block.DIAMOND_BLOCK)
    time.sleep(1.5)


########
# main program to test the adapted functions
if __name__ == "__main__":
    ##
    mc = minecraft.Minecraft.create(server.address)
    buildit = BuildIt(mc)

    ##
    # buildit.flatmapEraseAll()

    ## clearZone takes two x,z pairs
    x = -20
    y = -20
    xx = 20
    yy = 20

    buildit.clearZone(x, y, xx, yy)

    ##
    x = 0
    y = 0
    z = 0

    diamondBlock(mc, x, y, z)

    floors = 6
    width = 5
    depth = 5
    floor_height = 3
    wall_material = block.STONE
    floor_material = block.WOOD_PLANKS

    buildit.drawBuilding(x, y, z, floors,
                         width, depth, floor_height,
                         wall_material, floor_material
                         )

    diamondBlock(mc, x, y, z)

    ##
    x = 10
    y = 20
    z = 10

    diamondBlock(mc, x, y, z)

    radius = 8
    block_id = block.GOLD_BLOCK
    block_data = 0

    buildit.solidSphere(x, y, z, radius, block_id, block_data)

    diamondBlock(mc, x, y, z)

    ##
    x = 10
    y = 20
    z = 10

    diamondBlock(mc, x, y, z)

    width = 105
    height = 40

    buildit.drawRainbow(x, y, z, width, height)

    diamondBlock(mc, x, y, z)

    # end if __main__

