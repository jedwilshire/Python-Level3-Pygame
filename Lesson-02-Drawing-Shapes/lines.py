import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

pygame.draw.line(screen, BLUE, (100, 200), (600, 50))
pygame.draw.line(screen, GREEN, (200, 300), (400, 400), width = 3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # flip the display
    pygame.display.flip()
pygame.quit()