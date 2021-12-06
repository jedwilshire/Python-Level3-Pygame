import pygame

WIDTH = 800 # these values may be stored in a setting.py module
HEIGHT = 600
class Application:
    def __init__(self):
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        self.sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.running = True

    
        
    def gameloop(self):
        while self.running:
            #
            self.dt = self.clock.tick(FPS) / 1000
            self.update_events()
            
            # update particle logic and positions
            self.sprites.update()
            
            # update the screen
            self.update_screen()    
    
    def update_screen(self):
        self.screen.fill(WHITE)
        self.particles_group.draw(self.screen)
        pygame.display.flip()
    
    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
                    
                    
def main():
    pygame.init()
    app = Application()
    app.gameloop()
    pygame.quit()

if __name__ == '__main__':
    main()
