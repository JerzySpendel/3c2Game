__author__ = 'jurek'
import pygame
from pygame.locals import *
ANIM_RATE = 170
"""
Class representing Hero object of player with
animations of move
"""
class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.im = pygame.image.load('sprites.png')
        self.anims()
        self.image = self.down[0]
        self.x = 10
        self.y = 10

        self.dt = 0
    def anims(self):
        self.setDownAnimation()
        self.setUpAnimation()
        self.setRightAnimation()
        self.setLeftAnimation()
    def setDownAnimation(self):
        self.down = []
        for i in range(3):
            r = pygame.Rect(3+i*32,0,27,33)
            self.down.append(self.im.subsurface(r))
    def setUpAnimation(self):
        self.up = []
        for i in range(3):
            r = pygame.Rect(3+i*32,96,27,33)
            self.up.append(self.im.subsurface(r))
    def setRightAnimation(self):
        self.right = []
        for i in range(3):
            r = pygame.Rect(3+i*32,64,27,33)
            self.right.append(self.im.subsurface(r))
    def setLeftAnimation(self):
        self.left = []
        for i in range(3):
            r = pygame.Rect(3+i*32,32,27,33)
            self.left.append(self.im.subsurface(r))

    #Generic method for moving
    def move(self,check,which):
        if [True]*3 == check(which):
            self.image = which[0]
        if self.dt >= ANIM_RATE:
            if self.image == which[0]:
                self.image = which[1]
            elif self.image == which[1]:
                self.image = which[2]
            elif self.image == which[2]:
                self.image = which[0]
            self.dt = 0

#Method for moving using general "move" method
    def moving(self,keys,dt):
        def check(which):
            result = []
            for img in which:
                if not img == self.image:
                    result.append(True)
            return result

        self.dt += dt
        if keys[K_d]:
            self.x += 0.2*dt
            self.move(check,self.right)
        if keys[K_a]:
            self.x -= 0.2*dt
            self.move(check,self.left)
        if keys[K_w]:
            self.y -= 0.2*dt
            self.move(check,self.up)
        if keys[K_s]:
            self.y += 0.2*dt
            self.move(check,self.down)