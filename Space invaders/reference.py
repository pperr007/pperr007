import pygame
import settings
import ship

class Alien_Invasion:
    """The Game"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = settings()
        self.screen = pygame.display.set_mode()

        pygame.display.set_caption("03 Alien Invasion")
        self.ship = ship(self)

        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))#tuple
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Runs the Game"""
        while True:
            if not self._check_events():
                return
            
            #always move ship
            self.ship.rect.x += self.dx
            self.ship.rect.y += self.dy

            #keep ship on screen
            if self.ship.rect.x < 0:
                self.ship.rect.x = 0
                self.dx = 0
            if self.ship.rect.y < 0:
                self.ship.rect.y = 0
                self.dx = 0
            if self.ship.rect.right > self.screen.get_width():
                self.ship.rect.right = self.screen.geth_width()
            if self.ship.rect.bottom > self.screen.get_height():
                self.ship.rect.bottom = self.screen.get_height()

            #SPEEDY
            self.dx *= 1.05
            self.dy *= 1.05
            #look into def _check_events if have this in your code

            self._update_screen()
            self.clock.tick(60)
    
 
    


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('QUIT recieved')
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.dx = -3
                elif event.key == pygame.K_RIGHT:
                    self.dx = 3
                elif event.key == pygame.K_UP:
                    self.dy = 3
                elif event.key == pygame.K_DOWN:
                    self.dy = -3
            elif event.type == pygame.KEYUP:
                self.dx = 0
                self.dy = 0



