from pico2d import *
from math import *
open_canvas()
grass = load_image('aaa\grass.png')
character = load_image('run_animation.png')

x = 400
y = 300
x1 = 1
y1 = 1
frame = 0
while(x<800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x * cos(1) * 3.14, y * sin(1) * 3.14)
    update_canvas()
    frame = (frame + 1) % 8
#    x1 = cos(5) * 3.14
#    x1 += cos(1)/3.14
#    y1 += sin(1)
    delay(0.001)
    get_events()

close_canvas()

