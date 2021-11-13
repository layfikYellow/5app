import pygame
import time
import os

pygame.init()

sc = pygame.display.set_mode((512,256), pygame.NOFRAME)

background = pygame.image.load("bckgrnd.png")

run = True

if run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit
            run = False

    sc.blit(background, (0,0))
    pygame.display.update()
    time.sleep(10)
    try:
        os.startfile("engine.py")
    except:
        os.startfile("error0001.py")
        pygame.quit()
    run = False
    pygame.quit()
    quit

 
    
