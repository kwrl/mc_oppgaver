from mc import *

mc = Minecraft()

def draw_line_x(x, y, z, length, block_type):
    for current_x in range(x, x+length):
        mc.setBlock(current_x, y, z, block_type)

def draw_line_y(x, y, z, length, block_type):
    for current_y in range(y, y+length):
        mc.setBlock(x, current_y, z, block_type)

def draw_line_z(x, y, z, length, block_type):
    for current_z in range(z, z+length):
        mc.setBlock(x, y, current_z, block_type)

playerPos = mc.player.getPos()
x, y, z = int(playerPos.x), int(playerPos.y), int(playerPos.z)

draw_line_x(x, y, z, 200, GLASS)
