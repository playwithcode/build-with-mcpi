from mcpi import minecraft

mc = minecraft.Minecraft.create()

# # # # # # # #


# choose a block type (0 is Air, 1 is Stone, 2 is Grass, 3 is Dirt)
block_id = 0

# find where the player is 
x, y, z = mc.player.getPos()

# set blocks around where the player is
mc.setBlock(x+1, y, z, block_id)
mc.setBlock(x-1, y, z, block_id)
mc.setBlock(x, y, z+1, block_id)
mc.setBlock(x, y, z-1, block_id)


