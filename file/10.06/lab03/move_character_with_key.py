from pico2d import *

def handle_events():
    global running
    global x
    global y
    global addmove
    events = get_events()
    for event in events:
       if event.type == SDL_QUIT: #10
           running = False
       if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            addmove = True
       elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            addmove = False

       #if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
       #     minmove = True
       #elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
       #     minmove = False

       elif event.key == SDLK_ESCAPE:
               running = False

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')
#20
running = True
addmove = False
minmove = False

x = 10
xmove = 0
frame = 0
while (running):
    clear_canvas()
    grass.draw(400, 30) #30
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

    if addmove == True:
        x += xmove
    elif addmove == False:
        #x -= xmove
    #if minmove == True:
    #    xmove == 10
    #elif minmove == False:
    #    xmove == 0
    handle_events()

close_canvas()

