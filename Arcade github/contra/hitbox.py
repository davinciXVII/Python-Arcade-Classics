import arcade

class Line(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("hitbox.png")
        self.set_position(x,y)
