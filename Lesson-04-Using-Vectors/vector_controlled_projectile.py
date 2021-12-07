import pygame
WIDTH = 600
HEIGHT = 600
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Circle_Sprite(pygame.sprite.Sprite):
    def __init__(self, app, x, y, speed, angle):
        super().__init__()
        self.game = app
        self.image = pygame.Surface( (50, 50) )
        pygame.draw.circle(self.image, BLUE, (25, 25), 25)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(speed, 0)
        self.vel = self.vel.rotate(angle)
        self.acc = pygame.math.Vector2(0, 10)
        self.rect.center = self.pos
    
    def update(self):
        dt = self.game.dt
        self.vel += self.acc * dt
        self.pos += 0.5 * self.acc * dt ** 2 + self.vel * dt
        self.rect.center = self.pos

class Application:
    def __init__(self):
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        self.sprites = pygame.sprite.Group()
        self.circle = Circle_Sprite(self, 100, 200, 50, -45)
        self.sprites.add(self.circle)
        self.running = True
        self.clock = pygame.time.Clock()
        self.paused = False
        
    def gameloop(self):
        self.dt = self.clock.tick(60) / 1000
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.paused = not self.paused
            # flip the display
            self.screen.fill(WHITE)
            if not self.paused:
                self.sprites.update()
            self.sprites.draw(self.screen)
            self.draw_vectors()
            pygame.display.flip()
            
    def draw_vectors(self):
        pygame.draw.line(self.screen, RED, self.circle.pos, self.circle.pos + self.circle.vel)
        pygame.draw.line(self.screen, GREEN, self.circle.pos, self.circle.pos + self.circle.acc)

def main():
    pygame.init()
    app = Application()
    app.gameloop()
    pygame.quit()
    
if __name__ == '__main__':
    main()
