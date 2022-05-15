import pygame
import random
import math

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((760,650))

x=300
y=550
x_change=0
y_change=0

#adding player
player = pygame.image.load("upward-arrow.png")


#setting images for enemey
enemey = pygame.image.load("downward-arrow.png")
bh = pygame.image.load("black-hole.png")
list1 = [15, 185, 355, 525, 685]
enemey_x = random.choice(list1)
enemey_y=0
enemey_speed = 10

# for score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
text_x = 5
text_y = 608

# score function
def show_score(x,y):
    score = font.render("Score : " + str(score_value),True,(0,255,0))
    screen.blit(score,(x,y))


#loading player on screen
def playerimg():
    screen.blit(player,(x,y))

def bhimg():
    screen.blit(bh,(10,0))
    screen.blit(bh,(180,0))
    screen.blit(bh,(350,0))
    screen.blit(bh,(520,0))
    screen.blit(bh,(690,0))
    # screen.blit(bh,(10,0))


def enemeyimg_fire(x,y):
    screen.blit(enemey,(x,y))


def distanceB(x,y,x1,y1):
    distance = math.sqrt((pow(x - enemey_x, 2)) + (pow(y - enemey_y, 2)))
    if distance <27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change += 10
            elif event.key == pygame.K_RIGHT:
                x_change -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    x = x - x_change
    if x<=0:
        x=0
    if x>=696:
        x=696

    enemeyimg_fire(enemey_x,enemey_y)
    enemey_y += enemey_speed
    # if enemey_y > 650:
    #     enemey_y = 0
    #     enemey_x = random.choice(list1)
    distance = distanceB(x,y,enemey_x,enemey_y)
    if distance:
        enemey_y = 0
        enemey_x = random.choice(list1)
        score_value += 1
    if enemey_y > 650:
        enemey_y = 0
        enemey_x = random.choice(list1)
    playerimg()
    bhimg()
    show_score(text_x, text_y)
    clock.tick(30)
    pygame.display.update()