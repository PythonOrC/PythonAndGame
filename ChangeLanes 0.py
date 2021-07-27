#
#! analyze what need to be done before starting
# * create a window
# * create road + car
# * have the car moving along the road
# * control the car
# * create obstacles
# * status bar (distance health)
# * remove health
# * eend game

# Step 0: initialize window

from arcade import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Change Lanes"


class MyCar(Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        pass
        # just a placeholder

    def on_draw(self):
        start_render()

    def on_update(self, delta_time):
        pass
        # just a placeholder


if __name__ == "__main__":
    game = MyCar(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    run()
