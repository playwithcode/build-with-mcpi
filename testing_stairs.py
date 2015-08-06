######## 
# import stuff to play with and build on:
 
from mcpi import minecraft
from mcpi import vec3

import mcpi_data_names # see https://github.com/playwithcode/build-with-mcpi

import time
import random

########
# setup stuff global for the code below

# to run this program across a network,
#   change "localhost" below for the IP 
#   address of the computer running the  
#   compatable Minecraft - e.g. "192.168.0.10"
mc = minecraft.Minecraft.create("localhost")

Vec3 = vec3.Vec3 # for 3D vector objects (x,y,z)

bid = mcpi_data_names.BlockIDs  # to access names representing block id numbers
dv = mcpi_data_names.Data       # to access words describing the data values

t = 0.25 # time in seconds used to sleep at various points in our main program


########
# functions to use in our main program

def setCube(x, y, z, radius, block, data):
  mc.setBlocks(x-radius, y, z-radius,     # coords for one corner of the cuboid
               x+radius, y+(radius*2), z+radius,  # the opposite corner of the cuboid
               block, data)  # block used to fill the cuboid (block id, data value)
# end def

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
  # end of for loop
# end of def stoneFloor(radius)

def stepPattnBlocks( origin, pattn, n_steps, b_id, b_dv ):
  for i in range(n_steps):
    v = origin + (pattn * i) 
    mc.setBlock( v.x, v.y, v.z, b_id, b_dv )
  # end for loop
# end def stepPattnBlocks


########
# main program

time.sleep( t ) 

## clear around 0,0,0 and set a floor to build on

x,y,z = 0,0,0
rad = 12
setCube( x, y, z, rad, bid.air, dv.null )
stoneBrickFloor( x, y, z, rad )
mc.setBlock( x, y-1, z, bid.diamond_block )

## build steps

num_steps  = 5
block_id   = bid.stairs_quartz

# N
start      = Vec3(x, y, z-2)
step_pttn  = Vec3(0, 1, -1)
block_data = dv.ascend_north
stepPattnBlocks( start, step_pttn, 2*num_steps, block_id, block_data )

# S
start      = Vec3(x, y, z+2)
step_pttn  = Vec3(0, 1, 2)
block_data = dv.ascend_south
stepPattnBlocks( start, step_pttn, num_steps, block_id, block_data )

start      = Vec3(x, y, z+2+1) #
step_pttn  = Vec3(0, 1, 2)
block_data = dv.invert_north #
stepPattnBlocks( start, step_pttn, num_steps, block_id, block_data )

# E
start      = Vec3(x+2, y, z)
step_pttn  = Vec3(2, 1, 0)
block_data = dv.ascend_east
stepPattnBlocks( start, step_pttn, num_steps, block_id, block_data )

# W
start      = Vec3(x-2, y, z)
step_pttn  = Vec3(-2, 1, 0)
block_data = dv.ascend_west
stepPattnBlocks( start, step_pttn, num_steps, block_id, block_data )



