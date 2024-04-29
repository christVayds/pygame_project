import pygame

class UI:

    def __init__(self, x, y, width, height, name=''):
        self.width = width
        self.height = height
        self.name = name

        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, screen):
        
        pygame.draw.rect(screen, (255,255,255), self.rect, 2)