#
# 看板
#
import pygame
from pygame.font import Font
from alien_invasion import AlienInvasion


class DashBoard:
    """游戏状态看板"""

    def __init__(self, ai_game: AlienInvasion):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.status = ai_game.gameStatus

        self.font = Font(None, ai_game.settings.button_text_font_size)
        self.current_score_rect = pygame.Rect(0, 0, ai_game.settings.button_size[0],
                                              ai_game.settings.button_size[1])
        self.current_score_rect.x = self.screen_rect.right - 250
        self.current_score_rect.y = self.screen_rect.top + 10

        self.heighest_score_rect = pygame.Rect(0, 0, ai_game.settings.button_size[0],
                                               ai_game.settings.button_size[1])

        self.heighest_score_rect.center = self.screen_rect.center
        self.heighest_score_rect.y = self.screen_rect.top + 10
