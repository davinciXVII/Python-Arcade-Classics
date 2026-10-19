from const import *
import arcade 
import math
import exp


class Tank(arcade.Sprite):
    def __init__(self,window):
        super().__init__("TANK.png",scale=0.12)
        self.angle=0
        self.part_x=0
        self.part_y=1
        self.window=window
        self.hp=10

    def update(self):
        self.temp=self.angle
        self.angle+=self.change_angle
        if self.collision_check():
            self.angle=self.temp
        self.temp=(self.center_x,self.center_y)
        self.part_x=math.cos(math.radians(self.angle))
        self.part_y=math.sin(math.radians(self.angle))
        self.center_x+=self.change_x*self.part_x
        self.center_y+=self.change_y*self.part_y
        if self.collision_check():
            self.set_position(self.temp[0],self.temp[1])

        for i in arcade.check_for_collision_with_list(self,self.window.shells):
            if  not i.tank==self:

                if self.hp>0:
                    self.hp-=1
                self.window.exps.append(exp.Exp(i))
                i.kill()
        
    def draw(self):
        super().draw()
        if self.hp>0:

            arcade.draw_rectangle_outline(self.center_x,self.center_y+50,72,8,(0,0,0),1)
            arcade.draw_rectangle_filled(self.center_x,self.center_y+50,70,6,(255,0,0))
            arcade.draw_rectangle_filled(self.center_x-(3.5*(10-self.hp)),self.center_y+50,7*self.hp,6,(0,255,0))


    def collision_check(self):
        if arcade.check_for_collision_with_list(self,self.window.bases) :
            return  True
        
        if arcade.check_for_collision_with_list(self,self.window.enemys):
            return True
        return False




    