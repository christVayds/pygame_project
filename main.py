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
from Data.read import Read

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

# read object data from json file data
readData = Read('Data/data.json')
readData.read() # read all data
readData.strToTuple('Map1') # make all string tuple in Map1 to tuple

# create objects for blocks and other objects
create = Create(window, player, readData.data['Map1'])
create.create()

# camera
camera = Camera(player, windowSize)

# LISTS
listenemies = [enemy1]
listOfMap = [map1]

# all objects in map 1
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
        print(round(clock.get_fps()), 2)

    # quit program after the loop
    pygame.quit()

# main program
if __name__=='__main__':
    main()