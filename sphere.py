from mc import *

import math

mc = Minecraft()

def draw_circle(x, y, z, radius, mcblock):
    for degree in range(0, 360):
        current_x = int(x + radius*math.cos(math.radians(degree)))
        current_y = int(y + radius*math.sin(math.radians(degree)))
        mc.setBlock(current_x, current_y, z, mcblock) 

def draw_sphere(x, y, z, radius, mcblock):
    for step in range(0, 2*radius):
        draw_circle(x, y, z+step, int(math.sqrt(radius**2-(radius-step)**2)), mcblock)

playerPos = mc.player.getPos()
draw_sphere(int(playerPos.x), int(playerPos.y), int(playerPos.z), 40, GLASS)
