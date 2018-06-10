import pygame, sys
from pygame.locals import *
import time

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE=(255,255,255)
    blue=(0,0,255)

    DISPLAY.fill(WHITE)

    x  = 200
    y = 150
    size = 30
    pygame.draw.rect(DISPLAY,blue,(x,y,size,size))

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(DISPLAY, WHITE, (x, y, size, size))
        x = x + 5
        if (x > 500):
            x = 0
        pygame.draw.rect(DISPLAY, blue, (x, y, size, size))
        pygame.display.update()
        time.sleep(0.01)

main()
