######## 
# import stuff to play with and build on:
 
from mcpi import minecraft

import time, random

import mcpi_data_names # see https://github.com/playwithcode/build-with-mcpi

########
# setup 

ip_addr = "192.168.0.10" # IP address of the RPi running Minecraft - try "localhost"


mc = minecraft.Minecraft.create(ip_addr)

# mc.postToChat("playing with mcpi in Python") # message in chat confirms the connection

id = mcpi_data_names.BlockIDs   # so we can use names representing block id numbers
dv = mcpi_data_names.Data       # so we can use words describing the data values

t = 0.25 # time in seconds used to sleep at various points in our main program

########
# functions to use in our main program


########
# main program

time.sleep(t) # program will wait before continuing 

# find where the player is and clear a space to build in
x,y,z = mc.player.getTilePos()
mc.setBlocks(x-10, y, z-10,     # coords for one corner of the cuboid
             x+10, y+20, z+10,  # the opposite corner of the cuboid
             id.air, dv.null)   # block used to fill the cuboid (id, data value)

time.sleep(t) 

# set the floor of that area to stone_brick
mc.setBlocks(x-10, y-1, z-10,     
             x+10, y-1, z+10,     
             id.stone_brick, dv.normal)            

time.sleep(t) 

# choose randomly to add some mossy and cracked blocks to the stone_brick floor
for i in range(200):
  time.sleep( t * 0.1 )
  x_rand  = x + random.choice( range(-10,10) )
  z_rand  = z + random.choice( range(-10,10) )
  dv_rand =     random.choice( (dv.mossy, dv.cracked) )
  mc.setBlock(x_rand, y-1, z_rand, id.stone_brick, dv_rand)
  
mc.setBlock( x, y, z, id.diamond_block ) 
mc.player.setPos( x, y+1, z )