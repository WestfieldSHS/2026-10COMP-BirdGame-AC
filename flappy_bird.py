# start modules
import pgzrun
import sys

# create constants
WIDTH = 800
HEIGHT = 600

# print welcome
print('Welcome!\nThis game is about to start!\nClick the mouse to "flap" upwards\nDodge the pipes and the floor\nGood luck and have fun!')

# make background
background = Actor("bg")
background.x = 400
background.y = 300

# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300

# make pipes
class Pipes():
    def __init__(self, x, centre, gap):
        self.top = Actor("top")
        self.bottom = Actor("bottom")
        self.top.y = centre - (150 + gap/2)
        self.bottom.y = centre + 150 + gap/2
pipelist = [
    Pipes(266, 400, 220),
    Pipes(532, 180, 220),
    Pipes(798, 415, 220)
]

# draw everything to screen
def draw():
    # draw background
    background.draw()

    # draw characters
    bird.draw()
    for pipe in pipelist:
        pipe.top.draw()
        pipe.bottom.draw()

# update everything
def update():
    # update bird
    bird.y = bird.y + 1

    # update pipes

    # bird hits bottom of screen
    if bird.y > 600:
        print("Game Over!")
        sys.exit()

    # bird hits pipes

# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go()