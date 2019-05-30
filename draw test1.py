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
    dx, dy = 5, 5
    size = 30
    pygame.draw.rect(DISPLAY,blue,(x,y,size,size))

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(DISPLAY, WHITE, (x, y, size, size))
        nextx = x + dx
        if (nextx>= 500 - size or nextx <= 0):
            dx = -dx
            nextx = x + dx

        nexty = y + dy
        if (nexty >= 400 - size or nexty <= 0):
            dy = -dy
            nexty = y + dy

        x, y = nextx, nexty

        pygame.draw.rect(DISPLAY, blue, (x, y, size, size))
        pygame.display.update()
        time.sleep(0.01)

main()
