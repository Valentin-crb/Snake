import pygame
import random
from sys import exit

pygame.init()
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_WIDTH = 680
GAME_HEIGHT = 480
x_head = 400
y_head = 300
score = 0
game_over = False
game_start = False

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
game_screen = pygame.Rect(60,60,GAME_WIDTH, GAME_HEIGHT)
culoare_sarpe = (0,204,0)
culoare_joc = (102, 102, 51)
directie = ""
sarpe = [pygame.Rect(x_head, y_head, 20, 20),
         pygame.Rect(x_head, y_head+20, 20, 20),
         pygame.Rect(x_head, y_head+40, 20, 20),
         pygame.Rect(x_head, y_head+60, 20, 20),
         pygame.Rect(x_head, y_head+80, 20, 20)]
mar = pygame.Rect(200,500,20,20)
culoare_mar =(230,0,0)
font = pygame.font.SysFont(None, 48)
text_game_over = font.render("GAME OVER", True, (255, 0, 0))
text_game_start = font.render("PRESS W TO START", True, culoare_sarpe)
text_score = font.render(f"SCORE: {score}",True, culoare_joc)
rect_over = text_game_over.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
rect_start = text_game_start.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
rect_score = text_score.get_rect(bottomleft=(game_screen.left, game_screen.top - 5))



while True:
    screen.fill((204,204,0))
    
    if not game_start:
        screen.blit(text_game_start, rect_start)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and directie != "jos":
                directie = "sus"
                game_start = True
            if event.key == pygame.K_s and directie != "sus":
                directie = "jos"
            if event.key == pygame.K_a and directie != "dreapta":
                directie = "stanga"
            if event.key == pygame.K_d and directie != "stanga":
                directie = "dreapta"
            if event.key == pygame.K_r and game_over: #restart joc
                game_over = False
                sarpe = [pygame.Rect(x_head, y_head, 20, 20),
                pygame.Rect(x_head, y_head+20, 20, 20),
                pygame.Rect(x_head, y_head+40, 20, 20),
                pygame.Rect(x_head, y_head+60, 20, 20),
                pygame.Rect(x_head, y_head+80, 20, 20)]
                directie = "sus"
                score = 0
                text_score = font.render(f"SCORE: {score}",True, culoare_joc)
    if not game_over and game_start:
        screen.fill((204,204,0))
        pygame.draw.rect(screen, culoare_joc,game_screen) #desenare ecran
        screen.blit(text_score, rect_score)

        pozitii_vechi = [(seg.x, seg.y) for seg in sarpe]

        if directie == "sus":
            sarpe[0].y -=20
        elif directie == "jos":
            sarpe[0].y +=20
        elif directie == "stanga":
            sarpe[0].x -=20
        elif directie == "dreapta":
            sarpe[0].x +=20

        if sarpe[0].colliderect(mar): #redesenare mar + adaugare scor + marire sarpe
            while True:
                mar.x = random.randrange(game_screen.left, game_screen.right, 20)
                mar.y = random.randrange(game_screen.top, game_screen.bottom, 20)
                if not any(mar.colliderect(seg) for seg in sarpe):
                    break
            x,y = pozitii_vechi[-1]
            bloc_nou = pygame.Rect(x,y,20,20)
            sarpe.append(bloc_nou)
            score +=1
            text_score = font.render(f"SCORE: {score}",True, culoare_joc)

        for i in range(1, len(sarpe)):
            sarpe[i].x, sarpe[i].y = pozitii_vechi[i-1]
            
        for i, seg in enumerate(sarpe):
            radius = 5 if i == 0 else 2
            pygame.draw.rect(screen, culoare_sarpe, seg, border_radius=radius)
        pygame.draw.rect(screen,culoare_mar,mar)

        for i in range(2, len(sarpe)):
            if sarpe[0].colliderect(sarpe[i]) or not game_screen.contains(sarpe[0]):
                game_over = True
        
    if game_over:
        screen.blit(text_game_over, rect_over)

    pygame.display.update()
    clock.tick(15)
    
