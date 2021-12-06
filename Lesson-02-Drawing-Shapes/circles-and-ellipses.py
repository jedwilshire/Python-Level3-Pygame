import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

pygame.draw.circle(screen, BLUE, (400, 300), 50)
pygame.draw.circle(screen, RED, (100, 400), 25, width = 1)

rect1 = pygame.Rect(550, 200, 75, 75)
pygame.draw.ellipse(screen, GREEN, rect1)
rect2 = pygame.Rect(200, 40, 100, 50)
pygame.draw.ellipse(screen, BLUE, rect2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # flip the display
    pygame.display.flip()
pygame.quit()