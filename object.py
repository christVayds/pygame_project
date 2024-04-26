import pygame

class Object(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, _type = '', name=''):
        super().__init__()
        self.width = width
        self.height = height
        self._type = _type
        self.name = name

        # if player is above or bellow the object
        self.front = False

        # enemies in front of abj
        self.e_front = []

        self.rect = pygame.Rect((x, y), (self.width, self.height)) # oject rect
        self.collision = pygame.Rect((x, y), (self.width, self.height)) # object collision rect
        self.image = pygame.Surface((self.width, self.height)) # object surface

    def draw(self, screen):
        if self._type not in ['hidden', 'hidden2', 'other']:
            image = pygame.image.load(f'characters/obj2/{self._type}/{self.name}.png')
            image = pygame.transform.scale(image, (self.width, self.height))

            screen.blit(image, self.rect)
        elif self._type == 'other':
            image = pygame.image.load(f'characters/objects/{self.name}.png')
            image = pygame.transform.scale(image, (self.width, self.height))

            screen.blit(image, self.rect)
        # else:
        #     pygame.draw.rect(screen, (255,0,0), self.rect, 1)

    def move_x(self, direction):
        self.rect.x += direction

    def move_y(self, direction):
        self.rect.y += direction

# soon
class animatedObjects(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, _type='', name=''):
        super().__init__()
        self.width = width
        self.height = height
        self._type = _type
        self.name = name

        self.rect = pygame.Rect((x, y), (self.width, self.height))
        self.image = pygame.Surface((self.width, self.height))

        # player facing
        self.font = False