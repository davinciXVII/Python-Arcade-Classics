import arcade
from const import *
import green
import base
import shell
import red










class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        self.bg=arcade.load_texture("BG.png")
        self.bases=arcade.SpriteList()
        self.shells=arcade.SpriteList()
        self.exps=arcade.SpriteList()
        self.enemys=arcade.SpriteList()
        self.play=True
        self.winner="green"


        self.setup()

    def setup(self):
        self.player=green.Tank(self)
        self.player.set_position(100,100)
        for pic in ["greenbase.png","redbase.png"]:
            temp=base.Base(pic,self)
            temp.center_y=SCREEN_HEIGHT/2
            temp.center_x=150+900*len(self.bases)
            self.bases.append(temp)
        #self.player2=
        #self.player2.set_position(50,50)
        for i in range(3):
            temp=red.Tank(self)
            temp.center_x=800
            temp.center_y=200+150*i
            self.enemys.append(temp)

        



    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.bg)
        self.player.draw()
        for bas in self.bases:
            bas.draw()
        self.shells.draw()
        for enemy in self.enemys:
            enemy.draw()
        self.exps.draw()
        
        #self.player2.draw()
        if not self.play:
            arcade.draw_text(f"{self.winner} is win ",SCREEN_WIDTH/2-40,SCREEN_HEIGHT/2,font_size=40)


    def update(self, delta_time):
        if self.play:
            self.player.update()
            self.shells.update()
            self.bases.update()
            self.exps.update()
            self.enemys.update()

        #self.player2.update()
        
    def on_key_press(self,key,modif):
        if key==arcade.key.LEFT:
            self.player.change_angle=2


        if key==arcade.key.RIGHT:
            self.player.change_angle=-2

        if key==arcade.key.UP:
            self.player.change_x=3
            self.player.change_y=3
        
        if key==arcade.key.DOWN:
            self.player.change_x=-2
            self.player.change_y=-2

        if key==arcade.key.SPACE:
            temp=shell.Shell(self.player,self)
            self.shells.append(temp)











    def on_key_release(self,key,modif):
        if key==arcade.key.LEFT:
            self.player.change_angle=0


        if key==arcade.key.RIGHT:
            self.player.change_angle=0


        if key==arcade.key.UP:
            self.player.change_x=0
            self.player.change_y=0
        
        if key==arcade.key.DOWN:
            self.player.change_x=0
            self.player.change_y=0
        

    











window=Game()
arcade.run()
