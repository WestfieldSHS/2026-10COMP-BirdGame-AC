# Aaron Chan
# start modules
import pgzrun, sys
from random import *

# create constants
WIDTH = 800
HEIGHT = 600
tick = 0
score = 0
high = int(open("highscore.txt").read())
gameOver = False

# print welcome
print('Welcome!\nThis game is about to start!\nClick the mouse to "flap" upwards\nDodge the pipes and the floor\nGood luck and have fun!')

# make background
background = Actor("day")
background.x = 400
background.y = 300

# make bird
bird = Actor("bird_wingsup")
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
        screen.draw.text("Game Over!", center = (400, 250), fontsize = 60)
        screen.draw.text(f"Score: {score}", center = (400, 300), fontsize = 40)
        screen.draw.text(f"High Score: {high}", center = (400, 350), fontsize = 40)
    else:
    # draw background
        background.draw()
    # draw characters
        bird.draw()
        for pipe in pipelist:
            drawPipe(pipe)
    # draw score
        screen.draw.text(f"{score}", center = (400, 40), color = (255, 255, 255), fontsize = 80)

def updatePipe(self, bird):
    global score, gameOver, high
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
            if high < score:
                high = score
                with open("highscore.txt", "w") as f:
                    f.write(str(high))
    # bird hits pipes
    for pipe in pipelist:
        for part in [pipe.top, pipe.bottom]:
            if part.colliderect(bird):
                gameOver = True

# update everything
def update():
    global score, gameOver, tick
    tick += 1
    if tick == 29:
        tick = 0
    # update bird
    bird.y = bird.y + 2
    if tick == 7 or tick == 14 or tick == 21 or tick == 28:
        bird.image = "bird" + str(int(tick/7))
    # update pipes
    for pipe in pipelist:
        updatePipe(pipe, bird)

    # bird hits bottom of screen
    if bird.y > 600:
        gameOver = True
    elif bird.y < 0:
        bird.y = 0

# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go()