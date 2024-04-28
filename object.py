import pygame

class Object(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, _type = '', name='', animated=False):
        super().__init__()
        self.width = width
        self.height = height
        self._type = _type
        self.name = name
        self.animated = animated

        # if player is above or bellow the object
        self.front = False

        # enemies in front of abj
        self.e_front = []

        self.rect = pygame.Rect((x, y), (self.width, self.height)) # oject rect
        self.collision = pygame.Rect((x, y), (self.width, self.height)) # object collision rect
        self.image = pygame.Surface((self.width, self.height)) # object surface

        # non animated object/image
        self.nonAnimated = ''
        self.loadNonAnimated() # all all non animated objects

        # for animated object
        self.animateObj = False
        self.animation = 0
        self.animation1 = 0 # only for object that animate once
        self.animatedObjects = [] # load all animated image here
        if self._type in ['animated', 'animated_once']:
            self.loadAnimated() # all animated image loaded
        # for animated once
        self.stop = False

    def draw(self, screen):
        if self._type not in ['hidden', 'hidden2', 'other', 'animated', 'animated_once']:
            screen.blit(self.nonAnimated, self.rect)

        elif self._type == 'other':
            screen.blit(self.nonAnimated, self.rect)

        elif self._type == 'animated':
            self.animate(screen) # auto animating if the object is animated(note animated_once)

        elif self._type == 'animated_once' and self.stop:
            screen.blit(self.animatedObjects[-1], self.rect)

        elif self._type == 'animated_once' and not(self.animateObj):
            screen.blit(self.animatedObjects[0], self.rect)

        # else:
        #     pygame.draw.rect(screen, (255,0,0), self.rect, 1)

        # pygame.draw.rect(screen, (255,255,255), self.rect, 1)

    def move_x(self, direction):
        self.rect.x += direction

    def move_y(self, direction):
        self.rect.y += direction

    def animate(self, screen):
        if(self.animation + 1) >= 63:
            self.animation = 0

        screen.blit(self.animatedObjects[self.animation//9], (self.rect.x, self.rect.y))
        self.animation+=1

    def animateOnce(self, screen):
        if(self.animation1) >= 63:
            self.animation1 = 0
            self.animateObj = False
            self.stop = True
        else:
            if self.animateObj:
                screen.blit(self.animatedObjects[self.animation1//9], (self.rect.x, self.rect.y))
                self.animation1 += 1

    # load animated objects here
    def loadAnimated(self):
        for i in range(7):
            image = f'characters/animatedObj/{self.name}/frame_{i}.png'
            image = pygame.image.load(image)
            image = pygame.transform.scale(image, (self.width, self.height))
            self.animatedObjects.append(image)
    
    # load non animated objects here
    def loadNonAnimated(self):
        if self._type not in ['hidden', 'hidden2', 'other', 'animated', 'animated_once']:
            image = pygame.image.load(f'characters/obj2/{self._type}/{self.name}.png')
            self.nonAnimated = pygame.transform.scale(image, (self.width, self.height))
        elif self._type == 'other':
            image = pygame.image.load(f'characters/objects/{self.name}.png')
            self.nonAnimated = pygame.transform.scale(image, (self.width, self.height))