__author__ = 'jurek'
import pygame
#bc - background_color, variable (r,g,b) which tells about color used
#  as background in set of frame in amination
#dx - variable which tells about range between frames in 'x' axis


class AnimationNapalm(pygame.sprite.Sprite):
    def __init__(self, where):
        super(pygame.sprite.Sprite,self).__init__()
        self.im = pygame.image.load('napalm.png')
        self.im.set_colorkey(pygame.Color(255, 0, 255))
        self.frames = []
        self.createFrames()
        self.image = self.frames[0]
        self.spf = 100
        self.dt = 100
        self.x, self.y = where

    def setName(self,name):
        self.name = name

    def update(self, dt):
        self.dt += dt
        if self.dt >= self.spf:
            self.image = self.frames[self.nextFrame()]
            self.dt = 0

    def createFrames(self):
        for i in range(10):
            r = pygame.Rect(0+i*34, 0,34, 34)
            self.frames.append(self.im.subsurface(r))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def nextFrame(self):
        i = 0
        for frame in self.frames:
            if frame == self.image:
                return i+1
            i += 1


