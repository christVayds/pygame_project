"""
Game name: The Adventure of Christian
Project: Application Development and Emerging Technology
Professor: Gary Bato-ey

Frames: 21 fps
walking animation(character and enemy): 7 frames/images
characters size(character and enemy): 130x80 pixels

developers:
    1. Christian Vaydal
    2. Aeron Segobia
    3. Ethan Diego Lim

Date started: April 16, 2024
"""

import pygame
from character import *
from object import *
from create import Create
from camera import Camera
from lab import TileMap

# initialize pygame
pygame.init()

# screen
windowSize = {'width': 700, 'height': 500} # size of the display
window = pygame.display.set_mode((windowSize['width'], windowSize['height']))
pygame.display.set_caption('Project Exodus')

# clock and FPS - frame per second
clock = pygame.time.Clock()
fps = 30 # 30 frames per second

# MAP
map1 = TileMap(25, 0, 0)

# PLAYER
player = Player(((windowSize['width'] - 50) / 2), ((windowSize['height'] - 50) / 2), 50, 50)

# enemies
enemy1 = Enemy(100, 100, 50, 50, 'goblin')

# OBJECTS
listofobj = [
        {'name': '7', 'type': 'Stone', 'rect': (50, 200, 50, 50), 'collide': True},
        {'name': '7', 'type': 'Stone', 'rect': (50, 250, 50, 50), 'collide': True},

        # walls and other hidden rect
        {'name': 'hidden', 'type': 'hidden', 'rect': (0, 25, 250, 50)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (250, 25, 1000, 50)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (225, 25, 25, 300)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (225, 300, 25, 70)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (225, 425, 25, 425)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (0, 500, 250, 25)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (0, 550, 250, 50)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (225, 825, 75, 100)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (375, 825, 50, 100)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (0, 1050, 1600, 25)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (425, 675, 25, 400)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (425, 400, 25, 125)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (425, 150, 25, 150)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (425, 275, 25, 75)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (425, 550, 900, 50)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (425, 500, 900, 25)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (425, 150, 725, 25)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (1200, 150, 125, 25)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (625, 150, 25, 75)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (625, 225, 25, 75)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (450, 200, 175, 50)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (625, 325, 25, 175)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (1075, 175, 25, 325)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (630, 200, 520, 50)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (1300, 175, 25, 325)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (1200, 200, 100, 50)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (1325, 225, 100, 25)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (1325, 275, 100, 50)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (1275, 25, 200, 50)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (1250, 25, 25, 125)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (1475, 25, 25, 1025)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (675, 675, 25, 250)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (1175, 675, 25, 250)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (1325, 675, 25, 375)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (450, 675, 50, 25)}, # for extecd door
        {'name': 'hidden', 'type': 'hidden2', 'rect': (575, 675, 300, 25)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (950, 675, 375, 25)},
        {'name': 'hidden', 'type': 'hidden2', 'rect': (675, 900, 500, 25)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (675, 950, 525, 50)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (450, 725, 50, 50)}, # for extend door
        {'name': 'hidden', 'type': 'hidden', 'rect': (575, 725, 100, 50)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (700, 725, 175, 50)},
        {'name': 'hidden', 'type': 'hidden', 'rect': (950, 725, 400, 50)},
    ]

# create objects for blocks and other objects
create = Create(window, player, listofobj)
create.create()

# camera
camera = Camera(player, windowSize)

# LISTS
listenemies = [enemy1]
listOfMap = [map1]
allObjects = create.listofObjects+listenemies+listOfMap

# draw function
def draw():
    window.fill((54, 54, 54))

    # map
    map1.drawMap(window)

    # draw object
    create.draw()

    # draw enemy
    enemy1.draw(window, create.listofObjects[1:])
    enemy1.follow(player)

    # draw player
    player.draw(window, create.listofObjects[1:])

    # the camera
    camera.move(allObjects)

    pygame.display.flip()

# main function
def main():
    run = True

    while run:
        # fps of the game
        clock.tick(fps)

        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # draw the display
        draw()

    # quit program after the loop
    pygame.quit()

# main program
if __name__=='__main__':
    main()