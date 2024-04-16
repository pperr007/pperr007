
import pygame

class Ship:
 """A class to manage the ship."""
 def __init__(self, ai_game):
    """Initialize the ship and set its starting position."""
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
     
     # Load the ship image and get its rect.
    self.image = pygame.image.load('ship.bmp')
    self.image = pygame.transform.scale(self.image, (60, 58))
    self.rect = self.image.get_rect()
    # Start each new ship at the bottom center of the screen.
    self.rect.midbottom = self.screen_rect.midbottom
 def blitme(self):
    """Draw the ship at its current location."""
    self.screen.blit(self.image, self.rect)

 def center_ship(self):
    """center the ship on the screen."""
    self.rect.midbottom = self.screen_rect.midbottom
    self.x = float(self.rect.x)








#class ship:
    #def __init__(self, ai_game):
        #self.screen = ai_game.screen
        #self.screen.rect = ai_game.screeen.get.rect()
