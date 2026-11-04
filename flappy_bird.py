# Aaron Chan
# start modules
import pgzrun, sys
from random import *

# create constants
WIDTH = 800
HEIGHT = 623
tick = 0
birdtick = 0
score = 0
high = int(open("highscore.txt").read())
status = "menu"

# print welcome
print('Welcome!\nThis game is about to start!\nClick the mouse to "flap" upwards\nDodge the pipes and the floor\nGood luck and have fun!')

# make background
background = Actor("day")
background.x = 400
background.y = 300

# make title
title = Actor("logo")
title.x = 400
title.y = 200

# make bird
bird = Actor("bird1")
bird.x = 160
bird.y = 300

# make ground
ground1 = Actor("ground2")
ground1.x = 480
ground1.y = 611.5
ground2 = Actor("ground2")
ground2.x = 1440
ground2.y = 611.5

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
    # draw background
    background.draw()
    if status == "menu":
        # draw title
        title.draw()

    elif status == "game":
        # draw characters
        bird.draw()
        for pipe in pipelist:
            drawPipe(pipe)

        # draw score
        screen.draw.text(f"{score}", center = (400, 60), color = (255, 255, 255), fontname = "pixels", fontsize = 40, owidth = 2)


    else:
        # draw text
        title.draw()
        screen.draw.text(f"Score: {score}", center = (400, 300), fontsize = 40)
        screen.draw.text(f"High Score: {high}", center = (400, 350), fontsize = 40)
    # draw ground
    ground1.draw()
    ground2.draw()

def updatePipe(self, bird):
    global score, status, high
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
        if status == "game":
            score += 1
            if high < score:
                high = score
                with open("highscore.txt", "w") as f:
                    f.write(str(high))

    # bird hits pipes
    for pipe in pipelist:
        for part in [pipe.top, pipe.bottom]:
            if part.colliderect(bird):
                status = "over"

def bob(self):
    global tick
    if tick < 30:
        self.y += .5
    else:
        self.y -= .5

# update everything
def update():
    global score, status, tick, birdtick
    tick += 1
    if tick == 60:
        tick = 0
    for ground in [ground1, ground2]:
        ground.x -= 2
        if ground.x == -480:
            ground.x = 1440
    if status == "menu":
        bob(title)
        bob(bird)
    elif status == "game":
        birdtick += 1
        if birdtick == 29:
            birdtick = 1

        # update bird
        bird.y = bird.y + 2
        if birdtick == 7 or birdtick == 14 or birdtick == 21 or birdtick == 28:
            bird.image = "bird" + str(int(birdtick/7))

        # update pipes
        for pipe in pipelist:
            updatePipe(pipe, bird)

        # bird hits bottom of screen
        for ground in [ground1, ground2]:
            if ground.colliderect(bird):
                status = "over"
        if bird.y < 0:
            bird.y = 0

# moving
def on_mouse_down():
    global status
    bird.y = bird.y - 50
    if status == "menu":
        status = "game"

# runs everything
pgzrun.go()