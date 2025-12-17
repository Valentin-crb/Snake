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
font = pygame.font.SysFont(None, 48)   
culoare_sarpe = (0,204,0)
culoare_joc = (102, 102, 51)
culoare_mar =(230,0,0)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
game_screen = pygame.Rect(60,60,GAME_WIDTH, GAME_HEIGHT)


class GameState:
    def __init__(self):
        self.directie = ""
        self.game_start = False
        self.game_over = False
        self.score = 0

        self.sarpe = [pygame.Rect(x_head, y_head, 20, 20),
         pygame.Rect(x_head, y_head+20, 20, 20),
         pygame.Rect(x_head, y_head+40, 20, 20),
         pygame.Rect(x_head, y_head+60, 20, 20),
         pygame.Rect(x_head, y_head+80, 20, 20)]
        
        self.mar = pygame.Rect(200,400,20,20)
        self.text_score = font.render(f"SCORE: {score}",True, culoare_joc)


state = GameState()

text_controls = font.render("WASD - move | R - restart", True, culoare_joc)
text_game_over = font.render("GAME OVER", True, (200, 0, 0))
text_restart = font.render("PRESS R TO RESTART",True, (200,0,0))
text_game_start = font.render("PRESS W TO START", True, culoare_joc)
rect_over = text_game_over.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
rect_start = text_game_start.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
rect_score = state.text_score.get_rect(bottomleft=(game_screen.left, game_screen.top - 5))
rect_controls = text_controls.get_rect(midbottom=(rect_start.centerx, rect_start.top-10))
rect_restart = text_restart.get_rect(midtop=(rect_start.centerx, rect_start.bottom+10))

def procesare_input(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and state.directie != "jos":
                state.directie = "sus"
                state.game_start = True
            elif event.key == pygame.K_s and state.directie != "sus":
                state.directie = "jos"
            elif event.key == pygame.K_a and state.directie != "dreapta":
                state.directie = "stanga"
            elif event.key == pygame.K_d and state.directie != "stanga":
                state.directie = "dreapta"
            elif event.key == pygame.K_r and state.game_over: #restart joc
                reset_game(state)
                
def reset_game(state):
    state.game_over = False
    state.directie = "sus"
    state.score = 0

    state.sarpe = [pygame.Rect(x_head, y_head, 20, 20),
    pygame.Rect(x_head, y_head+20, 20, 20),
    pygame.Rect(x_head, y_head+40, 20, 20),
    pygame.Rect(x_head, y_head+60, 20, 20),
    pygame.Rect(x_head, y_head+80, 20, 20)]
    
    state.text_score = font.render(f"SCORE: {state.score}",True, culoare_joc)
    state.mar = pygame.Rect(200,400,20,20)
    pygame.draw.rect(screen,culoare_mar,state.mar)

def game(state):
    if not state.game_over and state.game_start:
        screen.fill((204,204,0))
        pygame.draw.rect(screen, culoare_joc,game_screen) #desenare ecran
        screen.blit(state.text_score, rect_score)

        pozitii_vechi = [(seg.x, seg.y) for seg in state.sarpe]

        if state.directie == "sus":
            state.sarpe[0].y -=20
        elif state.directie == "jos":
            state.sarpe[0].y +=20
        elif state.directie == "stanga":
            state.sarpe[0].x -=20
        elif state.directie == "dreapta":
            state.sarpe[0].x +=20

        if state.sarpe[0].colliderect(state.mar): #redesenare mar + adaugare scor + marire sarpe
            while True:
                state.mar.x = random.randrange(game_screen.left, game_screen.right, 20)
                state.mar.y = random.randrange(game_screen.top, game_screen.bottom, 20)
                if not any(state.mar.colliderect(seg) for seg in state.sarpe):
                    break
            x,y = pozitii_vechi[-1]
            bloc_nou = pygame.Rect(x,y,20,20)
            state.sarpe.append(bloc_nou)
            state.score +=1
            state.text_score = font.render(f"SCORE: {state.score}",True, culoare_joc)

        for i in range(1, len(state.sarpe)):
            state.sarpe[i].x, state.sarpe[i].y = pozitii_vechi[i-1]
            
        for i, seg in enumerate(state.sarpe):
            radius = 5 if i == 0 else 2
            pygame.draw.rect(screen, culoare_sarpe, seg, border_radius=radius)
        pygame.draw.rect(screen,culoare_mar,state.mar)

        for i in range(2, len(state.sarpe)):
            if state.sarpe[0].colliderect(state.sarpe[i]) or not game_screen.contains(state.sarpe[0]):
                state.game_over = True


while True:
    screen.fill((204,204,0))
    
    procesare_input(state)

    if not state.game_start:
        screen.blit(text_game_start, rect_start)
        screen.blit(text_controls, rect_controls)
    
    game(state)
        
    if state.game_over:
        screen.blit(text_game_over, rect_over)
        screen.blit(text_restart, rect_restart)

    pygame.display.update()
    clock.tick(15)
    
