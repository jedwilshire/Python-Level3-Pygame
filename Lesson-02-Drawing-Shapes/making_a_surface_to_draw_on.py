import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

image = pygame.Surface( (100, 100) )
x, y = image.get_width() / 2, image.get_height() / 2
pygame.draw.circle(image, RED, (x, y), 20) 
screen.blit(image, (400, 300))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # flip the display
    pygame.display.flip()
pygame.quit()