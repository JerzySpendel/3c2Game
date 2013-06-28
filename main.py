__author__ = 'jurek'
import pygame,copy,random
from pygame.locals import *
from Characters import Hero
size = 800,600
class Game(object):
    def __init__(self):

        pygame.init()
        flag = DOUBLEBUF
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(size,flag)
        self.gamestate = 1

        self.hero = Hero()
        self.loop()
    def game_exit(self):
        exit()
    def loop(self):
        while self.gamestate == 1:
            dt = self.clock.tick()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.gamestate = 0
            keys = pygame.key.get_pressed()
            self.hero.moving(keys,dt)
            self.surface.fill((20,0,0))
            self.surface.blit(self.hero.image,(self.hero.x,self.hero.y))
            pygame.display.flip()
        self.game_exit()
if __name__ == '__main__':
    Game()
