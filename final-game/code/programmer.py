import pygame

class Programmer:
    def __init__(self, screen):
        """Initialise a programmer"""
        self.screen = screen
        self.image = pygame.image.load('/Users/rustya/Desktop/M.Sc./1st sem/Python Basic/Assignments/final_game_Magomedov/images/prog.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.center = float(self.rect.centery)  # for smooth movement
        self.rect.midleft = self.screen_rect.midleft
        self.mdown = False
        self.mup = False

    def programmer(self):
        """Draw a programmer"""
        self.screen.blit(self.image, self.rect)

    def get_programmer_position(self):
        """get programmer's position"""
        # moving down
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.center += 3.5
        # moving up
        elif self.mup and self.rect.top > 0:
            self.center -= 3.5
        self.rect.centery = self.center

    def revive_programmer(self):
        """revies programmer in case of approached deadline"""
        self.midleft = self.screen_rect.midleft
