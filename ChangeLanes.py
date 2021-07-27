import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Change Lanes"


class MyCar(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        self.road = arcade.Sprite("images/road.png")
        self.road.center_x = 300
        self.road.center_y = 400

        # initialize the car
        self.small_car = arcade.Sprite("images/smallcar1.png")
        self.small_car.center_x = 300
        self.small_car.center_y = 100

    def on_draw(self):
        arcade.start_render()
        self.road.draw()
        self.small_car.draw()

    def on_update(self, delta_time):
        pass


if __name__ == "__main__":
    game = MyCar(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
