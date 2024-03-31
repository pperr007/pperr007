import sys
import pygame
from settings import settings
import bullet
import ship

class AlienInvasion:
 """Overall class to manage game assets and behavior."""
 
 def _check_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                print('QUIT recieved')
                return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.dx = -3
                print("firing")
            elif event.key == pygame.K_RIGHT:
                self.dx = 3
            elif event.key == pygame.K_UP:
                self.dy = -3
            elif event.key == pygame.K_DOWN:
                self.dy = 3
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
        else:
            self.dx = 0
            self.dy = 0

    return True
 

 def _fire_bullet(self):
    """Create a new bullet and add it to the bullets group."""
    if len(self.bullets) < self.settings.bullet_allowed:
        new_bullet = bullet.Bullet (self)
        self.bullets.add(new_bullet)

 def _update_screen(self):
  """Update images on the screen, and flip to the new screen."""
  self.screen.fill(self.settings.bg_color)
  for bullet in self.bullets.sprites():
    bullet.draw_bullet()
  self.ship.blitme()
  pygame.display.flip()


 def __init__(self):
    """Initialize the game, and create game resources."""
    self.dx = 0
    self.dy = 0
    pygame.init()
    self.settings = settings()
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #tuple

    pygame.display.set_caption("Alien Invasion")

    self.clock = pygame.time.Clock()
    
    self.screen = pygame.display.set_mode()

    pygame.display.set_caption("03 Alien Invasion")
    self.ship = ship.Ship(self)
    self.bullets = pygame.sprite.Group()
 
 def _update_bullets(self):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    self.bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
            self.bullets.remove(bullet)


 def run_game(self):
    """Start the main loop for the game."""
    while True:
 # Make the most recently drawn screen visible.
        pygame.display.flip()
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
            self.ship.rect.right = self.screen.get_width()
        if self.ship.rect.bottom > self.screen.get_height():
            self.ship.rect.bottom = self.screen.get_height()

            #SPEEDY
        self.dx *= 1.05
        self.dy *= 1.05
            #look into def _check_events if have this in your code
        
        self._check_events()
        self._update_bullets()
        self._update_screen()
        self.clock.tick(60)


if __name__ == "__main__":
    print("Create game object...")
    ai = AlienInvasion()

    print("Running game...")
    ai.run_game()

    print("Game complete")