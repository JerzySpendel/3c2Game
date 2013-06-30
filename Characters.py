__author__ = 'jurek'
import pygame
from pygame.locals import *
from Animation import AnimationNapalm
ANIM_RATE = 170
MOVE_RATE = 0.2
"""
Class representing Hero object of player with
animations of move
"""
class Hero(pygame.sprite.Sprite):
    def __init__(self,manager):
        pygame.sprite.Sprite.__init__(self)
        self.im = pygame.image.load('sprites.png')
        self._anims()
        self.manager = manager
        self.image = self.down[0]
        self.x = 10
        self.y = 10

        self.dt = 0
    def _anims(self):
        self._setDownAnimation()
        self._setUpAnimation()
        self._setRightAnimation()
        self._setLeftAnimation()
    def _setDownAnimation(self):
        self.down = []
        for i in range(3):
            r = pygame.Rect(3+i*32,0,27,33)
            self.down.append(self.im.subsurface(r))
    def _setUpAnimation(self):
        self.up = []
        for i in range(3):
            r = pygame.Rect(3+i*32,96,27,33)
            self.up.append(self.im.subsurface(r))
    def _setRightAnimation(self):
        self.right = []
        for i in range(3):
            r = pygame.Rect(3+i*32,64,27,33)
            self.right.append(self.im.subsurface(r))
    def _setLeftAnimation(self):
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
    def moving(self, keys, dt):
        def check(which):
            result = []
            for img in which:
                if not img == self.image:
                    result.append(True)
            return result

        self.dt += dt
        if keys[K_w] and keys[K_d]:
            self.y -= MOVE_RATE*dt
            self.x += MOVE_RATE*dt
            self.move(check, self.up)
        elif keys[K_w] and keys[K_a]:
            self.y -= MOVE_RATE*dt
            self.x -= MOVE_RATE*dt
            self.move(check, self.up)
        elif keys[K_s] and keys[K_d]:
            self.y += MOVE_RATE*dt
            self.x += MOVE_RATE*dt
            self.move(check,self.down)
        elif keys[K_s] and keys[K_a]:
            self.y += MOVE_RATE*dt
            self.x -= MOVE_RATE*dt
            self.move(check, self.down)
        elif keys[K_w]:
            self.y -= MOVE_RATE*dt
            self.move(check, self.up)
        elif keys[K_d]:
            self.x += MOVE_RATE*dt
            self.move(check, self.right)
        elif keys[K_a]:
            self.x -= MOVE_RATE*dt
            self.move(check, self.left)
        elif keys[K_s]:
            self.y += MOVE_RATE*dt
            self.move(check, self.down)
    def mousing(self,clicked):
        self.manager.animations.append(AnimationNapalm(clicked))


"""
Class for handling events from input and
sending it to sprites under this object
"""

class Manager():
    def __init__(self,sur):
        self.beeings = []
        self.animations = []
        self.surface = sur
        self.test = AnimationNapalm((100,100))
        self.animations.append(self.test)
    def update(self,dt):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if not mouse == (0,)*3:
            mouse = pygame.mouse.get_pos()
            self.mouseUpdate(mouse)
        self.keyboardUpdate(keys,dt)
        self.updateAnimations(dt)
    def updateAnimations(self,dt):
        for anim in self.animations:
            try:
                anim.update(dt)
            except Exception:
                self.animations.remove(anim)

    def add(self, beeing):
        self.beeings.append(beeing)

    def addAnimation(self,anim):
        self.animations.append(anim)

    def keyboardUpdate(self, keys, dt):
        for sprite in self.beeings:
            sprite.moving(keys,dt)

    def mouseUpdate(self, clicked):
        for sprite in self.beeings:
            sprite.mousing(clicked)

    def draw(self, surface):
        for sprite in self.beeings:
            x = sprite.x
            y = sprite.y
            surface.blit(sprite.image, (x, y))
        for animation in self.animations:
            animation.draw(surface)