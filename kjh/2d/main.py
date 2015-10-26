import random
import json
import os

from pico2d import *

background = None
ground = None
object = None

running, RIGHT_STOP, LEFT_STOP, LEFT_RUN, RIGHT_RUN = False, False, False, False, False
L_JUMP, R_JUMP = False, False

def handle_events():
    global running, RIGHT_STOP, LEFT_STOP, LEFT_RUN, RIGHT_RUN, R_JUMP
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:#왼쪽 정지
            LEFT_STOP, RIGHT_STOP, LEFT_RUN, RIGHT_RUN, R_JUMP, L_JUMP = True, False, False, False, False, False
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:#오른쪽 정지
            LEFT_STOP, RIGHT_STOP, LEFT_RUN, RIGHT_RUN, R_JUMP, L_JUMP = False, True, False, False, False, False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:#왼쪽 이동
            LEFT_STOP, RIGHT_STOP, LEFT_RUN, RIGHT_RUN, R_JUMP, L_JUMP = False, False, True, False, False, False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:#오른쪽 이동
            LEFT_STOP, RIGHT_STOP, LEFT_RUN, RIGHT_RUN, R_JUMP, L_JUMP = False, False, False, True, False, False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:#R점프 업
            LEFT_STOP, RIGHT_STOP, LEFT_RUN, RIGHT_RUN, R_JUMP, L_JUMP = False, False, False, False, True, False
        elif event.type == SDL_KEYUP and event.key == SDLK_UP:#L점프 다운
            LEFT_STOP, RIGHT_STOP, LEFT_RUN, RIGHT_RUN, R_JUMP, L_JUMP = False, False, False, False, False, True
            pass

class Logo():
    def __init__(self):
        self.image = load_image('mario.png')
        self.x = 640
        self.y = 360
    def draw(self):
        self.image.draw(self.x, self.y)
    pass

class Ground():
    def __init__(self):
        self.x ,self.y = 1920, 25
        self.image = load_image('down.png')
    def draw(self):
        self.image.draw(self.x, self.y)
    pass

class BackGround():
    def __init__(self):
        self.x = 1920
        self.y = 360
        self.image = load_image('back.png')
    def draw(self):
        self.image.draw(self.x, self.y)
        pass

class Object():
    def __init__(self):
        self.frame = 1
        self.x, self.y = 1100, 70
        self.image = load_image('object.png')
        self.rect = SDL_Rect(int(0),int(0),int(640),int(480))
    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y)
        #self.image.draw(self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 4
        pass

class Player:
    #global ground

    image = None
    global LEFT_STOP, RIGHT_STOP, LEFT_RUN, RIGHT_RUN, R_JUMP, L_JUMP

    def __init__(self):
        self.jump_l = 0
        self.jump_r = 0
        self.left, self.right = 0, 0
        self.x, self.y = 600, 70
        self.frame = 6
        self.xdir = 0
        self.ydir = 0
        self.state = 0
        self.xstate = 1
        if Player.image == None:
            Player.image = load_image('player.png')
        pass

    def update(self):
        if self.x >= 960:
            ground.x -= 10
            background.x -= 10
            object.x -= 10
            self.x = 950
        elif self.x <= 320:
            ground.x += 10
            background.x += 10
            object.x += 10
            self.x = 330
            pass

        if RIGHT_STOP == True:
            self.frame = 6
            self.xdir = 0
            #self.x += (self.xdir * 0)
            self.xstate = 1

        elif LEFT_STOP == True:
            self.frame = 5
            self.xdir = 0
            self.xstate = -1
            #self.x += (self.xdir * 0)

        if LEFT_RUN == True:
            self.frame = 3 + (self.frame + 1) % 3
            self.xdir = -1
            #self.x += (self.xdir * 10)
            self.xstate = -1
        elif RIGHT_RUN == True:
            self.frame = 7 + (self.frame + 1) % 3
            self.xdir = 1
            self.xstate = 1

        if (self.x <= object.x + 50) and (self.x >= object.x - 50) and (self.y <= object.y + 50 )and (self.y <= object.y + 50):
            self.xdir = 0
            #self.x += (self.xdir * 10)
            # if self.xstate == -1:
            #     self.frame = 5
            # elif self.xstate == 1:
            #     self.frame = 6

            if LEFT_RUN == True and self.x < object.x +50:
                self.frame = 3 + (self.frame + 1) % 3
                self.xdir = -1
                #self.x += (self.xdir * 10)
                self.xstate = -1
            if RIGHT_RUN == True and self.x > object.x -50:
                self.frame = 7 + (self.frame + 1) % 3
                self.xdir = +1
                #self.x += (self.xdir * 10)
                self.xstate = +1
            if self.y <= object.y + 50 and (self.x <= object.x + 35) and (self.x >= object.x - 35):
                self.y = 130
                if self.y == 130 and self.xstate == -1:
                    self.frame = 0
                elif self.y == 130 and self.xstate == 1:
                    self.frame = 11

        if (R_JUMP == True):
            self.jump_r = 1

        if(self.jump_r == 1):
            #self.frame = 0
            self.ydir = 10
            self.y += (self.ydir)
            if self.xstate == 1:
                self.frame = 11
            elif self.xstate == -1:
                self.frame = 0

            if(self.y >= 300):
                self.jump_r = 2
                if(self.jump_r == 2):
                    self.ydir = -10
                    self.y += (self.ydir)
                    if(self.y <= 80):
                        self.jump_r = 0

        elif self.y >= 80:
            self.frame = 0
            self.ydir = 10
            self.y -= (self.ydir * 1)
            if self.xstate == 1:
                self.frame = 11
            elif self.xstate == -1:
                self.frame = 0

        self.x += (self.xdir * 10)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 50, self.x, self.y)
    pass

def main():
    open_canvas(1280, 720)
    global running
    global background
    global ground
    global object
    player = Player()
    object = Object()
    background = BackGround()
    ground = Ground()
    running = True
    while running:
        handle_events()
        player.update()
        object.update()
        clear_canvas()
        background.draw()
        ground.draw()
        player.draw()
        object.draw()
        update_canvas()
        delay(0.05)
    close_canvas()
    pass

if __name__ == '__main__':
    main()