import pygame
import random

class bgEnemey():
    def __init__(self,black_holes,enemeyha):
        self.bh = pygame.image.load(black_holes)
        self.ene = pygame.image.load(enemeyha)

    def drawB(self,screen):
        screen.blit(self.bh,(10,0))
        screen.blit(self.bh,(180,0))
        screen.blit(self.bh,(350,0))
        screen.blit(self.bh,(520,0))
        screen.blit(self.bh,(690,0))

    def drawE(self,screen):
        screen.blit(self.ene,(enemey_x,enemey_y))

    def update(self,enemey_speed):



class player():
    def __init__(self,pla):
        self.img = pygame.image.load(pla)
        self.imgX = 760 / 2
        self.imgY = 530
        self.img_rect = self.img.get_rect(center = (self.imgX,self.imgY))


    def draw(self,screen):
        screen.blit(self.img,(self.imgX,self.imgY))

    def update(self,screen):
        self.imgX = self.imgX - x_change
        if self.imgX <= 0:
            self.imgX = 0
        if self.imgX >= 696:
            self.imgX = 696
        self.draw(screen)


# class gameState():

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((760,650))

x=300
y=550
x_change=0
y_change=0

#setting value for enemy
list1 = [15, 185, 355, 525, 685]
enemey_x = random.choice(list1)
enemey_y=0
enemey_speed = 10


enem1 = bgEnemey("black-hole.png" , "downward-arrow.png")
pl= player("upward-arrow.png")

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

    # pl.draw(screen)
    pl.update(screen)
    enem1.update(enemey_speed)
    enem1.drawB(screen)
    enem1.drawE(screen)
    clock.tick(30)
    pygame.display.update()