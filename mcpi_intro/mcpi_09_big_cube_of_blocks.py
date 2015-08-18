from mcpi import minecraft, block 

mc = minecraft.Minecraft.create()

# # # # # # # #

dirt = block.DIRT.id
bricks = block.BRICK_BLOCK.id
iron = block.IRON_BLOCK.id
lapis = block.LAPIS_LAZULI_BLOCK.id
gold = block.GOLD_BLOCK.id
diamond = block.DIAMOND_BLOCK.id
stone = 1

# find where the player is 
x, y, z = mc.player.getPos()

# set a 3D volume of blocks between two coordinates

mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, stone)



