import sys
sys.path.append('../LabsAll/Labs')

import random
from pico2d import *

running = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    image = None
    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.dir = 1#x방향의 벡터값
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('player.png')
        pass

    def update(self):
        if self.state == self.RIGHT_RUN:
            self.frame = (self.frame + 1) % 8
            self.x += (self.dir * 20)
        elif self.state == self.LEFT_RUN:
            self.frame = (self.frame + 1) % 8
            self.x += (self.dir * 20)
        #self.frame = (self.frame + 1) % 8
        #self.x += (self.dir * 10)#이동속도
        if self.x > 780:
            self.dir = -1
            self.x = 780
            self.state = self.LEFT_RUN
        elif self.x < 20:
            self.dir = 1
            self.x = 20
            self.state = self.RIGHT_RUN
        pass
#fsm 상태이상 머신?
#지능 : 이벤트에 반응하는 진행 (상태 먼너 찾기)
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 50, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def main():

    open_canvas()
    boy = Boy()
    grass = Grass()

    global running
    running = True
    while running:
        handle_events()

        boy.update()

        clear_canvas()
        grass.draw()
        boy.draw()
        update_canvas()

        delay(0.05)

    close_canvas()


if __name__ == '__main__':
    main()