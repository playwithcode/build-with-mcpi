#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
import math


########
# a collection of functions
#  taken or adapted from the examples in
#  https://github.com/brooksc/mcpipy
#  by sdf ( @samuelfreeman on Twitter, soundmaking on GitHub )


####
''' after snowbound_flatmap.py
''' ### This will erase every block in the current world! Be careful! ###
def flatmapEraseAll(mc):
    mc.postToChat("please be patient - this may take a while!")
    time.sleep(3)
    mc.setBlocks(-128,0,-128,
                 128,64,128,
                 0
                )
    mc.setBlocks(-128,0,-128,
                 128,-64,128,
                 block.SANDSTONE.id
                )


####
""" clearZone clears an area and sets a stone floor
    takes two x,z pairs clears everything above 0y and then sets
    a stone floor at -1y
    @author: goldfish"""
def clearZone( alocx, alocz, blocx, blocz ):
    mc.setBlocks( alocx, 0, alocz, blocx, 64, blocz, block.AIR )
    mc.setBlocks( alocx, -1, alocz, blocx, -1, blocz, block.STONE )

####
""" draw a building
    @author: goldfish"""
def drawBuilding( locx, locy, locz, floors,
                  width, depth, floorheight,
                  wallmaterial, floormaterial
                ):
    topx = locx+width
    topy = locy+((floorheight+1)*floors)
    topz = locz+depth
    #draw building shell
    mc.setBlocks( locx, locy, locz,
                  topx, topy, topz,
                  wallmaterial
                )
    mc.setBlocks( locx+1, locy+1, locz+1,
                  topx-1, topy-1, topz-1,
                  block.AIR
                )
    #draw floors
    if( floors > 1 ):
        for i in range( floors -1 ):
            floorYloc = locy+( (floorheight+1)*(i+1) )
            mc.setBlocks( locx+1, floorYloc, locz+1,
                          topx-1, floorYloc, topz-1,
                          floormaterial
                        )
    #draw door
    doorloc = random.randint( 1, width-2 )
    mc.setBlock( locx, locy+1, locz+doorloc, block.AIR )
    mc.setBlock( locx, locy+2, locz+doorloc, block.AIR )
    #draw front windows
    if( floors > 1 ):
        for i in range( floors-1 ):
            windowYloc = locy+2+( (floorheight+1)*(i+1) )
            for j in range( floorheight-1 ):
                mc.setBlocks( locx, windowYloc+j , locz+1,
                              locx, windowYloc+j, locz+(width-1),
                              block.GLASS_PANE
                            )
    #draw back windows
    if( floors > 1 ):
        for i in range( floors-1 ):
            windowYloc = locy+2+( (floorheight+1)*(i+1) )
            for j in range( floorheight-1 ):
                mc.setBlocks( locx+depth, windowYloc+j , locz+1,
                              locx+depth, windowYloc+j, locz+(width-1),
                              block.GLASS_PANE
                            )
    #connect levels with ladder
    #mc.setBlocks( topx-1, locy+1, topz-1, topx-1, topy-1, topz-1, block.LADDER )
                

####
'''
function below abstracted from nt7s_sphere.py

original citation: 
  # mcpipy.com retrieved from URL below, written by  Jason Milldrum, NT7S
  # http://www.nt7s.com/blog/2013/02/exploring-minecraft-pi-edition/

made to take arguments instead of using pos

'''
def solidSphere (x_, y_, z_, radius, block_id, block_data=0):

  pos = minecraft.Vec3(x_,y_,z_) # was using mc.player.getPos() 

  for x in range(radius*-1,radius):
    for y in range(radius*-1, radius):
      for z in range(radius*-1,radius):
        if x**2 + y**2 + z**2 < radius**2:
          mc.setBlock( pos.x + x,
                       pos.y + y + radius,
                       pos.z - z,#- 10,
                       block_id,
                       block_data
                     )



''' drawRainbow function adpated from zhuowei_rainbow.py:
        # mcpipy.com retrieved from URL below, written by zhuowei
        # http://www.minecraftforum.net/topic/1638036-my-first-script-for-minecraft-pi-api-a-rainbow/
    sdf added variable xyz_offset and width...
'''
def drawRainbow( x_, y_, z_, width, height ):
  colors = [14, 1, 4, 5, 3, 11, 10]
  x_offset = x_ + int(width / 2) 
  for x in range(0, width):
    for colourindex in range(0, len(colors)):
      x_now = x - x_offset
      y_now = math.sin( ( x / float(width) ) * math.pi ) * height + colourindex
      z_now = z_
      global.mc.setBlock( x_now, int(y_now), z_now,
                   block.WOOL.id,
                   colors[len(colors) - 1 - colourindex]
                 )

      


########
# functions added by sdf to help with testing

def diamondBlock(x,y,z):
  mc.setBlock( x, y, z, block.DIAMOND_BLOCK )
  time.sleep(1)


######## 
# main program to test all the functions
if __name__ == "__main__":
  mc = minecraft.Minecraft.create( )

  ##
  # see https://github.com/playwithcode/build-with-mcpi
  #flatmapEraseAll(mc)
  
  ## 
  clearZone( -20, -20, 20, 20 )

  ##
  diamondBlock( 0, 0, 0 )
  drawBuilding( 0, 0, 0, 4,   # x, y, z, floors,
                5, 5, 3,      # width, depth, floorheight,
                block.STONE, block.WOOD_PLANKS    # wallmaterial, floormaterial
              )
  diamondBlock( 0, 0, 0 )

  ##
  diamondBlock(10, 20, 10)
  solidSphere( 10, 20, 10, 7,        # x, y, z, radius
               block.GOLD_BLOCK, 0 # block_id, block_data
             )
  diamondBlock(10, 20, 10)

  ## drawRainbow( x, y, z, width, height )
  drawRainbow( -10, 10, -10, 120, 50 )
