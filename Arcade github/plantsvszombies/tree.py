import arcade
from plants import Plant






class Tree(Plant):
    def __init__(self,window):
        self.type=3
        super().__init__(hp=10,cost=175,window=window)
        self.textures=[]
        for i in range(1,4):
            self.textures.append(arcade.load_texture(f"plants/tree{i}.png"))




    def update(self):
        super().update()
        for bul in arcade.check_for_collision_with_list(self,self.window.buls):
            bul.i=1