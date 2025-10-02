import pygame
import random

pygame.init()
pygame.display.set_caption("Pygame Piano")
Game_Screen = pygame.display.set_mode((800,200))
pygame.mixer.init()


Playing = True
Mouse_X_Pos = 0; Mouse_Y_Pos = 0
MousePos = (Mouse_X_Pos, Mouse_Y_Pos)

KeySounds = [
pygame.mixer.Sound("key01.mp3"),
pygame.mixer.Sound("key02.mp3"),
pygame.mixer.Sound("key03.mp3"),
pygame.mixer.Sound("key04.mp3"),
pygame.mixer.Sound("key05.mp3")
]

class PianoKeys:
    def __init__(self, i):
        self.X = i*50
        self.KeyType = (i+1)%2
        self.Key = KeySounds[i]
        if self.KeyType == 0:
            self.Width = 50
        else:
            self.Width = 100
        self.Pressed = False
    def Interact(self):
        if self.X < MousePos[0] < self.X + self.Width:
            self.Pressed = True
    def Draw (self):
        if self.Pressed == True:
            self.Pressed = False
        if self.KeyType == 1:
            if self.Pressed == False:
                pygame.mixer.Sound.play(self.Key)
                pygame.draw.rect(Game_Screen, (255, 255, 255), (self.X, 0, self.Width, 200))
                pygame.draw.rect(Game_Screen, (0, 0, 0), (self.X, 0, self.Width, 200), 2)
            else:
                pygame.draw.rect(Game_Screen, (200, 200, 200), (self.X, 0, self.Width, 200))
                pygame.draw.rect(Game_Screen, (0, 0, 0), (self.X, 0, self.Width, 200), 2)
        else:
            if self.Pressed == False:
                pygame.draw.rect(Game_Screen, (0, 0, 0), (self.X + 25, 0, self.Width, 100))
                pygame.draw.rect(Game_Screen, (255, 255, 255), (self.X + 25, 0, self.Width, 100), 2)
            else:
                pygame.draw.rect(Game_Screen, (100, 100, 100), (self.X + 25, 0, self.Width, 100))
                pygame.draw.rect(Game_Screen, (255, 255, 255), (self.X + 25, 0, self.Width, 100), 2)

OddKeys = []
EvenKeys = []

for i in range(5):
    if i % 2 == 0:
        OddKeys.append(PianoKeys(i))
    else:
        EvenKeys.append(PianoKeys(i))

Keys = OddKeys + EvenKeys

while Playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False
        elif event.type == pygame.MOUSEMOTION:
            Mouse_X_Pos, Mouse_Y_Pos = pygame.mouse.get_pos()
            MousePos = (Mouse_X_Pos, Mouse_Y_Pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(Keys)):
                Keys[i].Interact()

    for i in range(len(Keys)):
        Keys[i].Draw()


    pygame.display.flip()
pygame.quit()
