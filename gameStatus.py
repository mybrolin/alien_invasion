import shelve
import traceback

import log


class GameStatus:
    """游戏状态"""

    def __init__(self, al_game):
        """初始化"""
        self.activity = False

        self.initial_ship_life = al_game.settings.ship_life
        self.alien_score_for_one = al_game.settings.alien_score_for_one

        # self.ship_left = self.initial_ship_life
        # self.current_score = 0
        self.max_score = 0
        self.load_max_score()

        self.initial_status()

    def active(self):
        """激活"""
        self.activity = True

    def shut_down(self):
        """结束"""
        self.activity = False

    def is_alive(self):
        """状态是否存活"""
        return self.activity

    def initial_status(self):
        """重置"""
        self.ship_left = self.initial_ship_life

        self.current_score = 0
        # self.max_score = 0

    def save_max_score(self):
        """保存最高记录"""
        maxScoreHistory = shelve.open("maxScoreHistory")
        maxScoreHistory["maxScore"] = self.max_score
        maxScoreHistory.close()

    def load_max_score(self):
        """加载最高记录"""
        maxScoreHistory = shelve.open("maxScoreHistory")
        try:
            temp_max_score = maxScoreHistory["maxScore"]
            if temp_max_score:
                self.max_score = temp_max_score
        except Exception as ex:
            log.error(traceback.extract_stack())
            maxScoreHistory["maxScore"] = 0

        maxScoreHistory.close()

    def ship_minus(self):
        """飞船生命减一"""
        self.ship_left -= 1
        if self.ship_left == 0:
            self.shut_down()

    def hit_aliens(self, alien_count):
        """打中外星人"""
        self.current_score += alien_count * self.alien_score_for_one
        if self.current_score > self.max_score:
            self.max_score = self.current_score
