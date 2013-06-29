__author__ = 'jurek'
import pygame
from pygame.locals import *

#bc - background_color, variable (r,g,b) which tells about color used
#  as background in set of frame in amination
#dx - variable which tells about range between frames in 'x' axis
class Animation(pygame.sprite.Sprite):
    def __init__(self):
        super(pygame.sprite.Sprite,self).__init__()
        self.image = pygame.image.load('napalm.png')
        self.frames = []
        self.image.set_colorkey(pygame.Color(255,0,255))
    def createFrames(self):
        for i in range(10):
            r = pygame.Rect(0+i*34,0,34,34)
            self.frames.append(self.image.subsurface(r))
