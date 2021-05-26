#
# 外星人类
#
import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """外星人类"""

    def __init__(self, ai_game):
        """初始化"""
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def check_edge(self):
        """检查是否到了边缘"""
        if self.rect.right >= self.screen_rect.right or self.rect.left <= self.screen_rect.left:
            return True

    def update(self):
        """更新坐标"""
        if self.settings.alien_move_direct == 1:
            self.x += self.settings.alien_x_speen
        elif self.settings.alien_move_direct == -1:
            self.x -= self.settings.alien_x_speen

        # self.y += self.settings.alien_speen

        self.rect.x = self.x
        # self.rect.y = self.y

    def blitme(self):
        """将图片画出来"""
        self.screen.blit(self.image, self.rect)
