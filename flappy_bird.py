#not done!

import random
import sys
import pygame
from pygame.locals import *


#global variables
fps = 32
screenwidth = 289
screenheight = 511
screen = pygame.display.set_mode((screenwidth, screenheight))



player = 'resources/1.jpg'

if __name__ == "__main__":

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird with Sofus")

