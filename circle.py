from mc import *

import math

mc = Minecraft()

def draw_circle(x, y, z, radius, mcblock):
    for degree in range(0, 360):
        current_x = int(x + radius*math.cos(math.radians(degree)))
        current_y = int(y + radius*math.sin(math.radians(degree)))
        mc.setBlock(current_x, current_y, z, mcblock) 

playerPos = mc.player.getPos()
draw_circle(int(playerPos.x), int(playerPos.y), int(playerPos.z), 57, GLASS)
