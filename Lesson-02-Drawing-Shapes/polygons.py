import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
points = [(50, 100), (50, 200), (100, 150)]
pygame.draw.polygon(screen, GREEN, points)
pygame.draw.polygon(screen, RED, points, width = 2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # flip the display
    pygame.display.flip()
pygame.quit()