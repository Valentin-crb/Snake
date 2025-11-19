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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((204,204,0))
    #umplu ecranul cu patratele
    for x in range(0,SCREEN_WIDTH,20):
        for y in range(0,SCREEN_HEIGHT,20):
            pygame.draw.rect(screen,(204,204,0), (x,y, 20,20))

    
    pygame.draw.rect(screen, culoare_sarpe, head, border_radius= 5)
    for contor in range(20,100):
        pygame.draw.rect(screen,culoare_sarpe, (x_head, y_head+contor, 20, 20), border_radius=5)
    pygame.display.update()
    clock.tick(60)
    
