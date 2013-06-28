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
            r = pygame.Rect(3+i*32,66,27,33)
            self.right.append(self.im.subsurface(r))
    def setLeftAnimation(self):
        self.left = []
        for i in range(3):
            r = pygame.Rect(3+i*32,33,27,33)
            self.left.append(self.im.subsurface(r))
    def moving(self,keys,dt):
        def check(which):
            result = []
            for img in which:
                if not img == self.image:
                    result.append(True)
            return result
        self.dt += dt
        if keys[K_d]:
            if [True]*3 == check(self.right):
                self.image = self.right[0]
            self.x += 0.2*dt
            if self.dt >= ANIM_RATE:
                if self.image == self.right[0]:
                    self.image = self.right[1]
                elif self.image == self.right[1]:
                    self.image = self.right[2]
                elif self.image == self.right[2]:
                    self.image = self.right[0]
                self.dt = 0
        if keys[K_a]:
            if [True]*3 == check(self.left):
                self.image = self.left[0]
            self.x -= 0.2*dt
            if self.dt >= ANIM_RATE:
                if self.image == self.left[0]:
                    self.image = self.left[1]
                elif self.image == self.left[1]:
                    self.image = self.left[2]
                elif self.image == self.left[2]:
                    self.image = self.left[0]
                self.dt = 0
        if keys[K_w]:
            if [True]*3 == check(self.up):
                self.image = self.up[0]
            self.y -= 0.2*dt
            if self.dt >= ANIM_RATE:
                if self.image == self.up[0]:
                    self.image = self.up[1]
                elif self.image == self.up[1]:
                    self.image = self.up[2]
                elif self.image == self.up[2]:
                    self.image = self.up[0]
                self.dt = 0
        if keys[K_s]:
            if [True]*3 == check(self.down):
                self.image = self.down[0]
            self.y += 0.2*dt
            if self.dt >= ANIM_RATE:
                if self.image == self.down[0]:
                    self.image = self.down[1]
                elif self.image == self.down[1]:
                    self.image = self.down[2]
                elif self.image == self.down[2]:
                    self.image = self.down[0]
                self.dt = 0
