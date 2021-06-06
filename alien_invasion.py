#
# 主应用程序
#
import pygame
import game_function
from settings import Settings
from ship import Ship
from button import Button
from gameStatus import GameStatus


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化"""
        pygame.init()  # 初始化背景设置

        self.settings = Settings()  # 设置加载

        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width,
                                                   self.settings.screen_height))  # 创建一个显示窗口 参数是个元组，表示宽1200像素，高800像素 给到screen的是个Surface，是游戏元素
        pygame.display.set_caption("Alien Invasion")

        # 屏幕上的元素
        self.ship = Ship(self)  # 飞船
        self.bullets = pygame.sprite.Group()  # 子弹
        self.aliens = pygame.sprite.Group()  # 外星人
        self.play_button = Button(self, "Play")

        # 游戏状态控制
        self.gameStatus = GameStatus(self)

        # 创建外星人
        game_function.create_fleet(self)

    def run_game(self):
        """
        开始游戏主循环
        """
        while True:
            # 键盘输入反馈
            game_function.check_events(self)

            if self.gameStatus.is_alive():
                # 飞船实时更新
                self.ship.update()
                # 子弹处理
                game_function.update_bullets(self)
                # 外星人处理
                game_function.update_aliens(self)
            # 屏幕显示
            game_function.update_screen(self)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
