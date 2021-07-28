import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Change Lanes"


class Road:
    def __init__(self):
        self.image = arcade.Sprite("images/road.png")
        self.image.center_x = SCREEN_WIDTH // 2
        self.image.center_y = SCREEN_HEIGHT // 2


class SmallCar:
    def __init__(self):
        self.image = arcade.Sprite("images/smallcar1.png")
        self.image.center_x = SCREEN_WIDTH // 2
        self.image.center_y = 100


class MyCar(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        # initialize the road
        self.road = Road()
        # initialize the car
        self.small_car = SmallCar()

    def on_draw(self):
        arcade.start_render()

        self.road.image.draw()
        self.small_car.image.draw()

    def on_update(self, delta_time):
        pass


if __name__ == "__main__":
    game = MyCar(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
