"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
from random import randint

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "aaaa"
colisoes = []

def set_colision(x, y):
    colisoes.append(x)
    colisoes.append(y)

def confirm_colision(o):
    if o in colisoes:
        return True
    else:
        return False


class MyGame(arcade.Window):


    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        
       
        self.color = arcade.color.ROCKET_METALLIC
        self.backcolor = arcade.color.COOL_BLACK

        self.player_x = 100
        self.player_y = 200
        self.player_speed = 250
        self.life_color_state = arcade.color.GRANNY_SMITH_APPLE


        self.box_y = 100
        self.box_x = 100
        set_colision(self.box_y, self.box_y)

        self.right = False
        self.left  = False
        self.up    = False
        self.down  = False

        arcade.set_background_color(self.backcolor)



    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_rectangle_filled(self.box_x, self.box_y, 20,20, self.color)

        arcade.draw_circle_outline(self.player_x, self.player_y, 10, arcade.color.DARK_GRAY, 2, 50)
        arcade.draw_circle_filled(self.player_x, self.player_y, 8, self.life_color_state)


    def on_update(self, delta_time):
        
        if confirm_colision(self.player_x) and confirm_colision(self.player_y):
            self.life_color_state = arcade.color.RED
        else:
            self.life_color_state = arcade.color.GRANNY_SMITH_APPLE
        
        if self.right:
            if self.player_x + self.player_speed * delta_time > SCREEN_WIDTH:
                player_speed = 0
            else:
                self.player_x += self.player_speed * delta_time

        if self.left:
            if self.player_x - self.player_speed * delta_time < SCREEN_WIDTH:
                player_speed = 0
            else:
                self.player_x -= self.player_speed * delta_time

        if self.up:
            if self.player_y + self.player_speed * delta_time > SCREEN_HEIGHT:
                player_speed = 0
            else:
                self.player_y += self.player_speed * delta_time
            
        if self.down:
            if self.player_y - self.player_speed * delta_time < SCREEN_HEIGHT:
                player_speed = 0
            else:
                self.player_y -= self.player_speed * delta_time


    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.right = True
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.left = True
        if symbol == arcade.key.UP or symbol == arcade.key.W:
            self.up = True
        if symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.down = True
    
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.right = False
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.left = False
        if symbol == arcade.key.UP or symbol == arcade.key.W:
            self.up = False
        if symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.down = False



def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
