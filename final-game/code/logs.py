import pygame.font


class Logs:
    """initialising statistics"""
    def __init__(self):
        """initialize stats"""
        self.wipe()
        self.continue_game = True

    def wipe(self):
        """dynamic changes of lives available"""
        self.lives_left = 3  # max 3 retakes at HSE
        self.score = 0


class Score:
    def __init__(self, screen, logs):
        """initialising score"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.logs = logs
        self.text_color = (0, 0, 0)
        self.speed = 1
        self.font = pygame.font.SysFont(None, 40, italic=True)
        self.score_params()

    def score_params(self):
        """display score"""
        score_str = str(self.logs.score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = self.screen_rect.top + 25
        self.score_rect.right = self.screen_rect.right - 25

    def show_score(self):
        """show score on screen"""
        self.screen.blit(self.score_image, self.score_rect)
