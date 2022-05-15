import pygame
import time
import sys

pygame.init()

screen_size = (760,650)
screen = pygame.display.set_mode(screen_size)

time_left = 10  # in seconds
running = True

#game over screen
def game_over():
    font1 = pygame.font.SysFont("Somic Sans MS",100)
    text = font1.render("Time Over!!",True,color)
    screen.blit(text, (200, 200))
    pygame.display.flip()



font = pygame.font.SysFont("Somic Sans MS",30)
color = (255,255,255)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    total_mins = time_left // 60
    total_sec = time_left - (60 *(total_mins))
    time_left -= 1
    if time_left > -1:
        text = font.render(("Time left: "+str(total_mins)+":"+str(total_sec)),True,color)
        screen.blit(text,(600,608))
        pygame.display.flip()
        screen.fill((20,20,20))
        time.sleep(1)   # making the time interval of the loop 1 sec
    else:
        # text = font.render("Time Over!!",True,color)
        # screen.blit(text, (600, 608))
        # pygame.display.flip()
        game_over()
        screen.fill((20, 20, 20))

pygame.quit()
sys.exit()
