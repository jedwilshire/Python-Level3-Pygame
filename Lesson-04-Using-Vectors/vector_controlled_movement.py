import pygame
WIDTH = 600
HEIGHT = 600
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
class Circle_Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface( (50, 50) )
        pygame.draw.circle(self.image, BLUE, (25, 25), 25)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(50, -50)
        self.acc = pygame.math.Vector2(0, 20)
        self.rect.center = self.pos
        self.last_update_time = pygame.time.get_ticks()
        
    def update(self):
        current_time = pygame.time.get_ticks()
        dt = self.last_update_time - current_time
        self.vel += self.acc * dt
        self.pos += 0.5 * self.acc * dt ** 2 + self.vel * dt
        self.rect.center = self.pos
        self.last_update_time = current_time

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
sprites = pygame.sprite.Group()
circle = Circle_Sprite(100, 200)
sprites.add(circle)
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
    print(circle.pos)
pygame.quit()