import arcade
from constants import *







class Zombie(arcade.Sprite):
    def __init__(self,row,game,hp):
        super().__init__("zombies/OrdinaryZombie/Zombie_0.png",scale=0.8)
        self.row=row
        self.game=game
        game.zombie_rows[row]+=1
        self.center_y=80+100*row
        self.left=SCREENWIDTH
        self.change_x=0.2
        self.time=0
        self.i=0
        self.hp=hp

    
    def update(self):
        if self.center_x<100:
            self.game.play=False
            self.game.lost=True
        self.center_x-=self.change_x
        self.time+=1/60
        if self.time>0.1:
            self.time=0
            if self.i>=len(self.textures):
                self.i=0
            self.set_texture(self.i)
            self.i+=1
        if self.hp<=0:
            self.game.zombie_rows[self.row]-=1
            self.kill()
        self.change_x=0.2
        for i,plant in enumerate(self.game.field[self.row]):
            if plant:
                if plant.texture and arcade.check_for_collision(self,plant):
                    plant.hp-=1/15
                    self.change_x=0
                    if plant.hp<0:
                        plant.kill()
                        self.game.field[self.row][i]=None

class Ozombie(Zombie):
    def __init__(self,row,game):
        super().__init__(row,game,3)
        for i in range(22):
            self.textures.append(arcade.load_texture(f"zombies/OrdinaryZombie/Zombie_{i}.png"))
        self.set_texture(0)


class Bzombie(Zombie):
    def __init__(self,row,game):
        super().__init__(row,game,10)
        self.textures.clear()
        for i in range(15):
            self.textures.append(arcade.load_texture(f"zombies/BucketheadZombie/BucketheadZombie_{i}.png"))
        self.set_texture(0)

class Czombie(Zombie):
    def __init__(self,row,game):
        super().__init__(row,game,5)
        self.textures.clear()
        for i in range(21):
            self.textures.append(arcade.load_texture(f"zombies/ConeheadZombie/ConeheadZombie_{i}.png"))
        self.set_texture(0)



        