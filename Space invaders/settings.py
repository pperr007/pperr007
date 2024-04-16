import pygame 

class settings:
    """A class to store all settings for alien invasion"""
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.alien_speed = (5.0)
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 100

        #ship settings
        self.ship_limit = 3