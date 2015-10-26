from filecmp import clear_cache
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while(x < 800):
    update_canvas()
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
    x += 2
    delay(0.01)
    get_events()

# 여기를 채우세요.

close_canvas()

