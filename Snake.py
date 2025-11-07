import pygame
import random

pygame.init()
pygame.display.set_caption("Pygame Snek")
Game_Screen = pygame.display.set_mode((600, 500))
Clock = pygame.time.Clock()

Snek_X = 1
Snek_Y = 0
Snek = [
    [10, 8],
    [9, 8],
    [8, 8]
]
def Draw_Grid():
    for x in range(0 , 600, 20):
        pygame.draw.line(Game_Screen, (40, 40, 40), (x, 0), (x, 500))
    for y in range(0 , 500, 20):
        pygame.draw.line(Game_Screen, (40, 40, 40), (0, y), (600, y))

def Snake_Head(X, Y):
    pygame.draw.rect(Game_Screen, (20, 180, 20), (X *20, Y * 20, 20, 20))

Playing = True
while Playing:
    Clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False

    Game_Screen.fill((0, 0, 0))
    Draw_Grid()
    for i in range(len(Snek)):
        Snake_Head(Snek[i][0], Snek[i][1])
    
    pygame.display.flip()
pygame.quit()
