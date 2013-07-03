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
        self.name = "Me"
        self.dt = 0

        self.sb = StatusBar(self.manager.surface)

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
        self.update(dt)
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
        self.sb.setMana(self.sb.mp-10)

    def update(self,dt):
        self.sb.update(dt)

    def _drawName(self,surface):
        font = pygame.font.Font('vademecu.ttf',10)
        img = font.render('Me', 1, (0, 255, 0))
        surface.blit(img, (self.x+7, self.y - 15))

    def draw(self,surface):
        surface.blit(self.image, (self.x, self.y))
        self._drawName(surface)
        self.sb.draw(surface)

"""
Class for handling events from input and
sending it to sprites under this object
"""

class Manager():
    def __init__(self, sur):
        self.beeings = []
        self.animations = []
        self.surface = sur

    def update(self, dt):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if not mouse == (0,)*3:
            mouse = pygame.mouse.get_pos()
            self.mouseUpdate(mouse)
        self.keyboardUpdate(keys,dt)
        self.updateAnimations(dt)

    def updateAnimations(self, dt):
        for anim in self.animations:
            try:
                anim.update(dt)
            except Exception:
                self.animations.remove(anim)

    def add(self, beeing):
        self.beeings.append(beeing)

    def addAnimation(self, anim):
        self.animations.append(anim)

    def keyboardUpdate(self, keys, dt):
        for sprite in self.beeings:
            sprite.moving(keys, dt)

    def mouseUpdate(self, clicked):
        for sprite in self.beeings:
            sprite.mousing(clicked)

    def draw(self, surface):
        for sprite in self.beeings:
            sprite.draw(surface)
        for animation in self.animations:
            animation.draw(surface)


class StatusBar(pygame.sprite.Sprite):
    def __init__(self, surface):
        super(pygame.sprite.Sprite, self).__init__()
        self.max_hp = 100
        self.hp = 100
        self.max_mp = 100
        self.mp = 100
        self.font = pygame.font.Font('vademecu.ttf', 10)

        self.w, self.h = surface.get_size()
        #Variables which are determining general look of status bar
        self.status_length = 150
        self.status_height = 13

        self.left_margin = 10
        #Distance of mana status bar from bottom of window

        self.mana_top = 20

        #Distance of health status bar from bottom of window
        self.health_top = 40

        #Coordinates of points to draw border lines of mana and health status bar
        self.health_coords = [(self.left_margin, self.h-self.health_top), (self.left_margin+self.status_length, self.h-self.health_top), (self.left_margin+self.status_length, self.h-self.health_top+self.status_height), (self.left_margin, self.h-self.health_top+self.status_height)]
        self.mana_coords = [(self.left_margin, self.h-self.mana_top), (self.left_margin+self.status_length, self.h-self.mana_top), (self.left_margin+self.status_length, self.h-self.mana_top+self.status_height), (self.left_margin, self.h-self.mana_top+self.status_height)]

        self.health_rectangle = pygame.Rect(self.left_margin, self.h-self.health_top, 150, 13)
        self.mana_rectangle = pygame.Rect(self.left_margin, self.h-self.mana_top, 150, 13)

    def update(self,dt):
        self.mp += dt/100

    def setHealth(self,val):
        if val>=0:
            self.hp = val

    def setMana(self,val):
        if val >= 0:
            self.mp = val

    def _percent(self,HM):
        if HM == 1:
            return self.hp/self.max_hp
        else:
            return self.mp/self.max_mp

    def _healthLength(self):
        return self.status_length*self._percent(1)

    def _manaLength(self):
        return self.status_length*self._percent(0)

    def _drawBorder(self,surface):
        self.health_rectangle.width = self._healthLength()
        pygame.draw.lines(surface, pygame.Color(255, 0, 0), 1, self.health_coords, 1)
        self.mana_rectangle.width = self._manaLength()
        pygame.draw.lines(surface, pygame.Color(0, 0, 255), 1, self.mana_coords, 1)

    def _drawFilledBorder(self,surface):
        pygame.draw.rect(surface, pygame.Color(255, 0, 0), self.health_rectangle)
        pygame.draw.rect(surface, pygame.Color(0, 0, 255), self.mana_rectangle)

    def draw(self,surface):
        self._drawBorder(surface)
        self._drawFilledBorder(surface)
