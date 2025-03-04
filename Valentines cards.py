import pygame

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Valentine's Day Card")
screen = pygame.display.set_mode((800, 800))
font = pygame.font.Font('freesansbold.ttf', 32)
img = pygame.image.load("Flower.jpg")
img = pygame.transform.scale(img, (800,500))
#------------------------------------#
class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self, surface):
        pass
class Heart(Shape):
    def draw(self, surface):
        left_circle_center = (self.x - 20, self.y)
        right_circle_center = (self.x + 20, self.y)
        triangle_points = [(self.x - 40, self.y + 5),
                           (self.x + 40, self.y + 5),
                           (self.x, self.y + 50)]
        pygame.draw.circle(surface, self.color, left_circle_center, 20)
        pygame.draw.circle(surface, self.color, right_circle_center, 20)
        pygame.draw.polygon(surface, self.color, triangle_points)
class Square(Shape):
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, 100, 80),5)
# Create instances of Heart
Heart_list = []
for i in range (8):
    for j in range (4):
        Heart_list.append(Heart(i*100+40, j*80+20, (250,250,250)))
for i in range (9):
    for j in range (5):
        Heart_list.append(Square(i*100-60, j*80-40, (0,0,250)))

# Draw everything
for i in range(len(Heart_list)):
    Heart_list[i].draw(screen)

text1 = font.render('This is a maditory project!', True, (250, 0, 0))
text2 = font.render('So there\'s your Happy Valentines Day project', True, (250, 0, 0))
screen.blit(text1, (310, 50))
screen.blit(text2, (50, 150))
screen.blit(img, (0, 300))

pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
