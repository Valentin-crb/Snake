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

while True:
    
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
    
    
    if directie == "sus":
        head.y -=20
    if directie == "jos":
        head.y +=20
    if directie == "stanga":
        head.x -=20
    if directie == "dreapta":
        head.x +=20
    screen.fill((204,204,0))

    pygame.draw.rect(screen, culoare_sarpe, head, border_radius= 5)
    pygame.display.update()
    clock.tick(5)
    
