import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Circle_Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface( (50, 50) )
        pygame.draw.circle(self.image, BLUE, (25, 25), 25)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.rect.x += 1
        
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
sprites = pygame.sprite.Group()
sprite1 = Circle_Sprite(100, 200)
sprites.add(sprite1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # flip the display
    screen.fill(WHITE)
    sprites.update()
    sprites.draw(screen)
    pygame.display.flip()
pygame.quit()