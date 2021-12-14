import pygame
# these constants may be stored in a setting.py module
WIDTH = 800 
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
class Application:
    def __init__(self):
        # create the screen
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        # create a group for all sprites
        self.sprites = pygame.sprite.Group()
        # create a clock object to manage frame rate and ticks
        self.clock = pygame.time.Clock()
        # a bool value to end the game loop
        self.running = True

    
        
    def gameloop(self):
        while self.running:
            # maintain FPS rate and measure delta time
            self.dt = self.clock.tick(FPS) / 1000
            # handle all user events since last frame
            self.update_events()            
            # update sprite logic and positions
            self.sprites.update()           
            # update the screen
            self.update_screen()    
    
    def update_screen(self):
        # fill with background image or color
        self.screen.fill(WHITE)
        # draw sprites on screen
        self.sprites.draw(self.screen)
        # flip screen from previous frame to new frame
        pygame.display.flip()
    
    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # additional inputs can be handled here.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print('up')
                elif event.key == pygame.K_DOWN:
                    print('down')
                elif event.key == pygame.K_LEFT:
                    print('left')
                elif event.key == pygame.K_RIGHT:
                    print('right')
                    
                    
def main():
    pygame.init()
    app = Application()
    app.gameloop()
    pygame.quit()

if __name__ == '__main__':
    main()
