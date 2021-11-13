import pygame

pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Segoe UI Variable",22)
font2 = pygame.font.SysFont("Berlin Sans MF",24)
font3 = pygame.font.SysFont("Canadra",32)
txtt = font.render("E X I T", False, (20,20,20))
er = font2.render("Кирилл , ты долбанутый?", False, (20,20,20))
erc = font3.render("Code #0001", False, (20,20,20))

sc = pygame.display.set_mode((256,128), pygame.RESIZABLE)
pygame.display.set_caption("Error #0001(file or directory not found)")

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
            if pygame.mouse.get_pos() >= (100,86):
                pygame.quit()
                                

        

    sc.fill((50,50,50))
    drawbtn(sc, 100,86,(255,108,0),64,32)
    sc.blit(txtt,(102,86))
    sc.blit(er, (24,16))
    sc.blit(erc, (64,48))
    pygame.display.update()





