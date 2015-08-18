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

# # # # # # # #

# initialise previous block co-ords
prev_x = 0
prev_y = 0
prev_z = 0

# start loop
while True:
    # find where the player is 
    x, y, z = mc.player.getPos()

    # get which block player is on top of 
    block_x = int(x)
    block_y = int(y-1)
    block_z = int(z)

    # has the player moved?
    player_has_moved = False

    if block_x != prev_x:
        player_has_moved = True
    if block_y != prev_y:
        player_has_moved = True
    if block_z != prev_z:
        player_has_moved = True

    if player_has_moved:
        mc.setBlock(block_x, block_y, block_z, gold)

    # update prev block
    prev_x = block_x
    prev_y = block_y
    prev_z = block_z
# end of loop
