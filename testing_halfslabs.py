######## 
# import stuff to play with and build on:
 
from mcpi import minecraft

import build_it_util    # see https://github.com/playwithcode/build-with-mcpi
import server           # originally from mcpipy, also part of build-with-mcpi

import time
import random

########
# setup global code stuff

mc = minecraft.Minecraft.create(server.address)

Vec3 = minecraft.Vec3   # for 3D vector objects (x,y,z)

bid = build_it_util.BlockIDs   
dv  = build_it_util.Data
buildit = build_it_util.BuildIt(mc)

t = 0.25 # a time value in seconds, can be used to sleep at points in our main program


########
# functions to use in our main program


########
# main program

#time.sleep( t ) 

## clear around 0,0,0 and set a floor to build on

x,y,z = 0,0,0
#x,y,z = 266,64,300
buildit.centredCube(x, y, z, 20, bid.air, dv.null )
buildit.stoneBrickFloor(x, y, z, 16)


##
for i in range(16):
    mc.setBlock(x+i, y, z+i,
                bid.half_slab, 
                i)

types_of_half_slab = [dv.stone,
                      dv.sandstone,
                      dv.wood,
                      dv.cobble,
                      dv.brick , 
                      dv.stonebrick,
                      dv.upper_stone,
                      dv.upper_sandstone,
                      dv.upper_wood,
                      dv.upper_cobble,
                      dv.upper_brick ,
                      dv.upper_stonebrick]

i = 0
for value in types_of_half_slab:
    print value
    mc.setBlock(x+i, y, z+i,
                bid.half_slab, 
                value)
    i -= 1


