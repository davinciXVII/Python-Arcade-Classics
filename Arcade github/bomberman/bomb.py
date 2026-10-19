import arcade
import random as rnd

SCREEN_TITLE = "BOMBERMAN"
CELL = 60
ROWS = 11
COLS = 11
SCREEN_HEIGHT = CELL * ROWS
SCREEN_WIDTH = CELL * COLS

# Safe spawn zones for players where destructible blocks cannot spawn
FORBIDDEN = [(0,0), (0,1), (0,2), (0,3), (1,0), (2,0), (3,0), 
             (COLS-1, ROWS-1), (COLS-1, ROWS-4), (COLS-2, ROWS-1), 
             (COLS-3, ROWS-1), (COLS-4, ROWS-1), (COLS-1, ROWS-2), (COLS-1, ROWS-3)]

class Bomb(arcade.Sprite):
    def __init__(self, power):
        super().__init__(scale=0.7)
        self.i = 0
        self.power = power
        self.time = 0
        self.time_e = 0
        
        # Safe audio asset loading protection
        try:
            self.destr = arcade.load_sound("audio/retro-explode-2-236688.mp3")
        except Exception:
            self.destr = None

        # Loading animated textures for the bomb ticker
        for i in range(3):
            self.textures.append(arcade.load_texture(f"Bomb/Bomb_f0{i}.png"))
            
    def update_animation(self, delta_time):
        # Handle regular ticking animation speed
        self.time += delta_time
        if self.time > 0.1:
            self.time = 0
            self.set_texture(self.i)
            self.i += 1
            if self.i == len(self.textures):
                self.i = 0
                
        # Detonate the bomb exactly after 3 seconds of ticking
        self.time_e += delta_time
        if self.time_e > 3:
            directions = ["LEFT", "RIGHT", "UP", "DOWN"]

            # Calculate flame propagation based on current blast power
            for i in range(1, self.power + 1):
                local_directions = directions.copy()
                for d in local_directions:
                    temp = Flame()
                    temp.set_position(self.center_x, self.center_y)
                    
                    # Stop drawing fire vector if it collides with solid walls
                    if d == "LEFT":
                        temp.center_x -= CELL * i
                        if arcade.check_for_collision_with_list(temp, window.walls):
                            directions.remove("LEFT")
                            temp.kill()
                            continue

                    if d == "RIGHT":
                        temp.center_x += CELL * i
                        if arcade.check_for_collision_with_list(temp, window.walls):
                            directions.remove("RIGHT")
                            temp.kill()
                            continue
                    
                    if d == "UP":
                        temp.center_y += CELL * i
                        if arcade.check_for_collision_with_list(temp, window.walls):
                            directions.remove("UP")
                            temp.kill()
                            continue

                    if d == "DOWN":
                        temp.center_y -= CELL * i
                        if arcade.check_for_collision_with_list(temp, window.walls):
                            directions.remove("DOWN")
                            temp.kill()
                            continue
                            
                    window.flames.append(temp)
                    
            if self.destr:
                arcade.play_sound(self.destr)
            self.kill()

