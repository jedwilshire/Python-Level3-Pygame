import pygame
WIDTH = 600
HEIGHT = 600
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Circle_Sprite(pygame.sprite.Sprite):
    def __init__(self, app, x, y):
        super().__init__()
        self.game = app
        self.image = pygame.Surface( (50, 50) )
        pygame.draw.circle(self.image, BLUE, (25, 25), 25)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(50, -50)
        self.acc = pygame.math.Vector2(0, 20)
        self.rect.center = self.pos
    
    def check
    
    def update(self):
        self.check_keys()
        dt = self.game.dt
        self.vel += self.acc * dt
        self.pos += 0.5 * self.acc * dt ** 2 + self.vel * dt
        self.rect.center = self.pos

class Application:
    def __init__(self):
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        self.sprites = pygame.sprite.Group()
        circle = Circle_Sprite(self, 100, 200)
        self.sprites.add(circle)
        self.running = True
        self.clock = pygame.time.Clock()
        
    def gameloop(self):
        self.dt = self.clock.tick(60) / 1000
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # flip the display
            self.screen.fill(WHITE)
            self.sprites.update()
            self.sprites.draw(self.screen)
            pygame.display.flip()

def main():
    pygame.init()
    app = Application()
    app.gameloop()
    pygame.quit()
    
if __name__ == '__main__':
    main()
