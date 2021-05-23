import sys

import pygame

from settings import Settings
from sheep import Sheep


class GrassGame:
    """草原游戏"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("草原游戏")

        self.sheep = Sheep(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.sheep.blitme()

        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


if __name__ == '__main__':
    grass_game = GrassGame()
    grass_game.run_game()