class PowerUp(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.i = rnd.randint(0, 2)
        # Load upgrade perks assets dynamically
        for name in ["Bomb", "Flame", "Speed"]:
            self.textures.append(arcade.load_texture(f"Powerups/{name}Powerup.png"))
        self.set_texture(self.i)

    def update(self):
        # Apply attribute buffs instantly when player overlaps the item
        for p in arcade.check_for_collision_with_list(self, window.players):
            if self.i == 0:
                p.power += 1
            if self.i == 2:
                p.speed += 1
            self.kill()

class Flame(arcade.Sprite):
    def __init__(self):
        super().__init__("Flame/Flame_f00.png", scale=0.7)
        for i in range(1, 5):
            self.textures.append(arcade.load_texture(f"Flame/Flame_f0{i}.png"))
        self.i = 0
        self.time = 0
        self.time_e = 0
        
    def update_animation(self, delta_time):
        # Reduce user HP on dangerous flame collision overlapping
        for p in arcade.check_for_collision_with_list(self, window.players):
            p.hp -= 1
            self.kill()
            return
        if arcade.check_for_collision_with_list(self, window.walls):
            self.kill()
            return
            
        self.time += delta_time
        if self.time > 0.1:
            self.time = 0
            self.set_texture(self.i)
            self.i += 1
            if self.i == len(self.textures):
                self.i = 0
                
        # Fade out explosion effect quickly within 0.5s time frame
        self.time_e += delta_time
        if self.time_e > 0.5:
            self.kill()

class Walls(arcade.Sprite):
    def __init__(self):
        super().__init__("tiles/SolidBlock.png", scale=1)

class Destructible(arcade.Sprite):
    def __init__(self):
        super().__init__("tiles/ExplodableBlock.png", scale=1)
        
    def update(self):
        # Destroy brick on fire impact and trigger potential upgrade drops
        if arcade.check_for_collision_with_list(self, window.flames):
            if rnd.randint(1, 3) == 1:
                temp = PowerUp()
                temp.set_position(self.center_x, self.center_y)
                window.bonuses.append(temp)
            self.kill()

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(scale=0.5)
        self.isactive = True
        self.speed = 2
        self.power = 3
        self.hp = 3
        self.direction = "Down"
        self.i = 0
        self.time = 0
        self.moving = False
        self.pref_coord = (self.center_x, self.center_y)
        
        self.back = []
        self.front = []
        self.side_l = []
        self.side_r = []
        
        # Load full directional graphic spritesheets for character setup
        for i in range(8):
            self.back.append(arcade.load_texture(f"player/Back/Bman_B_f0{i}.png"))
            self.front.append(arcade.load_texture(f"player/Front/Bman_F_f0{i}.png"))
            self.side_l.append(arcade.load_texture(f"player/Side/Bman_S_f0{i}.png", flipped_horizontally=True))
            self.side_r.append(arcade.load_texture(f"player/Side/Bman_S_f0{i}.png"))
        self.textures = self.front
        self.set_texture(0)
    
    def update(self, delta_time):
        if self.isactive:
            if self.hp < 1:
                self.color = (0, 0, 0)
                self.isactive = False
                window.play = False
            if self.speed > 6:
                self.speed = 6         
                
            # Process discrete step grid calculations 
            if self.moving:
                if self.direction == "RIGHT":
                    self.center_x += self.new_speed
                    if self.center_x >= self.pref_coord[0] + CELL:
                        self.center_x = self.pref_coord[0] + CELL
                        self.moving = False
                if self.direction == "LEFT":
                    self.center_x -= self.new_speed
                    if self.center_x <= self.pref_coord[0] - CELL:
                        self.center_x = self.pref_coord[0] - CELL
                        self.moving = False
                if self.direction == "UP":
                    self.center_y += self.new_speed
                    if self.center_y >= self.pref_coord[1] + CELL:
                        self.center_y = self.pref_coord[1] + CELL
                        self.moving = False
                if self.direction == "DOWN":
                    self.center_y -= self.new_speed
                    if self.center_y <= self.pref_coord[1] - CELL:
                        self.center_y = self.pref_coord[1] - CELL
                        self.moving = False
                        
                # Revert movement steps safely if wall crash boundary detected
                if arcade.check_for_collision_with_list(self, window.walls) or arcade.check_for_collision_with_list(self, window.destructible):
                    self.set_position(self.pref_coord[0], self.pref_coord[1])
                    self.moving = False
            else:
                self.pref_coord = (self.center_x, self.center_y)
                self.new_speed = self.speed

    def update_animation(self, delta_time = 1 / 60):
        # Freeze frame loops instantly if player stops moving
        if not self.moving:
            self.i = 0
        else:
            self.time += delta_time
            if self.time > 0.05:
                self.time = 0
                self.i += 1
                if self.i == len(self.textures):
                    self.i = 0
        self.set_texture(self.i)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.walls = arcade.SpriteList()
        self.destructible = arcade.SpriteList()
        self.bombs = arcade.SpriteList()
        self.flames = arcade.SpriteList()
        self.bonuses = arcade.SpriteList()
        self.players = arcade.SpriteList()
        self.play = True
        
        try:
            self.bg = arcade.load_texture("tiles/BackgroundTile.png")
            self.p1win = arcade.load_texture("P1WIN.png")
            self.p2win = arcade.load_texture("P2WIN.png")
        except Exception:
            self.bg = None

        self.setup()
        
    def setup(self):
        for x in range(COLS):
            for y in range(ROWS):
                if x % 2 != 0 and y % 2 != 0:
                    temp = Walls()
                    temp.center_x = ((x * CELL) + CELL / 2)
                    temp.center_y = ((y * CELL) + CELL / 2)
                    self.walls.append(temp)
                else:
                    if (x, y) not in FORBIDDEN and rnd.randint(1, 2) == 1:
                        temp = Destructible()
                        temp.center_x = ((x * CELL) + CELL / 2)
                        temp.center_y = ((y * CELL) + CELL / 2)
                        self.destructible.append(temp)
                        
        self.player_sprite = Player()
        self.player_sprite.set_position(CELL/2, CELL/2)
        self.players.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        if self.bg:
            arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.walls.draw()
        self.destructible.draw()
        self.bombs.draw()
        self.flames.draw()
        self.bonuses.draw()
        self.players.draw()

    def on_update(self, delta_time):
        self.players.update(delta_time)
        self.players.update_animation(delta_time)
        self.bombs.update_animation(delta_time)
        self.flames.update_animation(delta_time)
        self.destructible.update()
        self.bonuses.update()

if __name__ == "__main__":
    window = Game()
    arcade.run()

    
