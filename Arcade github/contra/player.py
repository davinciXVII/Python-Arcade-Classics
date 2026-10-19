import arcade
from constant import *
import exp

class Player(arcade.Sprite):
    def __init__(self,window):
        super().__init__("bill_textures/BillWalkingR.gif",scale=2)
        self.set_position(100,100)
        self.window=window
        self.direction="right"
        self.left_text=[]
        self.right_text=[]
        for i in range(6):
            self.right_text.append(arcade.load_texture(f"go_bill/{i}.gif"))
            self.left_text.append(arcade.load_texture(f"go_bill/{i}.gif",flipped_horizontally=True))
        self.textures=self.right_text
        self.timer=0
        self.i=0 
        self.hp=15

        
        
    def update(self,delta_time):
        if self.direction=="right" and self.change_x<0:
            self.direction="left"
            self.textures=self.left_text
        if self.direction=="left" and self.change_x>0:
            self.direction="right"
            self.textures=self.right_text

        self.center_x+=self.change_x
        if self.window.index_bg==0  and self.left<0:
            self.left=0
        if self.window.index_bg==14  and self.left<0:
            self.left=0
        if self.window.index_bg==13 and self.right>SCREENWIDTH:
            self.right=SCREENWIDTH
        for enemy in arcade.check_for_collision_with_list(self,self.window.enemys):
            self.window.exps.append(exp.Exp(enemy.center_x,enemy.center_y))
            self.hp-=1
            enemy.kill() 




        self.timer+=delta_time
        if self.timer>0.1:
            self.timer=0
            if self.i>=len(self.textures) or self.change_x==0:              
                self.i=0
            self.set_texture(self.i)
            self.i+=1
            

    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x,self.center_y+45,62,7,(255,255,255),1)
        arcade.draw_rectangle_filled(self.center_x,self.center_y+45,60,5,(255,30,0))
        arcade.draw_rectangle_filled(self.center_x-(15-self.hp)*2,self.center_y+45,self.hp*4,5,(0,255,0))

        