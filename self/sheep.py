import pygame


class Sheep:
    """小羊"""

    def __init__(self, game_ui):
        self.screen = game_ui.screen
        self.screen_rect = game_ui.screen.get_rect()

        self.image = pygame.image.load("../images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
