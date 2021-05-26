#
# 设置参数记录
#
class Settings:
    """存储此项目中所有的配置数据"""

    def __init__(self):
        """初始化设置"""

        # 窗口显示所须参数
        self.screen_width = 1200  # 窗口宽像素
        self.screen_height = 800  # 窗口高像素
        self.bg_color = (230, 230, 230)  # 背景色
        self.full_screen = False  # 是否全屏

        # 飞船所须参数
        self.ship_speed = 1.5  # 飞船每次移动的像素

        # 子弹设置
        self.bullet_speed = 1.0  # 子弹速度
        self.bullet_width = 3  # 子弹宽
        self.bullet_hight = 15  # 子弹高
        self.bullet_color = (60, 60, 60)  # 子弹颜色
        self.bullets_allowed = 5  # 同时生成的子弹最大数量

        # 外星人设置
        self.alien_x_speen = 1.0  # 外星人移动速度
        self.alien_y_speen = 10.0  # 外星人移动速度
        self.alien_left_rows = 1  # 保留多少行空白
        self.alien_change_direct_step = 10  # 移动10步后换方向
        self.alien_move_direct = 1  # 外星人移动方向 1向右-1向左
