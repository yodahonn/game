import pygame, sys
from pygame.locals import *
import time

def main():
    pygame.init()

    SCREEN_SIZE_X = 500
    SCREEN_SIZE_Y = 400
    DISPLAY=pygame.display.set_mode((SCREEN_SIZE_X,SCREEN_SIZE_Y),0,32)

    WHITE=(255,255,255)
    BLUE=(0,0,255)

    DISPLAY.fill(WHITE)

    x = 200
    y = 150
    dx, dy = 5, 5
    SIZE = 30

    barx = 50
    bary = nextbary = 100
    BAR_SIZE_X = 30
    BAR_SIZE_Y = 90

    pygame.draw.rect(DISPLAY,BLUE,(x,y,SIZE,SIZE))
    pygame.draw.rect(DISPLAY,BLUE,(barx,bary,BAR_SIZE_X,BAR_SIZE_Y))

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    nextbary = bary - 5
                if event.key == pygame.K_DOWN:
                    nextbary = bary + 5


        pygame.draw.rect(DISPLAY,WHITE,(barx,bary,BAR_SIZE_X,BAR_SIZE_Y))

        pygame.draw.rect(DISPLAY, WHITE, (x, y, SIZE, SIZE))
        nextx = x + dx
        nexty = y + dy

        if (nextx >= SCREEN_SIZE_X - SIZE):
            dx = -5
        if (nextx <= 0):
            dx = 5

        if (nexty >= SCREEN_SIZE_Y - SIZE or nexty <= 0):
            dy = -dy

        x = nextx
        y = nexty

        bary = nextbary

        pygame.draw.rect(DISPLAY, BLUE, (x, y, SIZE, SIZE))
        pygame.draw.rect(DISPLAY,BLUE,(barx,bary,BAR_SIZE_X,BAR_SIZE_Y))
        pygame.display.update()
        time.sleep(0.01)

main()