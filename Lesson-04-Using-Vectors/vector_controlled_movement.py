import pygame
WIDTH = 1000
HEIGHT = 800
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
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
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)
        self.rect.center = self.pos
    
    def update(self):
        self.check_keys()
        dt = self.game.dt
        self.vel += self.acc * dt
        self.pos += 0.5 * self.acc * dt ** 2 + self.vel * dt
        self.rect.center = self.pos

    def check_keys(self):
        acc_rate = 0.01
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc += pygame.math.Vector2(-acc_rate, 0)
        if keys[pygame.K_RIGHT]:
            self.acc += pygame.math.Vector2(acc_rate, 0)
        if keys[pygame.K_DOWN]:
            self.acc += pygame.math.Vector2(0, acc_rate)
        if keys[pygame.K_UP]:
            self.acc += pygame.math.Vector2(0, -acc_rate)
        
        
class Application:
    def __init__(self):
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        self.sprites = pygame.sprite.Group()
        self.circle = Circle_Sprite(self, 100, 200)
        self.sprites.add(self.circle)
        self.running = True
        self.clock = pygame.time.Clock()
        
    def gameloop(self):
        self.dt = self.clock.tick(60) / 1000
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill(WHITE)
            self.sprites.update()
            self.sprites.draw(self.screen)
            self.draw_vectors()
            pygame.display.flip()

    def draw_vectors(self):
        # for visual effect vel vector is scaled by x 10 and acc vect by x 100
        pygame.draw.line(self.screen, RED, self.circle.pos, self.circle.pos + self.circle.vel * 10, width = 4)
        pygame.draw.line(self.screen, GREEN, self.circle.pos, self.circle.pos + self.circle.acc * 100, width = 4)

def main():
    pygame.init()
    app = Application()
    app.gameloop()
    pygame.quit()
    
if __name__ == '__main__':
    main()
