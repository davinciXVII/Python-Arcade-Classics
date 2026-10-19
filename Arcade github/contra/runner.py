import arcade
from constant import *





class Enemy(arcade.Sprite):
    def __init__(self,x,window):
        self.i=0
        self.time=0
        super().__init__(scale=2)
        self.hp=3
        self.set_position(x,100)
        self.right_textures=[]
        self.left_textures=[]
        for i in range(1,10):
                self.left_textures.append(arcade.load_texture(f"runner/frame-0{i}.gif"))
                self.right_textures.append(arcade.load_texture(f"runner/frame-0{i}.gif",flipped_horizontally=True))
        self.direction="left"
        if x<0:
            self.change_x=1
            self.direction="right"
            self.textures=self.right_textures
            
        else:
            self.change_x=-1
            self.textures=self.left_textures
        self.set_texture(0)
        self.window=window

    def update(self):
        for bullet in arcade.check_for_collision_with_list(self,self.window.bullets):
            bullet.kill()
            self.hp-=1
            if self.hp<=0:
                self.kill()
        self.center_x+=self.change_x
        self.time+=1/60
        if self.time>0.05:
            self.time=0
            self.set_texture(self.i)
            self.i+=1
            if self.i==len(self.textures):
                self.i=0
        if self.direction=="left" and self.window.player.center_x>self.center_x:
            self.change_x=1
            self.direction="right"
            self.textures=self.right_textures
        if self.direction=="right" and self.window.player.center_x<self.center_x:
            self.change_x=-1
            self.textures=self.left_textures
            self.direction="left"
        

             
    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x,self.center_y+45,32,7,(255,255,255),1)
        arcade.draw_rectangle_filled(self.center_x,self.center_y+45,30,5,(255,30,0))
        arcade.draw_rectangle_filled(self.center_x-(3-self.hp)*5,  self.center_y+45,  self.hp*10,5,(255,255,0))
                

            


        


      

