#
# 主应用程序
#
import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


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

        # 屏幕上的元素
        self.ship = Ship(self)  # 飞船
        self.bullets = pygame.sprite.Group()  # 子弹

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_bullets(self):
        """更新子弹信息"""
        # 子弹实时更新
        self.bullets.update()
        # 销毁屏幕外的子弹
        self._destory_bullet()

    def _fire_bullet(self):
        """发射子弹 在允许最大子弹数的范围内创建"""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    def _destory_bullet(self):
        """消除屏幕外的子弹"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # print(len(self.bullets))

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
        # 画出所有子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        """
        开始游戏主循环
        """
        while True:
            # 键盘输入反馈
            self._check_events()
            # 飞船实时更新
            self.ship.update()
            # 子弹处理
            self._update_bullets()
            # 屏幕显示
            self._update_screen()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
