from mcpi import minecraft

mc = minecraft.Minecraft.create()

# # # # # # # #

# find where the player is 
x, y, z = mc.player.getPos()

# set the player's position with +50 on the y
mc.player.setPos(x,y+50,z)

