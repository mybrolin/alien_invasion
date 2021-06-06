#
# 飞船
#
import pygame


class Ship:
    """外星飞船"""

    def __init__(self, ai_game):
        """初始化飞般并设置其初始位置"""

        self.screen = ai_game.screen  # 屏幕 Surface
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")  # 加载image，生成飞船Surface

        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏蔽底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.move_right = False  # 向右移动标志
        self.move_left = False  # 向左移动标志
        self.move_up = False  # 向上移动
        self.move_down = False  # 向下移动

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.settings = ai_game.settings

    def update(self):
        """位置变化"""
        if self.move_right:
            # if self.rect.x + 1 < self.screen_rect.x:
            if self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
        # else:
        #     pass
        if self.move_left:
            # if self.rect.x - 1 > self.screen_rect.x:
            if self.rect.left > self.screen_rect.left:
                # if self.rect.left > 0:
                self.x -= self.settings.ship_speed
        # else:
        #     pass
        if self.move_up:
            #     if self.rect.y - 1 > self.screen_rect.y:
            if self.rect.top > self.screen_rect.top:
                # if self.rect.top > 0:
                self.y -= self.settings.ship_speed
        #     else:
        #         pass
        if self.move_down:
            #     if self.rect.y + 1 < self.screen_rect.y:
            if self.rect.bottom < self.screen_rect.bottom:
                self.y += self.settings.ship_speed
        #     else:
        #         pass
        # 更新坐标
        self.rect.x = self.x
        self.rect.y = self.y

    def back_center(self):
        """恢复到中心位置"""
        self.rect.center = self.screen_rect.center
        self.x = self.rect.x
        self.rect.bottom = self.screen_rect.bottom
        self.y = self.rect.y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
