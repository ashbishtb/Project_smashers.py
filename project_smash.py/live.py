import pygame
import random

# Constants
FPS = 30
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)
HEIGHT = 400
WIDTH = 400

class Shape:
    def __init__(self, x=0, y=0, dx=0, dy=0, color=RED):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

    def random_shift_smooth(self, frame):
        if frame == 0:
            new_x = random.randint(0, WIDTH)
            new_y = random.randint(0, HEIGHT)
            self.dx = round((new_x - self.x)/FPS)
            self.dy = round((new_y - self.y)/FPS)
        else:
            self.x += self.dx
            self.y += self.dy

class Dot(Shape):
    def __init__(self, x=0, y=0, dx=0, dy=0, r=5, color=RED):
        super().__init__(x=x, y=y, dx=dx, dy=dy, color=color)
        self.r = r

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)

class Square(Shape):
    def __init__(self, x=0, y=0, dx=0, dy=0, w=5, color=RED):
        super().__init__(x=x, y=y, dx=dx, dy=dy, color=color)
        self.w = w

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.w, self.w))


# pygame initialization
pygame.init()
gameDisplay = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("random shift smooth")
clock = pygame.time.Clock()

# create two different objects
objects = []
dot = Dot(r=20, color=RED)
objects.append(dot)
dot = Dot(r=40, color=BLUE)
objects.append(dot)
square = Square(w=30, color=GREEN)
objects.append(square)


# game loop
frame = 0
done = False
while not done:
    # timing
    clock.tick(FPS)
    frame -= 1
    if frame < 0:
        frame = FPS

    # update surface
    gameDisplay.fill(WHITE)
    for obj in objects:
        obj.draw(gameDisplay)
        obj.random_shift_smooth(frame)
    pygame.display.flip()

    # user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

# cleanup and quit
pygame.quit()