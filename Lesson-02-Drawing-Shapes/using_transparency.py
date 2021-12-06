import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# create a screen
screen = pygame.display.set_mode((800, 600))
# make the screen a white background
screen.fill(WHITE)

# create a surface that will perfectly fit a circle with radius 50
radius = 50
image = pygame.Surface( (radius * 2, radius * 2) )
x, y = radius, radius
pygame.draw.circle(image, RED, (x, y), radius)

# make BLACK transparent
image.set_colorkey(BLACK)

# draw the circle image on the screen. 
screen.blit(image, (400, 300))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # flip the display
    pygame.display.flip()
pygame.quit()