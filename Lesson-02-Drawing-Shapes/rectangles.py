import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
# Drawing a red rectangle on screen at x = 100, y = 200, width = 50, height = 25
pygame.draw.rect(screen, RED, (100, 200, 50, 25))
pygame.draw.rect(screen, BLUE, (500, 400, 100, 20), width = 1)

my_rect = pygame.Rect(150, 550, 40, 40)
pygame.draw.rect(screen, GREEN, my_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # flip the display
    pygame.display.flip()
pygame.quit()