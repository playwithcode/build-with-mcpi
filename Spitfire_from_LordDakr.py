""" build design based on spitfire tutorial by Lord Dakr:
        https://youtu.be/5CNQgWBaOe4?list=PLpegz2C6u5FyzNNutMJhCpGCZb1ZhL8NO
    with some minor alterations and addition by sdf:
        (@samuelfreeman on Twitter, soundmaking on GitHub)
"""

########
# import stuff to play with and build on:

from mcpi import minecraft

import build_it_util    # see https://github.com/playwithcode/build-with-mcpi
import server           # originally from mcpipy, also part of build-with-mcpi

import time

########
# setup global code stuff

Vec3 = minecraft.Vec3   # for 3D vector objects (x,y,z)

mc = minecraft.Minecraft.create(server.address)

buildit = build_it_util.BuildIt(mc)

MyBlock = build_it_util.MyBlock

bid = build_it_util.BlockIDs

dv = build_it_util.Data

t = 0.25

########
# set what blocks we will use for the spitfire

wheel = MyBlock(bid.wool, dv.black)
nose = MyBlock(bid.iron_block, dv.null)

upper_half_slab = MyBlock(bid.half_slab, dv.upper_sandstone)
lower_half_slab = MyBlock(bid.half_slab, dv.sandstone)
full_block = MyBlock(bid.sandstone, dv.normal)
stairs = MyBlock(bid.stairs_sandstone, dv.ascend_west)

# # un-comment the lines below to use cobblestone type blocks

# upper_half_slab = MyBlock(bid.half_slab, dv.upper_cobble)
# lower_half_slab = MyBlock(bid.half_slab, dv.cobble)
# full_block = MyBlock(bid.cobblestone, dv.normal)
# stairs = MyBlock(bid.stairs_cobblestone, dv.ascend_west)


########
# main program

# get position of the player
player_pos = mc.player.getPos()

# set starting position to nearby where the player is
start_pos = Vec3(player_pos.x, player_pos.y, player_pos.z-5)


# # clear some space
rad = 8
buildit.centredCube(start_pos.x, start_pos.y+rad, start_pos.z, rad, bid.air, dv.null )
time.sleep(t)

# # Build the wheels # #

# start pos is between the front wheels
my_pos = Vec3(start_pos.x, start_pos.y, start_pos.z)

# move to front wheel pos:
my_pos += Vec3(-2,0,0)
mc.setBlock(my_pos.x, my_pos.y, my_pos.z, wheel.bid, wheel.dv)
mc.setBlock(my_pos.x, my_pos.y+1, my_pos.z, bid.fence)

# move to other front wheel pos:
my_pos += Vec3(4,0,0)
mc.setBlock(my_pos.x, my_pos.y, my_pos.z, wheel.bid, wheel.dv)
mc.setBlock(my_pos.x, my_pos.y+1, my_pos.z, bid.fence)

# move to back wheel pos:
my_pos += Vec3(-2,0,-6)
mc.setBlock(my_pos.x, my_pos.y, my_pos.z, wheel.bid, wheel.dv)
mc.setBlock(my_pos.x, my_pos.y+1, my_pos.z, bid.fence)

time.sleep(t)


# # build the body # #

#  move to one block up from the start pos, and also one block to the side
my_pos = Vec3(start_pos.x+1, start_pos.y+1, start_pos.z)

# put a 3x3 layer of upper half slabs
mc.setBlocks(my_pos.x, my_pos.y, my_pos.z,
             my_pos.x-2, my_pos.y, my_pos.z-2,
             upper_half_slab.bid, upper_half_slab.dv)

#  move to one block up from the start pos, and also one block forward towards the nose
my_pos = Vec3(start_pos.x, start_pos.y+1, start_pos.z+1)

# put a row of upper half slabs towards the tail
mc.setBlocks(my_pos.x, my_pos.y, my_pos.z,
             my_pos.x, my_pos.y, my_pos.z-5,
             upper_half_slab.bid, upper_half_slab.dv)

