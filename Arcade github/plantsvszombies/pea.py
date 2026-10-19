import arcade
from plants import Plant
import time


class Bul(arcade.Sprite):
    def __init__(self,window,x,y):
        super().__init__("bul.png",scale=0.1)
        self.set_position(x,y)
        self.window=window
        self.change_x=10
        self.textures.append(arcade.load_texture("firebul.png"))
        self.i=0
    
    def update(self):
        self.set_texture(self.i)
        self.center_x+=self.change_x
        for zombie in arcade.check_for_collision_with_list(self,self.window.zombies):
            zombie.hp-=self.i+1
            self.kill()

#прописать взаимодкйствие с зомби если он касается зомби то у зомби должно снять хп после чего горошенка исчезает

class Pea(Plant):
    def __init__(self,window):
        self.type=0
        super().__init__(hp=10,cost=100,window=window)
        self.textures=[]
        for i in range(1,4):
            self.textures.append(arcade.load_texture(f"plants/pea{i}.png"))
        self.bullet_time=time.time()

    def update(self):
        super().update()
        if self.row>-1:
            if self.window.zombie_rows[self.row] and time.time()-self.bullet_time>3:
                self.bullet_time=time.time()
                self.window.buls.append(Bul(self.window,self.center_x,self.center_y))

        