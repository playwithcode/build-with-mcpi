######## 
# import stuff to play with and build on:
 
from mcpi import minecraft
import time
import random

# following imports are from https://github.com/playwithcode/build-with-mcpi
import mcpi_data_names 
from mcpipy_fun import *


########
# setup stuff global for the code below

# to run this program across a network,
#   change "localhost" below for the IP 
#   address of the computer running the  
#   compatable Minecraft - e.g. "192.168.0.10"
mc = minecraft.Minecraft.create("localhost")


bid = mcpi_data_names.BlockIDs   
dv  = mcpi_data_names.Data

t = 0.25 # time in seconds used to sleep at various points in our main program




########
# functions to use in our main program


########
# main program
mc.postToChat("hello")
#mcpipy.flatmapEraseAll(mc) #<- use with caution - all blocks will be lost!
drawRainbow(0,0,0, 100, 15)
