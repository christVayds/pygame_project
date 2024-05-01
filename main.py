"""
Game name: Back in Time
Project: Application Development and Emerging Technology
Professor: Gary Bato-ey

Frames: 30 fps
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
from Data.read import Read
from UI import UI

# IMPORT MAPS
# from Maps.map1 import TileMap as Map1 
from Maps import baseMap # MAP1 / BASE
from Maps import Map_2

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
base = baseMap.TileMap(25, 0, 0)
map_2 = Map_2.TileMap(25, 0, 0)

# GUIs (not yet draw)
itemsGUI = UI((windowSize['width'] - 350) / 2, (windowSize['height'] - 80), 350, 70)

# pause button
pauseButton = UI((windowSize['width'] - 60), 10, 50, 50)

# player Icon and health bar
playerIcon = UI(10, 10, 70, 70)
healthbar = UI(90, 10, 150, 70)

# PLAYER
player = Player(((windowSize['width'] - 50) / 2), ((windowSize['height'] - 50) / 2), 50, 50)

# enemies for map 2
enemy1 = Enemy(100, 100, 50, 50, 'goblin')

# read object data from json file data
readData = Read('Data/data.json')
readData.read() # read all data
readData.strToTuple('Base') # make all string tuple in Map1 to tuple
readData.strToTuple('Map2')

# create objects for blocks and other objects - Map 1 / base
create_base = Create(window, player, readData.data['Base'])
create_base.create()

# create objects for blocks and other objects - Map 1 / base
create_map2 = Create(window, player, readData.data['Map2'])
create_map2.create()

# camera
camera = Camera(player, windowSize)

# LISTS - BASE
listenemies = [enemy1] # only for map2 and map3(void)

# LIST of all objects in map 1 / Base
allObjects1 = create_base.listofObjects+[base]
allObjects2 = create_map2.listofObjects+[map_2]+listenemies

# create.listofObjects is a list of all objecst
# listenemies is a list of all enemies
# listOfMap is a list of map tiles

# draw base map function
def draw_base():

    window.fill((54, 54, 54))

    # map for the base map
    base.drawMap(window)

    # draw object
    create_base.draw()

    # draw player
    player.draw(window, create_base.listofObjects[1:])

    # camera
    camera.move(allObjects1)

    pygame.display.flip()

# draw MAP 2 funtion
def draw_map2():
    window.fill((54, 54, 54))

    # draw map 2
    map_2.drawMap(window)

    # draw objects
    create_map2.draw()

    # enemies / uncomment later
    # enemy1.draw(window, create.listofObjects[1:])
    # enemy1.follow(player)

    # draw player
    player.draw(window, create_map2.listofObjects[1:])

    # camera for map 2
    camera.move(allObjects2)

    pygame.display.flip()

# opening scene function / credits and loading
def Opening():

    window.fill((54, 54, 54))

    pygame.display.flip()

# for testing
fpsCollected = [] # collecting frames per second value

# main function
def main():
    run = True

    while run:

        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # draw the display
        if player.location == 'base':
            draw_base()
        elif player.location == 'map2':
            draw_map2()

        # for testing
        chechFPS(round(clock.get_fps(), 2))

        # fps of the game
        clock.tick(fps)

    # quit program after the loop
    print('fps timeline:',fpsCollected)
    print('lowest:', min(fpsCollected), '\nHighest:', max(fpsCollected), '\nLocation:', player.location)
    pygame.quit()

# function for testing

# frame drops test
def chechFPS(frames):
    if frames not in fpsCollected and frames >= 1:
        fpsCollected.append(frames)

# main program
if __name__=='__main__':
    main()