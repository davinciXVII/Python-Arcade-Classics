import arcade
import random as rnd

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN_TITLE="dino"

class Animate(arcade.Sprite):
    i=0
    time=0
    def update_animation(self,delta_time):
        self.time+=delta_time
        if self.time>0.1 and len(self.textures)==3 or self.time>0.5:
            self.time=0
            self.set_texture(self.i)
            self.i+=1
            if self.i>len(self.textures)-1:
                self.i=0


class Dino(Animate):
    def update(self,delta_time):
        self.center_y+=self.change_y
        if self.change_y>-10:
            self.change_y-=0.5
        if self.center_y<SCREEN_HEIGHT/3:
            self.center_y=SCREEN_HEIGHT/3


class Cactus(Animate):
    accel=0.1
    cooldown=False
    def update(self):
        self.center_x-=self.change_x
        if self.right<0:
            self.left=SCREEN_WIDTH+rnd.randint(0,int(self.change_x*100))
            self.cooldown=False
            self.change_x+=self.accel
        



 




class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.bg=arcade.load_texture("pics/bg.png")
        self.win=arcade.load_texture("pics/win.png")
        self.game_over=arcade.load_texture("pics/game_over.png")
        self.player=Dino("pics/dino1.png",0.5)
        self.wall=Cactus("pics/cactus1.png",0.5)
        self.play=True
        self.points=0
        self.setup()
        self.load_records()
    def load_records(self):
        with open("records.txt") as file:
            self.record=int(file.read())

    def update(self,delta_time):
        if self.play:
            self.wall.update()
            self.player.update(delta_time)
            self.player.update_animation(delta_time)
            self.wall.update_animation(delta_time)
            if arcade.check_for_collision(self.player,self.wall):
                self.play=False
            if self.wall.center_x<self.player.center_x and not self.wall.cooldown:
                self.points+=1
                self.wall.cooldown=True
            with open("records.txt")as file:
                temp=int(file.read())
            if temp<self.points:
                self.record=self.points
                with open("records.txt","w")as file:
                    file.write(str(self.record))

        
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.SPACE:
            if self.player.center_y==SCREEN_HEIGHT/3:
                self.player.change_y=12
        
    

    def on_draw(self):
        self.clear()
        arcade.draw_text(f"record:{self.record}",SCREEN_WIDTH-150,SCREEN_HEIGHT-40,(0,0,0),30)
        if self.play:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
            self.player.draw()
            self.wall.draw()
            arcade.draw_text(f"points:{self.points}",100,SCREEN_HEIGHT-30,arcade.color.COOL_BLACK,30)
        else:
            if self.points<5:
                 arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.game_over)
            else:
                 arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.win)
#добавить рекорды

    def setup(self):
        self.player.center_y=SCREEN_HEIGHT/3
        self.player.center_x=SCREEN_WIDTH/5
        self.wall.center_y=SCREEN_HEIGHT/3
        self.wall.center_x=SCREEN_WIDTH
        self.wall.change_x=5
        self.player.append_texture(arcade.load_texture("pics/dino2.png"))
        self.player.append_texture(arcade.load_texture("pics/dino3.png"))
        self.wall.append_texture(arcade.load_texture("pics/cactus2.png"))



    









window=Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
arcade.run()
