import math
from time import time
from base import RandomNum
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chisquare

class Player():
    def __init__(self, seed=round(time())):
        self.random_num = RandomNum(seed=seed)
        self.move1 = None
        self.move2 = None
        self.generate_move()

    def generate_move(self):
        self.random_num.gen_next()
        self.move1 = math.ceil(self.random_num.uniform_x*6)
        self.random_num.gen_next()
        self.move2 = math.ceil(self.random_num.uniform_x*6)
        self.total_points = self.move1 + self.move2
        return self.total_points
    
    def __str__(self):
        return self.name

class DiceGame():
    def __init__(self, p1: Player, p2: Player):
        self.player_1 = p1
        self.player_2 = p2
        self.win_statistics = {"wins": 0, "loses": 0, "draws": 0}
        self.advantage_statistics = {}


    def check_winner(self):
        if self.player_1.total_points == self.player_2.total_points:
            self.win_statistics["draws"] += 1
        elif self.player_1.total_points > self.player_2.total_points:
            self.win_statistics["wins"] += 1
        else:
            self.win_statistics["loses"] += 1
        advantage = self.player_1.total_points - self.player_2.total_points
        if self.advantage_statistics.get(advantage):
            self.advantage_statistics[advantage] += 1
        else:
            self.advantage_statistics[advantage] = 1
    def generate_moves(self):
        self.player_1.generate_move()
        self.player_2.generate_move()

    def play(self, num_of_games):
        for i in range(num_of_games):
            self.generate_moves()
            self.check_winner()
        return self.win_statistics, self.advantage_statistics

dice_game = DiceGame(Player(seed=5), Player())

win_statistics, advantage_statistics = dice_game.play(300)

fig, axs = plt.subplots(2, figsize=(10,10), dpi=80)

fig.suptitle(f'DICE GAME STATISTICS games generated: {30}')

axs[0].bar(win_statistics.keys(), win_statistics.values(), align='center')
axs[0].set_title('first player results')
axs[1].bar(advantage_statistics.keys(), advantage_statistics.values(), align='center')
axs[1].set_xticks(np.arange(-12, 12))
axs[1].set_title('first player advantage statistics')

plt.show()