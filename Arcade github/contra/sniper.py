import arcade
import bullet
import random






class Sniper(arcade.Sprite):
    def __init__(self,window,x,y,bg_index):
        super().__init__()
        self.down_left=arcade.load_texture("sniper/0.png")
        self.straight_left=arcade.load_texture("sniper/1.png")
        self.down_right=arcade.load_texture("sniper/0.png",flipped_horizontally=True)
        self.straight_right=arcade.load_texture("sniper/1.png",flipped_horizontally=True)
        self.set_position(x,y)
        self.window=window
        self.change_direction()
        self.bg_index=bg_index
        self.timer=0
        self.diag=0
        self.wait=3
        self.hp=3
        

    
    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x,self.center_y+45,32,7,(255,255,255),1)
        arcade.draw_rectangle_filled(self.center_x,self.center_y+45,30,5,(255,30,0))
        arcade.draw_rectangle_filled(self.center_x-(3-self.hp)*5,  self.center_y+45,  self.hp*10,5,(255,255,0))

#написать полоски для жизней 

    def change_direction(self):
        if self.center_x<self.window.player.center_x:
            self.direction="right"
            if self.center_y-20>self.window.player.center_y:
                self.texture=self.down_right
                self.diag=11
            else:
                self.texture=self.straight_right
                self.diag=0
        else:
            self.direction="left"
            if self.center_y-20>self.window.player.center_y:
                self.texture=self.down_left
                self.diag=11
            else:
                self.texture=self.straight_left
                self.diag=0

    def update(self,delta_time):
        if self.hp<=0:
            self.kill()
        self.change_direction()
        self.timer+=delta_time
        if self.timer>self.wait:
            self.wait=random.randint(2,6)
            self.timer=0
            if self.window.index_bg==self.bg_index:
                self.window.bullets.append(bullet.Bullet(self.window,self,self.diag))