time.sleep(t)


# move up one block
my_pos.y += 1

# put a full block on top of front slab
mc.setBlock(my_pos.x, my_pos.y, my_pos.z,
            full_block.bid, full_block.dv)

# move along putting two rows of stairs, with the last step turning inwards
for i in range(6):
    if i < 5:
        data_value_A = dv.ascend_west
        data_value_B = dv.ascend_east
    else:
        data_value_A = dv.ascend_south
        data_value_B = dv.ascend_south
    mc.setBlock(my_pos.x+1, my_pos.y, my_pos.z-i,
                stairs.bid, data_value_A)
    mc.setBlock(my_pos.x-1, my_pos.y, my_pos.z-i,
                stairs.bid, data_value_B)

time.sleep(t)

# put full block between the in-turned stairs, and another block on the back of that
my_pos.z -= 5
mc.setBlocks(my_pos.x, my_pos.y, my_pos.z,
             my_pos.x, my_pos.y, my_pos.z-1,
             full_block.bid, full_block.dv)

# put a row of half slabs on top of each of those
mc.setBlocks(my_pos.x, my_pos.y+1, my_pos.z+4,
             my_pos.x, my_pos.y+1, my_pos.z-1,
             lower_half_slab.bid, lower_half_slab.dv)

# replace two of the slabs with glass
mc.setBlocks(my_pos.x, my_pos.y+1, my_pos.z+2,
             my_pos.x, my_pos.y+1, my_pos.z+1,
             bid.glass, dv.null)

time.sleep(t)

# continuing towards the tail with an inverted stair over the back wheel
mc.setBlock(my_pos.x, my_pos.y, my_pos.z-2, stairs.bid, dv.invert_south)

# three more stairs and some half slabs to finish the tail
mc.setBlock(my_pos.x, my_pos.y+1, my_pos.z-2, stairs.bid, dv.ascend_north)
mc.setBlock(my_pos.x, my_pos.y+1, my_pos.z-3, stairs.bid, dv.invert_south)
mc.setBlock(my_pos.x, my_pos.y+2, my_pos.z-3, stairs.bid, dv.ascend_north)
mc.setBlock(my_pos.x+1, my_pos.y+1, my_pos.z-3, upper_half_slab.bid, upper_half_slab.dv)
mc.setBlock(my_pos.x-1, my_pos.y+1, my_pos.z-3, upper_half_slab.bid, upper_half_slab.dv)

time.sleep(t)

# # build the wings # #
my_pos = start_pos + Vec3(0,2,0)

wing_size = 5
# wing_size = 10

for i in range(2, wing_size+2):
    if i > wing_size:
        k = 2
    else:
        k = 3
    for j in range(k):
        mc.setBlock(my_pos.x-i, my_pos.y, my_pos.z-j, lower_half_slab.bid, lower_half_slab.dv)
        mc.setBlock(my_pos.x+i, my_pos.y, my_pos.z-j, lower_half_slab.bid, lower_half_slab.dv)
        if i == wing_size-1 and j == 1:
            mc.setBlock(my_pos.x-i, my_pos.y, my_pos.z-j, bid.half_slab, dv.stone)
            mc.setBlock(my_pos.x+i, my_pos.y, my_pos.z-j, bid.half_slab, dv.stone)


# # build the nose # #
my_pos = start_pos + Vec3(0,2,2)

mc.setBlock(my_pos.x, my_pos.y, my_pos.z, nose.bid, nose.dv)

mc.setBlock(my_pos.x, my_pos.y+1, my_pos.z, bid.fence, dv.null)
mc.setBlock(my_pos.x, my_pos.y-1, my_pos.z, bid.fence, dv.null)

mc.setBlock(my_pos.x+1, my_pos.y, my_pos.z, bid.fence_gate, dv.null)
mc.setBlock(my_pos.x-1, my_pos.y, my_pos.z, bid.fence_gate, dv.null)





