import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
image = pygame.image.load('game_guy.png') # load image
image = image.convert_alpha() # convert the pixel format to match screen
screen.blit(image, (400, 300)) # paint image at location (400, 300)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # flip the display
    pygame.display.flip()
pygame.quit()