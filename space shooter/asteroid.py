from settings import *
import pygame
class Asteroid(pygame.sprite.Sprite):
    def __init__(self,screen,x,y,v,h):
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(BAR_FILE_NAME).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
        self.speedy= h
        self.speedx= v
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
    def draw(self):
        self.screen.blit(self.image, self.rect)
