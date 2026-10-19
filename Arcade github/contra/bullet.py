import arcade 
from constant import *
import player






class Bullet(arcade.Sprite):
    def __init__(self,window,gunner,diag=0):
        super().__init__("bullet.png",scale=0.05)
        self.set_position(gunner.center_x,gunner.center_y+10)
        self.window=window
        self.gunner=gunner
        self.diag=diag
        self.direction=gunner.direction
        if self.direction=="right":
            
            self.change_x=20-diag
        else:
            self.change_x=-20+diag

    def update(self):
        self.center_x+=self.change_x
        self.center_y-=self.diag
        if self.center_x<0 or self.center_x>SCREENWIDTH:
            self.kill()
        if type(self.gunner)==player.Player:
            for i in arcade.check_for_collision_with_list(self,self.window.snipers):
                i.hp-=1
                self.kill()
        else:
            if arcade.check_for_collision(self,self.window.player):
                self.window.player.hp-=1
                self.kill()
