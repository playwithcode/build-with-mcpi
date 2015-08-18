from mcpi import minecraft

mc = minecraft.Minecraft.create()

# # # # # # # #

pos = mc.player.getPos()

mc.postToChat("player pos (x,y,z) = ")
mc.postToChat(pos.x)
mc.postToChat(pos.y)
mc.postToChat(pos.z)

