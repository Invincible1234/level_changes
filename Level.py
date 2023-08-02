import pygame

class Level:
    
    def __init__(self):
        self.Objects = pygame.sprite.Group()

    def add_obj(self, object):
        self.Objects.add(object)
    
    def draw(self, screen):
        self.Objects.draw(screen)
        self.Objects.update()