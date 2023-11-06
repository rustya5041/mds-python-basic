import pygame


class Deadline(pygame.sprite.Sprite):
    """Class of a deadline - the worst enemy one can imagine"""
    def __init__(self, screen):
        """initialising deadline"""
        super(Deadline, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('/Users/rustya/Desktop/M.Sc./1st sem/Python Basic/Assignments/final_game_Magomedov/images/clock.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.height
        self.rect.y = self.rect.width
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # place the deadline in the middle right
        self.rect.right = self.screen.get_rect().right

    def draw_deadline(self):
        """Blits a deadline on a right middle of the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the deadline position"""
        self.x -= 0.9
        self.rect.x = self.x
