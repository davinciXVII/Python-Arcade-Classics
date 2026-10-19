import arcade
from plants import Plant






class Nut(Plant):
    def __init__(self,window):
        self.type=2
        super().__init__(hp=10,cost=50,window=window)
        self.textures=[]
        for i in range(1,4):
            self.textures.append(arcade.load_texture(f"plants/nut{i}.png"))
       