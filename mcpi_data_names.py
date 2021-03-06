######## 
# mcpi_data_names.py
# by sdf (@samuelfreeman on Twitter, soundmaking on GitHub)

# main API-reference used = http://www.stuffaboutcode.com/p/minecraft-api-reference.html

# id values for blocks 
class BlockIDs():
  air                 = 0
  stone               = 1
  grass               = 2
  dirt                = 3
  cobblestone         = 4
  wood_planks         = 5
  planks              = wood_planks
  sapling             = 6 # data: (0 oak), 1 spruce, 2 birch
  bedrock             = 7
  water_flowing       = 8
  water               = water_flowing
  water_stationary    = 9 # data: sets hight (not stationary if touching blocks interact)
  water_stat          = water_stationary
  lava_flowing        = 10
  lava                = lava_flowing
  lava_stationary     = 11 # data: sets hight (not stationary if touching blocks interact)
  lava_stat           = lava_stationary
  sand                = 12
  gravel              = 13
  gold_ore            = 14
  iron_ore            = 15
  coal_ore            = 16
  wood                = 17 # data: (0 oak), 1 spruce, 2 birch
  leaves              = 18 # data: (0 oak), 1 spruce, 2 birch
  glass               = 20
  lapis_lazuli_ore    = 21
  lapis_ore           = lapis_lazuli_ore
  lapis_lazuli_block  = 22
  lapis_block         = lapis_lazuli_block
  sandstone           = 24 # data: (0 sandstone), 1 chiseled, 2 smooth
  bed                 = 26 # data: different orientations: (0)-7 foot, 8-15 head of bed
  cobweb              = 30
  grass_tall          = 31 # data: 0 shrub, (1 or 2 long_grass), 3 fern
  foliage             = grass_tall
  wool                = 35 # data: 0-15 sets colour (for names, see class Data below)
  flower_yellow       = 37
  flower_cyan         = 38
  mushroom_brown      = 39
  mushroom_red        = 40
  gold_block          = 41
  iron_block          = 42
  stone_slab_double   = 43 # data: type of stone: see in class Data() below
  stone_slab_dbl      = stone_slab_double
  stone_slab          = 44 # data: type of stone: <8 lower half, >7 upper half: see below
  brick_block         = 45
  tnt                 = 46 # data: (0 inactive), 1 explode when hit
  bookshelf           = 47
  moss_stone          = 48
  obsidian            = 49
  torch               = 50 # data: should set orientation, depends on touching blocks
  fire                = 51 # not working(?)
  stairs_wood         = 53 # data: N%8 to set orientation
  chest               = 54 # data: set orientation: 2 north, 3 south, 4 west, 5 east
  diamond_ore         = 56
  diamond_block       = 57
  crafting_table      = 58
  farmland            = 60
  furnace_inactive    = 61 # data should set which way it is facing...
  furnace_active      = 62 # ...seems there is no change with data(?)
  sign                = 63 # data: N%16 sets angle # sign added to this list by sdf
  door_wood           = 64 # data: set orientation: <8 lower half, >7 upper half of door 
  ladder              = 65 # data: 2-5 sets orientation: needs a block to attach to
  stairs_cobblestone  = 67 # data: N%8 to set orientation
  door_iron           = 71 # data: seems glitchy: <8 lower half, >7 upper half of door
  redstone_ore        = 73
  snow                = 78
  ice                 = 79
  snow_block          = 80
  cactus              = 81
  clay                = 82
  sugar_cane          = 83
  fence               = 85
  glowstone_block     = 89
  bedrock_invisible   = 95
  stone_brick         = 98 # data: (0 Stone brick), 1 mossy, 2 cracked, 3 chiseled(?)
  glass_pane          = 102
  melon               = 103
  fence_gate          = 107
  glowing_obsidian    = 246
  nether_reactor_core = 247
  
  ##
  # The following were not listed in the api-reference!
  stairs_brick        = 108 # data: sets orientation 
  stairs_stonebrick   = 109 # data: sets orientation 
  stairs_sandstone    = 128 # data: sets orientation 
  stairs_quartz       = 156 # data: sets orientation 
  stairs_netherbrick  = 114 # data: sets orientation

  quartz_block        = 155 # data: (0 smooth)



# end class BlockIDs  

class Data():
  null = 0
  
  # wood and sapling, data value set type
  #   (note - wood_planks are always oak in Pi Edition)
  oak     = 0
  spruce  = 1
  birch   = 2
  
  # stationary water or lava data sets depth 
  #  (note - stat water or lava may interact
  #        with touching blocks and thus flow or change)
  # default 0 is as full as it gets at three quarters of the block height
  lowLevel = (7, 6, 5, 4, 3, 2, 1) # lowLevel[0] is lowest, lowLevel[6] is quarter block
  
  # sandstone data sets type
  basic    = 0 
  chiseled = 1     # also for quartz_block
  smooth   = 2
  
  # bed data: different orientations: (0)-7 foot, 8-15 head of bed
  '''
  foot_N =
  foot_E =
  foot_S =
  foot_W =
  head_N =
  head_E =
  head_S =
  head_W =
  '''

  # grass_tall or foliage, data value set type of plant:
  # (note - the API-reference used gives fern as 2, but sdf finds fern as 3)
  # (note - unlike other data values that default to 0, this block defaults to grass)
  shrub   = 0
  grass   = 1  
  fern    = 3 
  
  # wool, data value sets colour
  white       = 0
  orange      = 1
  magenta     = 2
  light_blue  = 3
  yellow      = 4
  lime        = 5
  pink        = 6
  grey        = 7
  light_grey  = 8
  cyan        = 9
  purple      = 10
  blue        = 11
  brown       = 12
  green       = 13
  red         = 14
  black       = 15
  
  # stone_slab_double (aka stone_slab_dbl)
  #   data sets type of stone
  stone_slabs  = 0
  sandst       = 1 # looks the same as a normal block of sandstone
  wood         = 2 # looks the same as a normal block of wood planks
  cobble       = 3 # looks the same as a normal block of cobblestone
  brick        = 4 # looks the same as a normal block of bricks
  stonebrick   = 5 # looks the same as a normal block of stone_brick
  stone_smooth = 6
  
  # stone_slab data sets type of stone,
  #  <8 lower half, >7 upper half
  
  # tnt data: (0 inactive), 1 explode when hit
  
  # torch
  
  # stairs_wood
  #       _cobblestone
  #       _sandstone
  #       _stonebrick
  #       _netherbrick
  #       _brick
  #       _quartz
  #   data set orientation
  ascend_east   = 0
  ascend_west   = 1
  ascend_south  = 2
  ascend_north  = 3
  invert_east   = 4
  invert_west   = 5
  invert_south  = 6
  invert_north  = 7
  
  # chest
  
  # furnace
  
  # sign
  
  # door_wood
  
  # ladder
  
  # stairs_cobblestone
  
  # door_iron
  
  # stone_brick data sets variant
  normal  = 0
  mossy   = 1
  cracked = 2

  # quartz_block data sets variant
  ''' some valid data names are declared above:
           0 == basic == normal == null
           1 == chiseled            '''
  pillar = 2

# end class Data  
