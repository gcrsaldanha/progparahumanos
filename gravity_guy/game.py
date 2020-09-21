import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Gravity Guy"

CHARACTER_SCALING = 0.5


class MyGame(arcade.Window):
    def __init__(self):
        # Create variables
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.player_list = None
        self.wall_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

    def setup(self):
        # Actually initializes variables with values
        # So it's easier to restart/replay the game later
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/alien/alienBlue_walk1.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        # Clear the screen to the background color
        arcade.start_render()

        # Draw sprites
        self.player_list.draw()
        self.wall_list.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
