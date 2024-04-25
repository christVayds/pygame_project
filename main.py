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

# initialize pygame
pygame.init()

# screen
windowSize = {'width': 700, 'height': 500} # size of the display
window = pygame.display.set_mode((windowSize['width'], windowSize['height']))
pygame.display.set_caption('Project Exodus')

# clock and FPS - frame per second
clock = pygame.time.Clock()
fps = 30 # 30 frames per second

# objects and items lists
objects = []
items = []
enimies = []

# PLAYER
player = Player(((windowSize['width'] - 50) / 2), ((windowSize['height'] - 50) / 2), 50, 50)

# enemies
enemy1 = Enemy(100, 100, 50, 50, 'goblin')

listenemies = [enemy1]

# OBJECTS
listofobj = [
        {'name': '7', 'type': 'Stone', 'rect': (50, 200, 50, 50), 'collide': True},
        {'name': '7', 'type': 'Stone', 'rect': (50, 300, 50, 50), 'collide': True}
    ]

# create objects for blocks
create = Create(window, player, listofobj)
create.create()

# camera
camera = Camera(player, windowSize)

# draw function
def draw():
    window.fill((54, 54, 54))

    # draw object
    create.draw()

    # draw enemy
    enemy1.draw(window)
    enemy1.follow(player)

    # draw player
    allobj = create.listofObjects+listenemies # list of object fron index 1 - ...N
    player.draw(window, create.listofObjects[1:])

    # the camera
    camera.move(allobj)

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