# Aaron Chan
# start modules
import pgzrun
import sys
from random import *

# create constants
WIDTH = 800
HEIGHT = 600
score = 0
gameOver = False

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
    def __init__(self, x):
        gap = randint(80, 130)
        centre = randint(int(-250 + 300 + gap), int(850 - (300 + gap)))
        self.top = Actor("top")
        self.bottom = Actor("bottom")
        self.top.x = x
        self.bottom.x = x
        self.top.y = centre - (300 + gap)
        self.bottom.y = centre + 300 + gap
pipelist = [
    Pipes(666),
    Pipes(932),
    Pipes(1198), 
    Pipes(1464)
]

def drawPipe(self):
    self.top.draw()
    self.bottom.draw()

# draw everything to screen
def draw():
    if gameOver:
        # draw background
        screen.fill((194, 0, 0))
        # draw text
        screen.draw.text("Game Over!", center = (400, 275), fontsize = 60)
        screen.draw.text(f"Score: {score}", center = (400, 325), fontsize = 40)
    else:
    # draw background
        background.draw()
    # draw characters
        bird.draw()
        for pipe in pipelist:
            drawPipe(pipe)
    # draw score
        screen.draw.text(f"Score: {score}", topleft = (10, 10), color = (0, 0, 0), fontsize = 30)

def updatePipe(self, bird):
    global score, gameOver
    self.top.x -= 2
    self.bottom.x -= 2
    if self.top.x < -44:
        self.top.x = 1020
        self.bottom.x = 1020
        gap = randint(80, 130)
        centre = randint(int(-250 + 300 + gap), int(850 - (300 + gap)))
        self.top.y = centre - (300 + gap)
        self.bottom.y = centre + 300 + gap
    if self.top.x == 160:
        if not gameOver:
            score += 1
    # bird hits pipes
    for pipe in pipelist:
        for part in [pipe.top, pipe.bottom]:
            if part.colliderect(bird):
                gameOver = True

# update everything
def update():
    global score, gameOver
    # update bird
    bird.y = bird.y + 2

    # update pipes
    for pipe in pipelist:
        updatePipe(pipe, bird)

    # bird hits bottom of screen
    if not 0 < bird.y < 600:
        gameOver = True

# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go()