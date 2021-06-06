#
# 飞船
#
import pygame
from pygame.sprite import Sprite


class ShipIcon(Sprite):
    """外星飞船"""

    def __init__(self, ai_screen, life_count):
        """初始化飞般并设置其初始位置"""
        super().__init__()

        self.screen = ai_screen  # 屏幕 Surface
        self.screen_rect = ai_screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship_life.bmp")  # 加载image，生成飞船Surface

        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏蔽底部的中央
        self.rect.top = self.screen_rect.top + 10
        self.rect.left = self.screen_rect.left + 10 + self.rect.width * (life_count - 1)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
