#
# 按钮类，可显示按钮和文字
#
import pygame.font


class Button:
    """按钮类"""

    def __init__(self, ai_game, mesg):
        """初始化"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.settings

        self.font = pygame.font.SysFont(None, self.setting.button_text_font_size)

        self.rect = pygame.Rect(0, 0, self.setting.button_size[0], self.setting.button_size[1])
        self.rect.center = self.screen_rect.center

        self._prop_mesg(mesg)

    def _prop_mesg(self, mesg):
        """显示信息"""
        self.msg_image = self.font.render(mesg, True, self.setting.button_text_color, self.setting.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """画按钮"""
        self.screen.fill(self.setting.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
