import arcade
from constants import *
from pea import *
from sun import *
from tree import *
from nut import *
import zombie
import time
import random

p_types=[Pea,Sun,Nut,Tree]
def finding(x,y):
    x-=245
    y-=30
    if x<=0 or y<=0:
        print(None)
    row=0
    col=0
    while y>0:
        y-=100
        row+=1
    while x>0:
        x-=82
        col+=1
    print(row,col)
    return (row,col)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREENWIDTH,SCREENHEIGHT,TITLE)
        self.bg=arcade.load_texture("bg.jpg")
        self.menu=arcade.load_texture("menu.png")
        self.menu_coords=[10+((SCREENHEIGHT-10)/4.7)/2,SCREENHEIGHT/2,(SCREENHEIGHT-10)/4.7,SCREENHEIGHT-10]
        self.menu_alpha=125
        self.seed=None
        self.field=[]
        for i in range(5):
            self.field.append([])
            for j in range(9):
                self.field[i].append(None)
        print(self.field)
        self.suns=arcade.SpriteList()
        self.towers=arcade.SpriteList()
        self.zombies=arcade.SpriteList()
        self.money=150
        self.zombie_timer=time.time()
        self.counter=0
        self.zombie_classes=[zombie.Ozombie,zombie.Czombie,zombie.Bzombie]
        self.i_zombie=0
        self.zombie_rows=[0,0,0,0,0]
        self.buls=arcade.SpriteList()
        self.play=True
        self.win=False
        self.lost=False
        self.bg_lost=arcade.load_texture("lost.png")
        self.bg_win=arcade.load_texture("win.png")
    def on_draw(self):
        self.clear()
        if self.play:
            arcade.draw_texture_rectangle(SCREENWIDTH/2,SCREENHEIGHT/2,SCREENWIDTH,SCREENHEIGHT,self.bg)
            arcade.draw_texture_rectangle(self.menu_coords[0],self.menu_coords[1],self.menu_coords[2],self.menu_coords[3],self.menu,0,self.menu_alpha)
            arcade.draw_text(str(self.money),40,490,font_size=30,color=(255,255,255,self.menu_alpha))
            self.towers.draw()
            self.zombies.draw()
            self.buls.draw()
            if self.seed:
                self.seed.draw()
            self.suns.draw()
        elif self.lost:
              arcade.draw_texture_rectangle(SCREENWIDTH/2,SCREENHEIGHT/2,SCREENWIDTH,SCREENHEIGHT,self.bg_lost)
        else:
              arcade.draw_texture_rectangle(SCREENWIDTH/2,SCREENHEIGHT/2,SCREENWIDTH,SCREENHEIGHT,self.bg_win)
    def update(self,delta_time):
        if self.play:

            self.towers.update()
            self.suns.update()
            self.zombies.update()
            self.buls.update()
        
            if self.seed:
                self.seed.update()
            if time.time()-self.zombie_timer>5 and len(self.zombies)< 10:
                self.zombie_timer=time.time()
                self.zombies.append(self.zombie_classes[random.randint(0,self.i_zombie)](random.randint(0,4),self))
                self.counter+=1
                
                if self.counter==10:
                    self.i_zombie=1
                if self.counter==20:
                    self.i_zombie=2
            if time.time()-self.zombie_timer>6 and len(self.zombies)< 1:
                self.play=False
                self.win=True
        #for tower in self.towers
    def on_mouse_motion(self, x, y, dx, dy):
        
        if x<self.menu_coords[0]+self.menu_coords[2]/2:
            
            self.menu_alpha=255
        else:
            self.menu_alpha=125
        if self.seed:
            self.seed.set_position(x,y)
            self.seed.alpha=200


    def on_mouse_press(self,x,y,button,mod):
        if button==1 and not self.seed:
            if 30<x<120:
                if 380<y<475:
                    print("sun")
                    self.seed=Sun(self)
                if 265<y<360:
                    print("pea")
                    self.seed=Pea(self)
                if 155<y<245:
                    print("nut")
                    self.seed=Nut(self)
                if 40<y<135:
                    print("tree")
                    self.seed=Tree(self)
                if self.seed:
                    self.seed.set_position(x,y)
            else:
                for i in self.suns:
                    if i.left<x<i.right and i.bottom<y<i.top:
                        i.kill()
                        self.money+=50
        
    def on_mouse_release(self, x, y, button, modifiers):
        if self.seed:
            row,col=finding(x,y)
            if not self.field[row-1][col-1] and self.money>=self.seed.cost and row and col:
                self.field[row-1][col-1]=self.plant_creation(row,col,self.seed)
                self.money-=self.seed.cost
                print(self.field)

            self.seed.kill()
            self.seed=None

    def plant_creation(self,row,col,plant):
        temp=p_types[plant.type](self)
        temp.positioning(row,col)
        self.towers.append(temp)
        return temp
        

       
            


Game()
arcade.run()
