from pico2d import *
import random
class Boy:
    global ran
    def __init__(self):
        self.x, self.y = random.randint(0, 800), random.randint(90, 600)
        #ran = rnadom.randint(0,1)
        self.frame = 0
        self.image = load_image('run_animation.png')
#10
    def update(self):
        self.frame = random.randint(0, 7)
        #self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
#21
    def draw(self):
        self.image.draw(400, 30)
#24
def handle_events():
    global running
    global x
    global y
    global addmove
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            running = False

        if event.key == SDLK_RIGHT:
            if event.key == SDL_KEYDOWN:
                addmove = true
       #elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
        #    addmove = False  40
#41
open_canvas()
#ran = rnadom.randint(0,1)
character = load_image('run_animation.png')
team = [Boy() for i in range(11)]
grass = Grass()
addmove = False
running = True;
x = 10
while running:
    handle_events()
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    #ran = rnadom.randint(0,1) 52
    for boy in team:
        boy.update()
    clear_canvas()
    grass.draw()

    if addmove == True:
        x += xmove

    for boy in team:
        boy.draw()

    update_canvas()

    delay(0.05)

close_canvas()