import pygame
WIDTH = 800
HEIGHT = 600
BLUE = (0, 0, 255)
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


class Application:
    def __init__(self):
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        self.sprites = pygame.sprite.Group()
        self.sprite1 = Circle_Sprite(100, 200)
        self.sprites.add(self.sprite1)
        self.running = True
        # set key mode so that held down key triggers a repeated keydown event ever 15 milliseconds
        pygame.key.set_repeat(15)
    
    def gameloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.sprite1.rect.x -= 4
                    elif event.key == pygame.K_RIGHT:
                        self.sprite1.rect.x += 4
                    elif event.key == pygame.K_DOWN:
                        self.sprite1.rect.y += 4
                    elif event.key == pygame.K_UP:
                        self.sprite1.rect.y -= 4
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