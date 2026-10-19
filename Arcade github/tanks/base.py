import arcade
import exp



class Base(arcade.Sprite):
    def __init__(self,img,window):
        super().__init__(img,scale=1.5)
        self.window=window
        self.hp=25
        self.define="base"
        self.i=0
        self.time=0
        





    def update(self):
        for shell in arcade.check_for_collision_with_list(self,self.window.shells):
            temp=exp.Exp(shell=shell)
            self.window.exps.append(temp)
            shell.kill()
            self.hp-=1
        if self.hp<=0 and self.i<10:
            if self.time>0.5:
                self.time=0
                self.i+=1
                self.window.exps.append(exp.Exp(self,scale=3))
            self.time+=1/60
        elif self.hp<=0:
            self.window.play=False
            if self.center_x<300:
                self.window.winner="red"
        




    def draw(self):
        super().draw()
        if self.hp>0:

            arcade.draw_rectangle_outline(self.center_x,self.center_y+300,256,15,(0,0,0),4)
            arcade.draw_rectangle_filled(self.center_x,self.center_y+300,250,9,(255,0,0))
            arcade.draw_rectangle_filled(self.center_x-(5*(25-self.hp)),self.center_y+300,10*self.hp,9,(0,255,0))
