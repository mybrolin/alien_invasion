#
# 看板
#
import pygame
from pygame.sprite import Sprite
from pygame.font import Font
from ship_icon import ShipIcon


class DashBoard:
    """游戏状态看板"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.status = ai_game.gameStatus
        self.setting = ai_game.settings

        self.font = Font(None, self.setting.button_text_font_size)

        self.left_ships = pygame.sprite.Group()

    def prop_score(self):
        """显示分数"""
        score_str = str(self.status.current_score)
        self.score_image = self.font.render(score_str, True, self.setting.button_text_color, self.setting.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = self.screen_rect.top + 20

        max_score_str = str(self.status.max_score)
        self.max_score_image = self.font.render(max_score_str, True, self.setting.button_text_color,
                                                self.setting.bg_color)
        self.max_score_image_rect = self.max_score_image.get_rect()
        self.max_score_image_rect.center = self.screen_rect.center
        self.max_score_image_rect.top = self.screen_rect.top + 20

    def prop_left_life(self):
        """显示剩余生命数"""
        self.left_ships.empty()
        for i in range(self.status.ship_left):
            self.left_ships.add(ShipIcon(self.screen, i + 1))

    def show_dash_board(self):
        """画计分板"""
        self.prop_score()
        self.prop_left_life()

        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.max_score_image, self.max_score_image_rect)
        self.left_ships.draw(self.screen)
