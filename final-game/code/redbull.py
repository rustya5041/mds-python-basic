import pygame
import random


class Redbull(pygame.sprite.Sprite):
    def __init__(self, screen, programmer):
        """initialising red bulls to fight deadlines"""
        super(Redbull, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 10)  # red bull size
        self.surf = pygame.image.load('/Users/rustya/Desktop/M.Sc./1st sem/Python Basic/Assignments/final_game_Magomedov/images/redbull.png')
        self.speed = random.randint(3, 5)  # adding random speed
        self.rect.centery = programmer.rect.centery  # red bull appears in the middle of the coder
        self.rect.right = programmer.rect.right  #
        self.x = float(self.rect.x)  # for smooth movement

    def update(self):
        """configuring redbull movement | nb. update is a method of pygame.sprite.Sprite and should not be changed"""
        self.x += self.speed
        self.rect.x = self.x

    def materialize_redbull(self):
        """drawing redbull"""
        self.screen.blit(self.surf, self.rect)  # red bull appears on the screen
