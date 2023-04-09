import pygame
import sys
import random
from settings import *
from player import Player
from sky import Sky
from asteroid import Asteroid
def asteroid_spawn(asteroids):
    coordy=[-500,-400,-300,-200,-100]
    coordx=[500,400,300,200,100]
    speedy=[3,4,5,6,7,8]
    speedx=[-3,-2,-1,0,1,2,3]
    random.shuffle(speedy)
    random.shuffle(speedx)
    random.shuffle(coordy)
    random.shuffle(coordx)
    for i in range(5):
        a=Asteroid(screen,coordx[i],coordy[i],speedx[i],speedy[i])
        asteroids.append(a)
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
player=Player("images/Ship.png",screen,(SCREEN_WIDTH)//2,(SCREEN_HEIGHT)//2)
sky=Sky("images/Sky.jpg",screen,0,0)
sky_2=Sky("images/Sky.jpg",screen,0,-1000)
meteors=pygame.sprite.Group()
asteroids=[]
asteroid_spawn(asteroids)
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for a in asteroids:
        a.update()
    sky.update()
    sky_2.update()
    player.update()

    screen.fill(BLACK)
    sky.draw()
    sky_2.draw()
    player.draw()
    for a in asteroids:
        a.draw()
    pygame.display.update()
    clock.tick(FPS)
