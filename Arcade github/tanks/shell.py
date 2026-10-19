import arcade
from const import *


class Shell(arcade.Sprite):
    def __init__(self,tank,window):
        super().__init__("shell.png",scale=0.1)
        self.tank=tank
        self.set_position(tank.center_x,tank.center_y)
        self.angle=tank.angle
        self.change_x=20*tank.part_x
        self.change_y=20*tank.part_y
        self.window=window
        self.define="shell"

    def update(self):
        self.center_x+=self.change_x
        self.center_y+=self.change_y
        if self.center_x<0 or self.center_x>SCREEN_WIDTH or self.center_y<0 or self.center_y>SCREEN_HEIGHT:
            self.kill()
        