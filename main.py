import os
import random
import pygame
import time
import iofile

#### SYSTEM SETUP ####
#/#/#/#/#/#/#/#/#/#/#/#/#/

SYSTEM_VOLUME = 0.5
GAME_NAME = "Engine Prototype"
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 600

RUNNING = True

if __name__ == '__main__':
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption(GAME_NAME)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),
                                 pygame.HWSURFACE|pygame.DOUBLEBUF|
                                 pygame.RESIZABLE)
clock = pygame.time.Clock()

controls = iofile.File(iofile.settingType.CONTROL, "")
settings = iofile.File(iofile.settingType.SETTING, "")

#\#\#\#\#\#\#\#\#\#\#\#\#\
##########################

def inputHandler():
    user_input = pygame.key.get_pressed()
    
    pressed = [i for i, x in enumerate(user_input) if x == 1]
    ## user_input gives us the entire keyboard
    ## that line of code allows me to find the indexes of all items
    ## in the list that returns 1

    if (len(pressed) > 0):
        for key in pressed:
            action = controls.searchForKey(key)
            if (key == True):
                print(action)
    
while RUNNING:
    clock.tick(60)

    inputHandler()

    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.constants.USEREVENT:
            pygame.mixer.music.set_volume(volume)
            inputHandler
    pygame.display.update()

pygame.quit()
