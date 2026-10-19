import arcade

class Money(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("sun.png",scale=0.1)
        self.set_position(x,y)
        self.change_y=1
        self.change_x=1
    def update(self):
        self.center_y+=self.change_y
        self.center_x+=self.change_x
        self.angle+=0.1
        if self.change_x>0:
            self.change_x-=0.01
        if self.change_y>-1:
            self.change_y-=0.01
        if self.top<0:
            self.kill()