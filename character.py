import pygame
import random

import pygame.locals

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, name=''):
        super().__init__()
        self.width = width
        self.height = height
        self.name = name

        # player life
        self.defaultLife = 100
        self.life = self.defaultLife

        # speed
        self.speed = 7
        self.walk = 0

        # rect and surface
        self.rect = pygame.Rect((x, y), (self.width, self.height)) # for player rect
        self.image = pygame.Surface((self.width, self.height)) # surface

        # facing
        self.left = False
        self.right = True
        self.up = False
        self.down = False

        # image and animation
        self.c_left = []
        self.c_right = []
        self.c_up = []
        self.c_down = []
        # load all images of a characters
        self.loadImages()
        self.flipImage() # flip image

    def draw(self, screen, allObj):

        # handle collision
        self.handleCollision(allObj, screen)

        # get key events
        keys = pygame.key.get_pressed()

        # left
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.left = True
            self.right = False
            self.up = False
            self.down = False

            self.move_x((self.speed * -1))

        # right
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.left = False
            self.right = True
            self.up = False
            self.down = False

            self.move_x(self.speed)

        # up
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.left = False
            self.right = False
            self.up = True
            self.down = False

            self.move_y((self.speed * -1))

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.left = False
            self.right = False
            self.up = False
            self.down = True

            self.move_y(self.speed)
        else: 
            self.walk = 0

        self.Facing(screen)
        
        # player rect
        # pygame.draw.rect(screen, (255,255,10), self.rect, 1)

    
    def Facing(self, screen):
        # self.walk is the number of walk of character
        if (self.walk + 1) >= 21:
            self.walk = 0
            
        if self.left:
            screen.blit(self.c_left[self.walk//3], (self.rect.x, self.rect.y))
            self.walk += 1
        elif self.right:
            screen.blit(self.c_right[self.walk//3], (self.rect.x, self.rect.y))
            self.walk += 1
        elif self.up:
            screen.blit(self.c_up[self.walk//3], (self.rect.x, self.rect.y))
            self.walk += 1
        elif self.down:
            screen.blit(self.c_down[self.walk//3], (self.rect.x, self.rect.y))
            self.walk += 1
        else:
            if self.left:
                screen.blit(self.c_left[0], (self.rect.x, self.rect.y))
            elif self.right:
                screen.blit(self.c_right[0], (self.rect.x, self.rect.y))

    # load all image in list of images [right, left, and down]
    def loadImages(self):
        images = ['D_Walk_', 'S_Walk_', 'U_Walk_']

        for image in images:
            for count in range(7):
                img = f'characters/char1/{image}{count}.png'
                img = pygame.image.load(img)
                img = pygame.transform.scale(img, (self.width, self.height))
                if image == 'D_Walk_':
                    self.c_down.append(img)
                elif image == 'U_Walk_':
                    self.c_up.append(img)
                elif image == 'S_Walk_':
                    self.c_left.append(img)

    # flip all characters to right
    def flipImage(self):
        for character in self.c_left:
            self.c_right.append(pygame.transform.flip(character, True, False))
    
    # [direction] positive number going to right, negative going to left
    def move_x(self, direction):
        self.rect.x += direction

    # [direction] positive number going down, negative going up
    def move_y(self, direction):
        self.rect.y += direction

    def handleCollision(self, objects, screen):
        for obj in objects:
            if self.left or self.right:
                if self.rect.y > obj.rect.y:
                    obj.front = True
                elif self.rect.y <= obj.rect.y:
                    obj.front = False

            if pygame.sprite.collide_mask(self, obj):
                if obj._type == 'animated_once':
                    if obj.stop == False:
                        obj.animateObj = True
                        obj.animateOnce(screen)
                    else:
                        obj.animatedObj = False

                else:
                    obj.stop = False

                if obj._type != 'hidden2':
                    if self.left:
                        if self.rect.y <= obj.rect.y:
                            self.rect.left = obj.rect.right
                    elif self.right:
                        if self.rect.y <= obj.rect.y:
                            self.rect.right = obj.rect.left

                    elif self.up and obj.front:
                        if self.rect.top < obj.rect.bottom - 40:
                            self.rect.top = obj.rect.bottom - 40
                    elif self.down and not(obj.front):
                        self.rect.bottom = obj.rect.top
                else:
                    if self.left:
                        self.rect.left = obj.rect.right
                    elif self.right:
                        self.rect.right = obj.rect.left
                    elif self.up:
                        self.rect.top = obj.rect.bottom
                    elif self.down:
                        self.rect.bottom = obj.rect.top

# enemy variant 1
class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, name=''):
        super().__init__()
        self.width = width
        self.height = height
        self.name = name

        # rect
        self.rect = pygame.Rect((x, y), (self.width, self.height))
        self.image = pygame.Surface((self.width, self.height))

        self.speed = random.choice([2.5, 3, 3.5])

        # facing
        self.left = True
        self.right = False
        self.up = False
        self.down = False
        self.walk = 0 # count of walk

        # images / character
        self.e_left = []
        self.e_right = []
        # load and flip image
        self.loadImages()
        self.flipImage()

    # draw the enemy
    def draw(self, screen, objects):

        # handle collision
        self.handleCollision(objects)
        
        if (self.walk + 1) >= 21:
            self.walk = 0

        if self.left or self.up:
            if self.rect.x > 0 and self.rect.x < 700 and self.rect.y > -20 and self.rect.y < 500:
                screen.blit(self.e_left[self.walk//3], (self.rect.x, self.rect.y))
            self.walk += 1
        elif self.right or self.down:
            if self.rect.x > 0 and self.rect.x < 700 and self.rect.y > -20 and self.rect.y < 500:
                screen.blit(self.e_right[self.walk//3], (self.rect.x, self.rect.y))
            self.walk += 1
        else:
            if self.rect.x > 0 and self.rect.x < 700 and self.rect.y > -20 and self.rect.y < 500:
                if self.left:
                    screen.blit(self.e_left[0], (self.rect.x, self.rect.x))
                elif self.right:
                    screen.blit(self.e_right[0], self.rect.x, self.rect.y)

        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 1)

    # enemy x and y move directions
    def move_x(self, direction):
        self.rect.x += direction

    def move_y(self, direction):
        self.rect.y += direction

    # enemy follow player until player's life is 0
    def follow(self, player):
        if player.life > 0:
            if self.rect.x > player.rect.x + 35:
                self.left = True
                self.right = False
                self.up = False
                self.down = False
                self.move_x(self.speed * -1)
            elif self.rect.x < player.rect.x - 35:
                self.left = False
                self.right = True
                self.up = False
                self.down = False
                self.move_x(self.speed)
            elif self.rect.y > player.rect.y + 35:
                self.left = False
                self.right = False
                self.up = True
                self.down = False
                self.move_y(self.speed * -1)
            elif self.rect.y < player.rect.y - 35:
                self.left = False
                self.right = False
                self.up = False
                self.down = True
                self.move_y(self.speed)
            else:
                self.walk = 0

    # load enemies image
    def loadImages(self):
        for character in range(7):
            image = f'characters/goblin/S_Walk_{character+1}.png'
            image = pygame.image.load(image)
            image = pygame.transform.scale(image, (self.width, self.height))
            self.e_left.append(image)

    # flip the image of enemy
    def flipImage(self):
        for character in self.e_left:
            self.e_right.append(pygame.transform.flip(character, True, False))

    # enemies collision
    def handleCollision(self, objects):
        for object in objects:
            if object._type != 'hidden2':
                if self.left or self.right:
                    if self.rect.y > object.rect.y:
                        object.e_front.append(self)
                    elif self.rect.y <= object.rect.y:
                        if self in object.e_front:
                            object.e_front.remove(self)
            if pygame.sprite.collide_mask(self, object):
                if object._type != 'hidden2':
                    if self.left:
                        if self.rect.y <= object.rect.y:
                            self.rect.left = object.rect.right
                    elif self.right:
                        if self.rect.y <= object.rect.y:
                            self.rect.right = object.rect.left

                    elif self.up and self in object.e_front:
                        if self.rect.top < object.rect.bottom - 40:
                            self.rect.top = object.rect.bottom - 40
                    elif self.down and self not in object.e_front:
                        self.rect.bottom = object.rect.top
                else:
                    if self.right:
                        self.rect.right = object.rect.left
                    elif self.left:
                        self.rect.left = object.rect.right
                    elif self.up:
                        self.rect.top = object.rect.bottom
                    elif self.down:
                        self.rect.bottom = object.rect.top