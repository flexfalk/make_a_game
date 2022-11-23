import pygame
from math import pi
pygame.init()

#size variable is using for set screen size
size = [400, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Example program to draw geometry")

#done varialbe is using as flag
done = False
clock = pygame.time.Clock()
while not done:
    #limits the while loop to max 10 times pr sec.
    clock.tick(10)


    for event in pygame.event.get(): #user did something
        if event.type == pygame.QUIT: #if user clicked quit
            done = True

    screen.fill((255, 255, 255))

    #draw on the screen a green line which is 5 pixels wide
    pygame.draw.line(screen, (0,255,0), [0,0], [50, 30], 5)

    pygame.draw.lines(screen, (0, 0, 0), False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)

    # Draw a rectangle outline
    pygame.draw.rect(screen, (0, 0, 0), [75, 10, 50, 20], 2)



    pygame.display.flip()

pygame.quit()