import pygame
from sys import exit

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

x_head = 400
y_head = 300
head = pygame.Rect(x_head, y_head, 20, 20)
culoare_sarpe = (0,204,0)
directie = ""
sarpe = [pygame.Rect(x_head, y_head, 20, 20),
         pygame.Rect(x_head, y_head+20, 20, 20),
         pygame.Rect(x_head, y_head+40, 20, 20),
         pygame.Rect(x_head, y_head+60, 20, 20),
         pygame.Rect(x_head, y_head+80, 20, 20)]
copie =[0,0,0,0,0]

while True:
    screen.fill((204,204,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and directie != "jos":
                directie = "sus"
            if event.key == pygame.K_s and directie != "sus":
                directie = "jos"
            if event.key == pygame.K_a and directie != "dreapta":
                directie = "stanga"
            if event.key == pygame.K_d and directie != "stanga":
                directie = "dreapta"
    lungime_sarpe = len(sarpe)
    pozitii_vechi = [(seg.x, seg.y) for seg in sarpe]

    if directie == "sus":
        sarpe[0].y -=20
    elif directie == "jos":
        sarpe[0].y +=20
    elif directie == "stanga":
        sarpe[0].x -=20
    elif directie == "dreapta":
        sarpe[0].x +=20
    
    for i in range(1, len(sarpe)):
        sarpe[i].x, sarpe[i].y = pozitii_vechi[i-1]
        
    for i, seg in enumerate(sarpe):
        radius = 5 if i == 0 else 2
        pygame.draw.rect(screen, culoare_sarpe, seg, border_radius=radius)

    
    pygame.display.update()
    clock.tick(15)
    
