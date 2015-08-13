######## 
# import stuff to play with and build on:
 
from mcpi import minecraft

import build_it_util # see https://github.com/playwithcode/build-with-mcpi

import time
import random

########
# setup stuff global for the code below

''' to run this program across a network,
    change "localhost" below for the IP 
    address of the computer running the
    compatable Minecraft - e.g. "192.168.0.10" '''

mc = minecraft.Minecraft.create("localhost")

Vec3 = minecraft.Vec3 # for 3D vector objects (x,y,z)

bid = build_it_util.BlockIDs   
dv  = build_it_util.Data

t = 0.25 # time in seconds used to sleep at various points in our main program




########
# functions to use in our main program

def setCube(x, y, z, radius, block, data):
  mc.setBlocks(x-radius, y, z-radius,     
               x+radius, y+(radius*2), z+radius,  
               block, data)  


def stoneBrickFloor(x,y,z,radius):
  mc.setBlocks(x-radius, y-1, z-radius,     
               x+radius, y-1, z+radius,     
               bid.stone_brick, dv.normal)            
  for i in range(2*radius*radius):
    x_rand  = x + random.choice( range(0-radius,radius) )
    z_rand  = z + random.choice( range(0-radius,radius) )
    dv_rand =     random.choice( (dv.mossy, dv.cracked) )
    mc.setBlock(x_rand, y-1, z_rand,
                bid.stone_brick, dv_rand)


def stepPattnBlocks( origin, pattn, n_steps, b_id, b_dv ): # use Vec3 for origin and pattn
  for i in range(n_steps):
    v = origin + (pattn * i) 
    mc.setBlock( v.x, v.y, v.z, b_id, b_dv )


def randomStairs():
  stairs = (bid.stairs_brick,
            bid.stairs_cobblestone,
            bid.stairs_netherbrick,
            bid.stairs_quartz,
            bid.stairs_sandstone,
            bid.stairs_stonebrick,
            bid.stairs_wood
           )
  return random.choice(stairs)
            


########
# main program

#time.sleep( t ) 

## clear around 0,0,0 and set a floor to build on

x,y,z = 0,0,0
rad = 16
setCube( x, y, z, rad, bid.air, dv.null )
stoneBrickFloor( x, y, z, rad )
#mc.setBlock( x, y, z, bid.diamond_block )



##
for i in range(16):
    mc.setBlock(i,0,0,
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
    mc.setBlock(0,0,i,
                bid.half_slab, 
                value)
    i += 1


