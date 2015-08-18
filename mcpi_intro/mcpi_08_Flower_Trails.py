from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

# # # # # # # #

flower = 38

# start loop
while True :
    # find where the player is 
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, flower)
    sleep(0.1)
# end of loop


