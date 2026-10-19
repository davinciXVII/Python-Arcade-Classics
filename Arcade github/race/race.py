import arcade 
import random as rnd

WINDOW_WIDTH=960
WINDOW_HEIGHT=720
WINDOW_TITLE="Race"
SPEED=5

class Car(arcade.Sprite):
    pass

class Wall(arcade.Sprite):
    accel=0
    down=False
    def update(self):
        self.change_y+=self.accel
        self.center_y-=self.change_y
        if self.top<0:
             self.bottom=WINDOW_HEIGHT+rnd.randint(0,300)
             self.left=rnd.randint(0,WINDOW_WIDTH-281)
             self.down=False

class BG(arcade.Sprite):
    accel=0
    def update(self):
        self.change_y+=self.accel
        self.center_y-=self.change_y
        if self.top<0 and self.change_y>0:
            self.bottom=WINDOW_HEIGHT
        if self.bottom>WINDOW_HEIGHT and self.change_y<0:
            self.top=0

            

class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.car=Car("yellow_car.png",0.9)
        self.road1=BG("bg.png")
        self.road2=BG("bg.png")
        self.brick=Wall("wall.png")
        self.play=True
        self.points=0
        self.setup()
        self.load_records()
    def load_records(self):
        with open("records.txt") as file:
            self.record=int(file.read())
#прописать управление автомобиля 
    def   on_draw(self):
        self.clear()
        self.road1.draw()
        self.road2.draw()
        self.brick.draw()
        self.car.draw()
        arcade.draw_text(f"score:{self.points}",20,WINDOW_HEIGHT-45,(0,0,0),40)
        arcade.draw_text(f"record:{self.record}",WINDOW_WIDTH-300,WINDOW_HEIGHT-45,(0,0,0),40)


    def setup(self):
        self.car.center_x=WINDOW_WIDTH/2
        self.car.center_y=WINDOW_HEIGHT/5
        self.road1.center_x=WINDOW_WIDTH/2
        self.road1.center_y=WINDOW_HEIGHT/2
        self.road2.center_x=WINDOW_WIDTH/2
        self.road2.bottom=WINDOW_HEIGHT
        self.road1.change_y=SPEED
        self.road2.change_y=SPEED
        self.brick.center_y=WINDOW_HEIGHT
        self.brick.left=rnd.randint(0,WINDOW_WIDTH-281)
        self.brick.change_y=SPEED



    def update(self,delta_time):
        if self.play:
            self.car.update()
            self.road1.update()
            self.road2.update()
            self.brick.update()
            if self.brick.center_y<self.car.center_y and self.brick.down==False:
                self.brick.down=True
                self.points+=1
        if arcade.check_for_collision(self.car,self.brick):
            self.play=False
            with open("records.txt")as file:
                temp=int(file.read())
            if temp<self.points:
                self.record=self.points
                with open("records.txt","w")as file:
                    file.write(str(self.record))




    def on_key_press(self,key,x):
        if key==65361:
            self.car.angle=15
            self.car.change_x=-5
        if key==65363:
            self.car.angle=-15
            self.car.change_x=5
        if key==arcade.key.UP:
            self.road1.accel=0.02
            self.road2.accel=0.02
            self.brick.accel=0.02
        if key==arcade.key.DOWN:
            self.road1.accel=-0.02
            self.road2.accel=-0.02
            self.brick.accel=-0.02

    def on_key_release(self,key,x):
        if key==65361 or key==65363:
            self.car.angle=0
            self.car.change_x=-0
        if key==arcade.key.UP or key==arcade.key.DOWN:
            self.road1.accel=0.0
            self.road2.accel=0.0
            self.brick.accel=0.0
        


   










window=Game(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_TITLE)
arcade.run()