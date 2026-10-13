# Aaron Chan
# start modules
import pgzrun
import sys

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
    def __init__(self, x, centre, gap):
        self.top = Actor("top")
        self.bottom = Actor("bottom")
        self.top.x = x
        self.bottom.x = x
        self.top.y = centre - (300 + gap/2)
        self.bottom.y = centre + 300 + gap/2
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
    global score
    global gameOver
    # update bird
    bird.y = bird.y + 1

    # update pipes
    for pipe in pipelist:
        pipe.top.x -= 1
        pipe.bottom.x -= 1
        if pipe.top.x < -44:
            pipe.top.x = 844
            pipe.bottom.x = 844
            if not gameOver:
                score += 1

    # bird hits bottom of screen
    if bird.y > 600:
        print("Game Over!")
        print(f"Score: {score}")
        gameOver = True

    # bird hits pipes
    for pipe in pipelist:
        for part in [pipe.top, pipe.bottom]:
            if part.colliderect(bird):
                print("Game Over!")
                print(f"Score: {score}")
                gameOver = True

# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go()