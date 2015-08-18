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
tnt = 46

# find where the player is 
x, y, z = mc.player.getPos()

# put a block of TNT!

mc.setBlock(x+1, y, z+1, tnt)

# but the player cannot activate that block


# # # # # # # #


# un-comment the following line (delete the #)
# to put a block of TNT with data value 1 = PRIMED!

#mc.setBlock(x+1, y+1, z+1, tnt, 1)

# the player can 'hit' this block (left click with sword)
# to activate the TNT and cause an explosion!


