from mcpi import minecraft, block

mc = minecraft.Minecraft.create()

# # # # # # # #


# we can get the id number of a block type
# and store it as a variable with an easy to remember name

dirt = block.DIRT.id
bricks = block.BRICK_BLOCK.id
iron = block.IRON_BLOCK.id
lapis = block.LAPIS_LAZULI_BLOCK.id
gold = block.GOLD_BLOCK.id
diamond = block.DIAMOND_BLOCK.id

# find where the player is 
x, y, z = mc.player.getPos()

# set blocks around where the player is
mc.setBlock(x+1, y, z, gold)
mc.setBlock(x-1, y, z, iron)
mc.setBlock(x, y, z+1, lapis)
mc.setBlock(x, y, z-1, diamond)


