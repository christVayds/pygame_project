import pygame

# for loading screen

class Loading:

    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, screen):

        pygame.draw.rect(screen, (0,255,0), self.rect)
        pygame.draw.rect(screen, (255,255,255), (self.rect.x, self.rect.y, self.width, self.height))