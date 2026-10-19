import arcade
import random

class Exp(arcade.Sprite):
    def __init__(self,shell,scale=1):
        super().__init__(scale=scale)
        self.set_position(shell.center_x,shell.center_y)
        if shell.define=="base":
            self.center_x+=random.randint(-80,80)
            self.center_y+=random.randint(-80,80)


        for i in range(13):
            self.textures.append(arcade.load_texture(f"exp/exp{i+1}.png"))
        self.i=0
        self.time=0

    def update(self):
        self.time+=1/60
        if self.time>0.03:
            self.time=0
            self.set_texture(self.i)
            self.i+=1
            if self.i==len(self.textures):
                self.kill()