######## 
# import stuff to play with and build on:
 
from mcpi import minecraft

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

Vec3 = minecraft.Vec3 # for 3D vector objects (x,y,z)

bid = mcpi_data_names.BlockIDs   
dv  = mcpi_data_names.Data

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

time.sleep( t ) 

## clear around 0,0,0 and set a floor to build on

x,y,z = 0,0,0
rad = 12
setCube( x, y, z, rad, bid.air, dv.null )
stoneBrickFloor( x, y, z, rad )
mc.setBlock( x, y-1, z, bid.diamond_block )

## build steps

num_steps  = 5
stop_looping = False

while(not stop_looping):
  block_id   = randomStairs()
  time.sleep(t)

  # N
  start      = Vec3(x, y, z-2)
  step_pttn  = Vec3(0, 1, -1)
  block_data = dv.ascend_north
  stepPattnBlocks( start, step_pttn, 2*num_steps, block_id, block_data )

  block_id   = randomStairs()
  time.sleep(t)

  # S
  start      = Vec3(x, y, z+2)
  step_pttn  = Vec3(0, 1, 2)
  block_data = dv.ascend_south
  stepPattnBlocks( start, step_pttn, num_steps, block_id, block_data )

  block_id   = randomStairs()
  time.sleep(t)

  start      = Vec3(x, y, z+2+1)  #
  step_pttn  = Vec3(0, 1, 2)
  block_data = dv.invert_north    #
  stepPattnBlocks( start, step_pttn, num_steps, block_id, block_data )

  block_id   = randomStairs()
  time.sleep(t)

  # E
  start      = Vec3(x+2, y, z)
  step_pttn  = Vec3(2, 1, 0)
  block_data = dv.ascend_east
  stepPattnBlocks( start, step_pttn, num_steps, block_id, block_data )

  block_id   = randomStairs()
  time.sleep(t)

  # W
  start      = Vec3(x-2, y, z)
  step_pttn  = Vec3(-2, 1, 0)
  block_data = dv.ascend_west
  stepPattnBlocks( start, step_pttn, num_steps, block_id, block_data )

  if mc.player.getTilePos() == Vec3(0,0,0):
    stop_looping = True

