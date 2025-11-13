import pygame
import random

pygame.init()
pygame.display.set_caption("Pygame Snek")
Game_Screen = pygame.display.set_mode((600, 500))
Clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)
pygame.mixer.init()

try:
    Bite = pygame.mixer.Sound("Bite.wav")
    Bite.set_volume(0.6)
    Music = pygame.mixer.load("Music.mp3")
    Music.set_volume(0.4)
    
except:
    Bite = None
    Music = None
    print("File didn't load")

Title = pygame.image.load("Snake.png")
Title = pygame.transform.scale(Title, (600, 500))

Game_Screen.blit(Title, (0, 0))
pygame.display.flip()
pygame.time.wait(1000)

Ticker = 0
Alive = True
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

def Food(SnakeList):
    while True:
        Fx = random.randint(0, 29)
        Fy = random.randint(0, 21)
        if [Fx, Fy] not in SnakeList:
            return [Fx, Fy]

Eat_This = Food(Snek)
Score = 0


Playing = True
while Playing:
    Clock.tick(60)
    Ticker += 1
    if Music != None:
        Music.play(-1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False
        elif event.type == pygame.KEYDOWN:
            if Snek_X == 0:
                if event.key == pygame.K_RIGHT:
                    Snek_X = 1
                    Snek_Y = 0
                if event.key == pygame.K_LEFT:
                    Snek_X = -1
                    Snek_Y = 0
            if Snek_Y == 0:
                if event.key == pygame.K_UP:
                    Snek_X = 0
                    Snek_Y = -1
                if event.key == pygame.K_DOWN:
                    Snek_X = 0
                    Snek_Y = 1

    if Alive:
        if Ticker % 20 == 0:
            New_Head = [Snek[0][0] + Snek_X, Snek[0][1] + Snek_Y]
            if (New_Head[0] < 0 or New_Head[0] > 29) or (New_Head[1] < 0 or New_Head[1] > 31):
                Alive = False
            elif New_Head in Snek:
                Alive = False                
            else:
                Snek.insert(0, New_Head)
                if New_Head[0] == Eat_This[0] and New_Head[1] == Eat_This[1]:
                    Eat_This = Food(Snek)
                    Score += 1
                    if Bite != None:
                        Bite.play()
                else:
                    Snek.pop()

    if Alive == False:
        text = font.render("Bonk   gg", True, (250, 250, 250,))
        Game_Screen.blit(text, (250, 250))
        pygame.display.flip()
        pygame.time.wait(1000)
        break

    Game_Screen.fill((0, 0, 0))
    Draw_Grid()
    for i in range(len(Snek)):
        Snake_Head(Snek[i][0], Snek[i][1])
    pygame.draw.rect(Game_Screen, (200, 50, 50), (Eat_This[0]*20, Eat_This[1]*20, 20, 20))
    text2 = font.render("Score: " + str(Score), True, (250, 250, 250))
    Game_Screen.blit(text2, (8,8))
    pygame.display.flip()
pygame.quit()
