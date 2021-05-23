#
# 主应用程序
#
import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化"""
        pygame.init()  # 初始化背景设置

        self.settings = Settings()  # 设置加载

        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width,
                                                   self.settings.screen_height))  # 创建一个显示窗口 参数是个元组，表示宽1200像素，高800像素 给到screen的是个Surface，是游戏元素
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def _check_keyup_event(self, event):
        """键盘弹起事件 将移动标志都置为false，不再移动"""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False
        elif event.key == pygame.K_UP:
            self.ship.move_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False

    def _check_keydown_event(self, event):
        """
        键盘按下事件 将移动标志都置为true，更新坐标
        按Q时退出游戏
        """
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_UP:
            self.ship.move_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_events(self):
        """监视键盘和鼠标事件"""
        for event in pygame.event.get():
            # print(event.type)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _update_screen(self):
        """每次循环都重缓屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # 画船

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
