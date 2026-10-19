import arcade 
import random as rnd

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN_TITLE="Flappybird"
SPEED=4
GRAVITY=0.4



class Bird(arcade.Sprite):
    def __init__(self):
        super().__init__("pics/redbird-upflap.png",1)
        self.center_y=SCREEN_HEIGHT/2
        self.center_x=SCREEN_WIDTH/16
        self.angle=0
        self.append_texture(arcade.load_texture("pics/redbird-midflap.png"))
        self.append_texture(arcade.load_texture("pics/redbird-downflap.png"))
        self.append_texture(arcade.load_texture("pics/redbird-midflap.png"))
        self.i=0
        self.time=0
        self.wing=arcade.load_sound("audio/wing.wav")
        self.hit=arcade.load_sound("audio/hit.wav")

    def update(self):
        self.center_y+=self.change_y
        self.angle-=1
        self.change_y-=GRAVITY
        if self.center_y<0:
            window.play=False
    
    def update_animation(self, delta_time):
        self.time+=delta_time
        if self.time>0.1:
            self.time=0
            self.set_texture(self.i)
            self.i+=1
            if self.i==len(self.textures):
                self.i=0
        
        

    
     




class Pipe(arcade.Sprite):
    def __init__(self,is_up=False):
        super().__init__("pics/pipe.png",0.2,flipped_vertically=is_up)
        self.is_up=is_up
        self.point=arcade.load_sound("audio/point.wav")
        self.behind=False
    def update(self):
        self.center_x-=self.change_x
        if self.center_x<SCREEN_WIDTH/16 and not self.behind:
            self.behind=True
            window.points+=0.5
            if self.is_up:
                arcade.play_sound(self.point,0.5)

        if self.right<0:
            self.left=SCREEN_WIDTH
            self.behind=False
            if not self.is_up:
                self.center_y=rnd.randint(0,SCREEN_HEIGHT/8)
            else:
                self.center_y=rnd.randint(SCREEN_HEIGHT-SCREEN_HEIGHT/8,SCREEN_HEIGHT)

#прописать реакцию на пробел

class Paralax(arcade.Sprite):
    def update(self):
        self.center_x-=self.change_x
        if self.right<0:
            self.left=SCREEN_WIDTH


class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.play=True
        self.bg=arcade.load_texture("pics/bg.png")
        self.player=Bird()
        self.pipelist=arcade.SpriteList()
        self.clouds=arcade.SpriteList()
        self.sea=arcade.SpriteList()
        self.grass=arcade.SpriteList()
        self.points=0
        self.load_records()
        self.game_over=arcade.load_texture("pics/gameover.png")
        self.setup()


    def load_records(self):
        with open("records.txt") as file:
            self.record=int(file.read())
            print(self.record)

#сделать рекорды


    def setup(self):
        for i in range(3):
            pipe_bottom=Pipe()
            pipe_bottom.center_y=rnd.randint(0,SCREEN_HEIGHT/8)
            pipe_bottom.change_x=SPEED
            pipe_bottom.center_x=SCREEN_WIDTH+((SCREEN_WIDTH/2.7)*i)
            self.pipelist.append(pipe_bottom)
            pipe_up=Pipe(is_up=True)
            pipe_up.center_y=rnd.randint(SCREEN_HEIGHT-SCREEN_HEIGHT/8,SCREEN_HEIGHT)
            pipe_up.change_x=SPEED
            pipe_up.center_x=SCREEN_WIDTH+((SCREEN_WIDTH/2.7)*i)
            self.pipelist.append(pipe_up)
        
        for i in range(2):
            temp=Paralax("pics/grass.png",0.42)
            temp.bottom=-20
            temp.center_x=SCREEN_WIDTH*i
            temp.change_x=SPEED
            self.grass.append(temp)

            temp=Paralax("pics/sea.png",0.42)
            temp.bottom=20
            temp.center_x=SCREEN_WIDTH*i
            temp.change_x=SPEED/2
            self.sea.append(temp)

            temp=Paralax("pics/clouds.png",0.42)
            temp.bottom=60
            temp.center_x=SCREEN_WIDTH*i
            temp.change_x=SPEED/4
            self.clouds.append(temp)
    
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.bg)
        self.clouds.draw()
        self.sea.draw()
        self.pipelist.draw()
        self.grass.draw()
        self.player.draw()
        arcade.draw_text(f"points:{int(self.points)}",SCREEN_WIDTH/2,SCREEN_HEIGHT-60,(0,0,0),50)
        arcade.draw_text(f"record:{int(self.record)}",20,SCREEN_HEIGHT-60,(0,0,0),50)
        if not self.play:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,200,50,self.game_over)


    def update(self,delta_time):
        if self.play==True:
            self.pipelist.update()
            self.player.update()
            self.player.update_animation(delta_time)
            self.clouds.update()
            self.sea.update()
            self.grass.update()
            if arcade.check_for_collision_with_list(self.player,self.pipelist):
                self.play=False
                arcade.play_sound(self.player.hit,0.5)
                if self.points>self.record:
                    self.record=int(self.points)
                    with open("records.txt","w") as file:
                        file.write(str(self.record))

            
        

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.SPACE:
            if not self.play:
                self.restart()
            if self.player.center_y<SCREEN_HEIGHT:
                self.player.change_y=GRAVITY*15
                self.player.angle=45
                arcade.play_sound(self.player.wing,0.5)

    def restart(self):
        for pipe in self.pipelist:
            pipe.center_x+=SCREEN_WIDTH
        self.player.change_y=0
        self.player.center_y=SCREEN_HEIGHT/2
        self.player.center_x=SCREEN_WIDTH/16
        self.player.angle=0
        self.points=0
        self.play=True
            


window=Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

arcade.run()
