import pygame

class TileMap():
    def __init__(self, tilesize):
        pygame.init()
        self.tilesize = tilesize
        self.images = []
        self.images.append(pygame.transform.scale(pygame.image.load("C:/Users/Admin/OneDrive/Documents/pygame_project/characters/objects/floor_2.png"), (self.tilesize, self.tilesize)))
        self.images.append(pygame.transform.scale(pygame.image.load("C:/Users/Admin/OneDrive/Documents/pygame_project/characters/objects/border_3.png"), (self.tilesize, self.tilesize)))
        self.images.append(pygame.transform.scale(pygame.image.load("C:/Users/Admin/OneDrive/Documents/pygame_project/characters/objects/floor_1.png"), (self.tilesize, self.tilesize)))
        self.images.append(pygame.transform.scale(pygame.image.load("C:/Users/Admin/OneDrive/Documents/pygame_project/characters/objects/wall_1.png"), (self.tilesize, self.tilesize)))
        self.images.append(pygame.transform.scale(pygame.image.load("C:/Users/Admin/OneDrive/Documents/pygame_project/characters/objects/border_1.png"), (self.tilesize, self.tilesize)))
        self.array = [[1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,3,3,3],
[1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,3,3,3],
[1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,1,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,1,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,3,3,5,5,2,5,2,3,3,3,3,3,3,3,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,3,3,1,1,1,1,2,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,4,4,1,1,1,1,2,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,2,4,4,4,4,4,4,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,2,5,5,5,5,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,2,4,4,4,4,4,4,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,2,1,1,1,1,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,2,1,1,1,1,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,1,3,3,3,3,3,3,3,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,1,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,5,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,5,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,5,3,3,3,3,3,3,3,2,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,2,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,2,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,2,3,3,3],
[5,5,5,5,5,5,5,5,5,2,3,3,3,3,3,3,3,2,5,5,5,5,5,5,5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,5,5,5,5,5,5,5,5,2,3,3,3,3,3,3,2,3,3,3],
[1,1,1,1,1,1,1,1,1,2,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,2,3,3,3],
[1,1,1,1,1,1,1,1,1,2,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,5,5,5,5,3,3,5,5,5,5,5,5,5,5,5,5,5,5,3,3,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,2,1,1,1,3,3,1,1,1,1,2,1,1,1,1,1,1,1,3,3,3,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,2,1,1,1,3,3,1,1,1,1,2,1,1,1,1,1,1,1,3,3,3,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,2,5,5,3,3,3,5,5,2,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,1,1,1,4,4,4,1,1,2,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,1,1,1,4,4,4,1,1,2,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3],
[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3],
[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,5,5,5,5,5,2,2,2,2],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    def drawMap(self, surface, location):
            for i,row in enumerate(self.array):
                for j,tile in enumerate(row):
                    if tile > 0:
                        surface.blit(self.images[tile - 1], (location[0] + j * self.tilesize, location[1] + i * self.tilesize))