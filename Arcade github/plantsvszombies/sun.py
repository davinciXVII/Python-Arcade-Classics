import arcade
from plants import Plant
import time
import money






class Sun(Plant):
    def __init__(self,window):
        self.type=1
        super().__init__(hp=10,cost=50,window=window)
        self.textures=[]
        self.timer=time.time()
        for i in range(1,3):
            self.textures.append(arcade.load_texture(f"plants/sun{i}.png"))

    def update(self):
        super().update()
        if time.time()-self.timer>10:
            self.window.suns.append(money.Money(self.center_x,self.center_y))
            self.timer=time.time()
        