
import arcade



class Exp(arcade.Sprite):
    def __init__(self,x,y,t=0):
        super().__init__(scale=1)
        for i in range(13):
            self.textures.append(arcade.load_texture(f"exp/exp{i+1}.png"))
        self.i=0
        self.time=0
        self.t=t
        self.set_position(x,y)

    def update(self,delta_time=1/60):
        if self.t>0:
            self.t-=delta_time
        else:
            self.t=0
        self.time+=delta_time
        if self.time>0.05 and self.t==0:

            self.time=0
            self.set_texture(self.i)
            self.i+=1
            if self.i==len(self.textures):
                self.kill()
