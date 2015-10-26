from pico2d import *

class Player:
    image = None
    global LEFT_STOP, RIGHT_STOP, LEFT_RUN, RIGHT_RUN, LEFT_JUMP, LEFT_MOVE

    def __init__(self):
        self.Gravity = -5
        self.x, self.y = 600, 70
        self.frame = 6
        self.xdir = 0
        self.ydir = 0
        self.state = 0
        if Player.image == None:
            Player.image = load_image('player.png')
        pass

    def update(self):
        if RIGHT_STOP == True:
            self.frame = 6
            self.xdir = 0
            self.x += (self.xdir * 0)
        elif LEFT_STOP == True:
            self.frame = 5
            self.xdir = 0
            self.x += (self.xdir * 0)
        elif RIGHT_RUN == True:
            self.frame = 7 + (self.frame + 1) % 3
            self.xdir = 1
            self.x += (self.xdir * 10)
        elif LEFT_RUN == True:
            self.frame = 3 + (self.frame + 1) % 3
            self.xdir = -1
            self.x += (self.xdir * 10)
        elif LEFT_JUMP == True:
            self.state = 1

        elif(self.state == 0):
            self.frame = 5

        elif LEFT_MOVE == True:
            self.frame = 0
            self.ydir = 20
            if(self.y >= 300 ):
                self.state =2
                if(self.state == 2):
                    self.ydir = -20
                    if(self.y <= 100):
                        self.state = 0

            self.y += (self.ydir * 1)

        elif self.y >= 70:
            self.frame = 0
            self.ydir = 20
            self.y -= (self.ydir * 1)
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 50, self.x, self.y)
