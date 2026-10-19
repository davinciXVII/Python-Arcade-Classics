import arcade
from constants import *


class Plant(arcade.Sprite):
    def __init__(self,hp,cost,window):
        super().__init__(scale=0.1)
        self.hp=hp
        self.cost=cost
        self.window=window
        self.i=0
        self.time=0
        self.row=-1
        #создать 4 класса наследующийся от плента 

    def update(self,delta_time=1/60):
        self.time+=delta_time
        if self.time>0.3:
            self.time=0
            self.set_texture(self.i)
            self.i+=1
            if self.i>=len(self.textures):
                self.i=0
        
    def positioning(self,row,col):
        x=245-41+82*col
        y=30-50+100*row
        self.set_position(x,y)
        self.row=row-1
        