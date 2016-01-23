from mc import *

mc = Minecraft()

def draw_wall(x, y, z, x_length, y_length, mcblock):
    for current_x in range(x, x+x_length):
        for current_y in range(y, y+y_length):
            mc.setBlock(current_x, current_y, z, mcblock)

def draw_square_wall(x, y, z, length, mcblock):
    pass

def draw_floor(x, y, z, length, mcblock):
    pass

playerPos = mc.player.getPos()
draw_rectangle(int(playerPos.x), int(playerPos.y), int(playerPos.z), 40, 40, GLASS)
