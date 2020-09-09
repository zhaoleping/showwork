class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #游戏刚启动时处于非活动状态
        self.game_active = False

        # 在任何情况下都不应该重置最高分
        self.get_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能的变化信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def get_high_score(self):
        with open('high_score.txt') as highscore:
            lines = highscore.readlines()
            if lines:
                self.high_score = int(lines[0])
            else:
                self.high_score = 0