import sys
from time import sleep
import pygame
from settings import settings
from GameStats import GameStats
import bullet
import ship
import alien

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
            elif event.key == pygame.K_RIGHT:
                self.dx = 3
            elif event.key == pygame.K_UP:
                self.dy = -3
            elif event.key == pygame.K_DOWN:
                self.dy = 3
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_RIGHT:
        #         self.dx = 0.5
        #     elif event.key == pygame.K_LEFT:
        #         self.dx = -0.5
        #     elif event.key == pygame.K_UP:
        #         self.dy = -0.5
        #     elif event.key == pygame.K_DOWN:
        #         self.dy = 0.5
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
  self.aliens.draw(self.screen)
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
    self.aliens = pygame.sprite.Group()
    self._create_fleet()
    self.stats = GameStats(self)
    self.game_active = True

 def _ship_hit(self):
    """Respond to the ship being hit by an alien"""
    if self.stats.ships_left > 0:
        self.stats.ships_left -= 1
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.ship.center_ship()
        sleep(0.5)
    else :
        self.game_active = False
 
 def _update_bullets(self):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    self.bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
            self.bullets.remove(bullet)
    self._check_bullet_alien_collisions()
    if not self.aliens:
        self.bullets.empty()
        self._create_fleet()
 def _check_bullet_alien_collisions(self):
    """Respond to bullet-alien collisions."""
    collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
 
 def _check_aliens_bottom(self):
    """Check if any aliens have reached the bottom of the screen"""
    for alien in self.aliens.sprites():
        if alien.rect.bottom >= self.settings.screen_height:
            self._ship_hit()
            break

 def _update_aliens(self):
    """Update the positions of all the aliens in the fleet."""
    self._check_fleet_edges()
    self.aliens.update()
    if pygame.sprite.spritecollideany(self.ship, self.aliens):
        print("Ship hit!!!")
        self._ship_hit()
    self._check_aliens_bottom()

 def _create_fleet(self):
    """Create the fleet of aliens."""
    # Make an alien.
    myalien = alien.Alien(self)
    alien_width , alien_height = myalien.rect.size
    self.aliens.add(myalien)
    alien_width = myalien.rect.width
    alien_height = myalien.rect.height
    current_x, current_y = alien_width, alien_height
    while current_y < (self.settings.screen_height - 3 * alien_height):
        while current_x < (self.settings.screen_width - 2 * alien_width):
            self._create_alien(current_x,current_y)
            current_x += 2 * alien_width
            
        current_x = alien_width
        current_y += 2 * alien_height
 
 def _check_fleet_edges(self):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in self.aliens.sprites():
        if alien.check_edges():
            self._change_fleet_direction()
            break
 def _change_fleet_direction(self):
    """Drop the entire fleet and change the fleet's direction"""
    for alien in self.aliens.sprites():
        alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1    
 def _create_alien(self, x_position, y_position):
     """Create an alien and add it to the row"""
     new_alien = alien.Alien(self)
     new_alien.x = x_position
     new_alien.rect.x = x_position
     new_alien.y = y_position
     new_alien.rect.y = y_position
     self.aliens.add(new_alien)

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

        if self.game_active:   
            self._update_bullets()
            self._update_aliens()
        self._update_screen()
        self.clock.tick(60)


if __name__ == "__main__":
    print("Create game object...")
    ai = AlienInvasion()

    print("Running game...")
    ai.run_game()

    print("Game complete")