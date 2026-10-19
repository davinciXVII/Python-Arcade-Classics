import arcade

WINDOW_WIDTH=600
WINDOW_HEIGHT=600
SPEED=2




class Ball(arcade.Sprite):
    def update(self):
        if self.right>WINDOW_WIDTH or self.left<0:
            self.change_x=-self.change_x
        self.center_x+=self.change_x
        if self.top>WINDOW_HEIGHT or self.bottom<0:
            self.change_y=-self.change_y
        self.center_y+=self.change_y
    

class Bar(arcade.Sprite):
    def update(self):
        self.center_x+=self.change_x




class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.ball=Ball("ball.png",scale=0.1)
        self.bar=Bar("bar.png",scale=0.1)
        self.score=0
        self.attemps=3
        self.play=True
        self.setup()
     
        
    
    def setup(self):
        self.ball.center_x=WINDOW_WIDTH/2
        self.ball.center_y=WINDOW_HEIGHT/2
        self.ball.change_x=4
        self.ball.change_y=4

        self.bar.center_x=WINDOW_WIDTH/2
        self.bar.center_y=20
       #сделать 3 попытки
   
    def on_draw(self):
        self.clear((0, 255, 255))
        self.bar.draw()
        self.ball.draw()
        arcade.draw_text(f"score:{self.score}",20,WINDOW_HEIGHT-30,(0,0,0),20)
        arcade.draw_text(f"attemps:{self.attemps}",20,WINDOW_HEIGHT-50,(0,0,0),20)
   
    def update(self, delta_time: float):
        if self.play:
            self.ball.update()
            #self.ball.change_x=SPEED
            #self.ball.change_y=SPEED+2
            self.bar.update()
            if arcade.check_for_collision(self.ball,self.bar):
                self.score=self.score+1
                #SPEED=SPEED+0.1
                self.ball.change_y=-self.ball.change_y
            if self.ball.bottom<=0:
                self.attemps=self.attemps-1 
                if self.attemps==0:
                    self.play=False
        
        
#добавить подушку и расположить что бы была оторвана от низа без дживения

    def on_key_press(self,key,x):
        if key==65361:
            self.bar.change_x=-5
        if key==65363:
            self.bar.change_x=5

    def on_key_release(self,key,x):
        if key==65361:
            self.bar.change_x=-0
        if key==65363:
            self.bar.change_x=0
    

        



window=Game(WINDOW_WIDTH,WINDOW_HEIGHT,"pingpong")
arcade.run()