import pygame
import os

pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Segoe UI Variable",24)
txtt = font.render("New Project", False, (20,20,20))

sc = pygame.display.set_mode((1024,512))
pygame.display.set_caption("Five Engine V1.0")

image = pygame.image.load("menu.png")

run = True
        
def drawbtn(s,x,y,c,w,h):
    he = h - 2
    r = pygame.Rect(x,y, w,h)
    r2 = pygame.Rect(x,y, w,he)
    pygame.draw.rect(s, c, r2, 0)
    pygame.draw.rect(s, c, r, 3)
    


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit
        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                if pygame.mouse.get_pos() >= (812,256):
                                    os.startfile("np.py")
            except:
                os.startfile("error0001.py")
                pygame.quit()
                                

        

    sc.fill((50,50,50))
    sc.blit(image, (0,0))
    drawbtn(sc, 812,256,(255,108,0),128,32)
    sc.blit(txtt,(812,256))
    pygame.display.update()

while not run:
    pygame.quit()




