import arcade
import random as rnd

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN_TITLE="StarWars"
SPEED=10

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("pics/falcon.png",0.3)
        self.center_x=SCREEN_WIDTH/2
        self.center_y=SCREEN_HEIGHT/6
        self.explode=False
        self.time=0
        self.destruction=arcade.load_sound("audio/exp.wav")

    def update(self):
        self.center_x+=self.change_x
        if self.explode:
            self.time+=0.016
            if self.time>0.5:
                window.play=False

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__("pics/TieFighter.png",0.2)
        self.angle=90
        self.change_y=SPEED/5
        self.explode=False
        self.time=0
        self.destruction=arcade.load_sound("audio/exp.wav")

    def update(self):
        self.center_y-=self.change_y
        if self.explode:
            self.time+=0.16
            if self.time:
                self.kill()

        if self.top<0:
            window.fails+=1
            self.kill()
    
class Explosion(arcade.Sprite):
    def __init__(self,scale=1):
        super().__init__(scale=scale)
        for i in range(1,14):
            self.append_texture(arcade.load_texture(f"pics/exp/exp{i}.png"))
        self.i=0
        self.time=0
        self.change_y=SPEED/5
    
    def update(self):
        self.center_y-=self.change_y
    
    def update_animation(self,delta_time):
        self.time+=delta_time
        if self.time>0.1:
            self.time=0
            self.set_texture(self.i)
            self.i+=1
            if self.i==13:
                self.kill()


class Laser(arcade.Sprite):
    def __init__(self):
        super().__init__("pics/laser.png",0.7)
        self.center_x=window.player.center_x
        self.bottom=window.player.top
        self.change_y=SPEED
        self.laser_sound=arcade.load_sound("audio/laser.wav")
        arcade.play_sound(sound=self.laser_sound,volume=0.7)
    def update(self):
        self.center_y+=self.change_y
        if self.bottom>SCREEN_HEIGHT:
            self.kill()

class Meteorit(arcade.Sprite):
    def __init__(self):
        super().__init__("pics/meteorit.png",scale=rnd.randint(5,10)/10)
        self.angle=rnd.randint(1,360)
        self.change_y=SPEED/10
        self.change_angle=rnd.randint(-3,3)
    
    def update(self):
        self.center_y-=self.change_y
        self.angle-=self.change_angle
        if self.top<0:
            self.kill()

        
            
    

class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.set_mouse_visible(0)
        self.bg=arcade.load_texture("pics/background.jpg")
        self.lost=arcade.load_texture("pics/lost.jpg")
        self.win=arcade.load_texture("pics/win.png")
        self.player=Player()
        self.lasers=arcade.SpriteList()
        self.enemys=arcade.SpriteList()
        self.explosions=arcade.SpriteList()
        self.meteorits=arcade.SpriteList()
        self.play=True
        self.fails=0
        self.bg_music=arcade.load_sound("audio/A New Hope.mp3")
        arcade.play_sound(sound=self.bg_music,volume=0.05)
        self.time=0
        self.setup()

    
    def setup(self):
        for i in range(15):
            temp=Meteorit()
            temp.center_x=rnd.randint(50,SCREEN_WIDTH-50)
            temp.center_y=SCREEN_HEIGHT+200*i
            self.meteorits.append(temp)
        for i in range(30):
            temp=Enemy()
            print(temp)
            temp.center_x=rnd.randint(50,SCREEN_WIDTH-50)
            temp.center_y=SCREEN_HEIGHT+200*i
            self.enemys.append(temp)

    
    def on_mouse_press(self,x: int, y: int, button: int, modifiers: int):
        if button==arcade.MOUSE_BUTTON_LEFT:
            temp=Laser()
            self.lasers.append(temp)

    def on_draw(self):
        self.clear()
        if self.play:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.bg)
            self.meteorits.draw()
            self.player.draw()
            self.lasers.draw()
            self.enemys.draw()
            self.explosions.draw()
        elif not self.enemys:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.win)
        else:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.lost)


    def update(self,delta_time):
        #delta time это время прошедшие с предыдущего апдейта 
        self.time+=delta_time
        print(f"с предыдушего апдейта прошло {delta_time} сначала игры прошло {self.time}")
        if self.play:
            if not self.enemys:
                self.play=False
            self.player.update()
            self.lasers.update()
            self.enemys.update()
            self.meteorits.update()
            self.explosions.update()
            self.explosions.update_animation(delta_time)
            for laser in self.lasers:
                hit_list=arcade.check_for_collision_with_list(laser,self.enemys)
                if hit_list:
                    laser.kill()
                for hit in hit_list:
                    temp=Explosion()
                    arcade.play_sound(sound=hit.destruction,volume=1)
                    temp.center_x=hit.center_x
                    temp.center_y=hit.center_y
                    self.explosions.append(temp)
                    hit.explode=True
            if self.fails>5:
                self.play=False
            if arcade.check_for_collision_with_list(self.player,self.enemys) and not self.player.explode:
                temp=Explosion(scale=2)
                arcade.play_sound(sound=self.player.destruction,volume=1)
                temp.center_x=self.player.center_x
                temp.center_y=self.player.center_y
                self.explosions.append(temp)
                self.player.explode=True
        
    def on_mouse_motion(self,x,y,dx,dy):
        if self.play:
            self.player.center_x=x

        

window=Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

arcade.run()

 
