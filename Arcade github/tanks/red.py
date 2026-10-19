import arcade
import shell
from const import *
import math
import exp
import random


class Tank(arcade.Sprite):
    def __init__(self,window):
        super().__init__("red.png",scale=0.12)
        self.angle=180
        self.change_x=1/2
        self.change_y=1/2
        self.hp=5
        self.window=window
        self.time=0

    def update(self):
        self.time+=1/60
        if self.hp>0:
            radius=arcade.get_distance_between_sprites(self,self.window.player)
            if radius<250:
                self.temp=self.angle
                delta_x=self.window.player.center_x-self.center_x 
                delta_y=self.window.player.center_y-self.center_y
                self.angle=math.degrees(math.atan2(delta_y,delta_x))
                if self.colission_check():
                    self.angle=self.temp
            else:
                self.angle=180

            self.part_x=math.cos(math.radians(self.angle))
            self.part_y=math.sin(math.radians(self.angle))
            self.temp=(self.center_x,self.center_y)
            self.center_x+=self.change_x*self.part_x
            self.center_y+=self.change_y*self.part_y
            if self.colission_check():
                self.set_position(self.temp[0],self.temp[1])
        else:
            self.texture=arcade.load_texture('deadred.png')
        for i in arcade.check_for_collision_with_list(self,self.window.shells):
            if  not i.tank==self:

                if self.hp>0:
                    self.hp-=1
                self.window.exps.append(exp.Exp(i))
                i.kill()
        if self.time>3 and self.hp>0:
            self.window.shells.append(shell.Shell(self,self.window))
            self.time=random.randint(-2,2)
            
    def draw(self):
        super().draw()
        if self.hp>0:

            arcade.draw_rectangle_outline(self.center_x,self.center_y+50,52,8,(0,0,0),1)
            arcade.draw_rectangle_filled(self.center_x,self.center_y+50,50,6,(255,0,0))
            arcade.draw_rectangle_filled(self.center_x-(5*(5-self.hp)),self.center_y+50,10*self.hp,6,(0,255,0))

    def colission_check(self):
        if arcade.check_for_collision_with_list(self,self.window.bases) :
            return  True
        if arcade.check_for_collision(self,self.window.player):
            return True
        if arcade.check_for_collision_with_list(self,self.window.enemys):
            return True
        return False
                   