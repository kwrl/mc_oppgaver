from mc import *

mc = Minecraft()

def draw_cube(x, y, z, length, mcblock):
    for current_x in range(x, x+length):
        for current_y in range(y, y+length):
            for current_z in range(z, z+length):
                mc.setBlock(current_x, current_y, current_z, mcblock)

def draw_box(x, y, z, length, mcblock):
    pass

playerPos = mc.player.getPos()
draw_cube(int(playerPos.x), int(playerPos.y), int(playerPos.z), 40, GLASS)
