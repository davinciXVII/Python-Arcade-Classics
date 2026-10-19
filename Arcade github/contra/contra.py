import arcade
from constant import *
import player
import hitbox
import runner
import bullet
import sniper
import exp
import time
import random



class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREENWIDTH,SCREENHEIGHT,SCREENTITLE)
        self.player=player.Player(self)
        #background list
        self.bg=[]
        for i in range(1,16):
            self.bg.append(arcade.load_texture(f"background/Map{i}.png"))
        self.index_bg=0
        #create list
        self.enemys=arcade.SpriteList()
        self.bullets=arcade.SpriteList()
        self.snipers=arcade.SpriteList()
        self.exps=arcade.SpriteList()
        #create hitboxes
        self.hb=arcade.SpriteList()
        for i in range(8):
            self.hb.append(hitbox.Line(x=50+i*100,y=65))
        self.change_hb(0)
        self.win=False
        self.fail=False
        self.tbc_bool=False
        self.t=None
        self.game_over=arcade.load_texture("image2.jpg")
        self.tbc=arcade.load_texture("image1.png")

        



        #creating a physics engine
        self.engine=arcade.PhysicsEnginePlatformer(self.player,self.hb,GRAVITY)
        #self.wall_explosion()
 

    def change_hb(self,dir):
        if dir:
            for enemy in self.enemys:
                enemy.center_x+=dir*SCREENWIDTH
            for enemy in self.snipers:
                enemy.center_x+=dir*SCREENWIDTH
            for exp in self.exps:
                exp.center_x+=dir*SCREENWIDTH



        
        while len(self.hb)>8:
            self.hb.pop()
        for coords in COORDS [self.index_bg]:
            x,y=coords
            self.hb.append(hitbox.Line(x,y))
        for _ in range(len(RUNNER[self.index_bg])):
            self.enemys.append(runner.Enemy(RUNNER[self.index_bg].pop(),self))
        for coords in COORDS_SNIPERS[self.index_bg]:
            if not coords[0]==None:
                self.snipers.append(sniper.Sniper(self,coords[0],coords[1],self.index_bg))
                coords[0]=None
                

    def on_draw(self):
        self.clear()
        if not self.fail and not self.tbc_bool:

            arcade.draw_texture_rectangle(SCREENWIDTH/2,SCREENHEIGHT/2,SCREENWIDTH,SCREENHEIGHT,self.bg[self.index_bg])

            self.player.draw()
            #self.hb.draw()
            self.bullets.draw()
            for i in self.enemys:
                i.draw()
            for i in self.snipers:
                i.draw()
            self.exps.draw()
        elif self.fail:
        
            arcade.draw_texture_rectangle(SCREENWIDTH/2,SCREENHEIGHT/2,SCREENWIDTH,SCREENHEIGHT,self.game_over)
        else:
            arcade.draw_texture_rectangle(SCREENWIDTH/2,SCREENHEIGHT/2,SCREENWIDTH,SCREENHEIGHT,self.tbc)
        
        

        



    def update(self,delta_time):
        if not self.fail and not self.tbc_bool:
            if self.player.hp<=0:
                self.fail=True
            self.player.update(delta_time)
            if self.player.center_x<0 and not self.win:
                self.index_bg-=1
                self.player.center_x=SCREENWIDTH
                self.change_hb(1)
            if self.player.center_x>SCREENWIDTH and not self.win:
                self.index_bg+=1
                self.player.center_x=0
                self.change_hb(-1)
            self.engine.update()
            self.enemys.update()
            self.bullets.update()
            for enemy in self.snipers:
                enemy.update(delta_time)
            self.exps.update()
            if len(self.enemys)==0 and self.index_bg==13 and not self.win:
                self.win=True
                self.t=time.time()
                self.wall_explosion()
            if self.win and time.time()-self.t>4:
                self.index_bg=14
            if self.index_bg==14 and self.player.center_x>SCREENWIDTH:
                self.tbc_bool=True

            
    def wall_explosion(self):
        for i in range(50):
            
            self.exps.append(exp.Exp(x=random.randint(round(SCREENWIDTH-SCREENWIDTH/5),SCREENWIDTH),
                                     y=random.randint(0,round(SCREENHEIGHT/1.1)),
                                     t=random.randint(1,50)/10))
        


            



    def on_key_press(self, symbol, modifiers):
        if symbol==arcade.key.LEFT:
            self.player.change_x=-5
        
        if symbol==arcade.key.RIGHT:
            self.player.change_x=5

        if symbol==arcade.key.UP and self.engine.can_jump():
            self.engine.jump(JUMP)
        
        if symbol==arcade.key.SPACE:
            self.bullets.append(bullet.Bullet(self,self.player))



    def on_key_release(self, symbol, modifiers):

        if symbol==arcade.key.LEFT:
            self.player.change_x=0
        
        if symbol==arcade.key.RIGHT:
            self.player.change_x=0


        


        
        








window=Game()
arcade.run()
