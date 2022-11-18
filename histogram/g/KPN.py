from base import RandomNum
import matplotlib.pyplot as plt
from enum import Enum
import math
from time import time
from scipy.stats import chisquare
class KPN_MOVES(Enum):
    KAMIEN = 0
    PAPIER = 1
    NOZYCE = 2

class Player():
    def __init__(self, name, moves: Enum, seed=round(time())):
        self.name = name
        self.random_num = RandomNum(seed=seed)
        self.moves = moves
        self.generate_move()

    def generate_move(self):
        self.random_num.gen_next()
        self.move = self.moves(math.floor(self.random_num.uniform_x*3))
    
    def __str__(self):
        return self.name

class KPN():
    def __init__(self, p1: Player, p2: Player):
        self.possible_moves = KPN_MOVES
        self.player_1 = p1
        self.player_2 = p2
        self.winner = None
        self.win_statistics = {"wins": 0, "loses": 0, "draws": 0}

    def check_winner(self):
        if self.player_1.move == self.player_2.move:
            self.winner = None
        elif self.player_1.move == KPN_MOVES.KAMIEN:
            if self.player_2.move == KPN_MOVES.PAPIER:
                self.winner = self.player_2
            else:
                self.winner = self.player_1
        elif self.player_1.move == KPN_MOVES.PAPIER:
            if self.player_2.move == KPN_MOVES.NOZYCE:
                self.winner = self.player_2
            else: 
                self.winner = self.player_1
        elif self.player_1.move == KPN_MOVES.NOZYCE:
            if self.player_2.move == KPN_MOVES.KAMIEN:
                self.winner = self.player_2
            else: 
                self.winner = self.player_1
        if self.winner == None:
            self.win_statistics["draws"] += 1
        elif self.winner == self.player_1:
            self.win_statistics["wins"] += 1
        else: 
            self.win_statistics["loses"] += 1
        return self.winner
    
    def generate_moves(self):
        self.player_1.generate_move()
        self.player_2.generate_move()

    def play(self, num_of_games):
        for i in range(num_of_games):
            self.generate_moves()
            self.check_winner()
        return self.win_statistics

kpn = KPN(Player("bot1", KPN_MOVES, 8), Player("bot2", KPN_MOVES, 5))

statistics = kpn.play(100)

plt.bar(statistics.keys(), statistics.values(), align='center')
plt.show()

chisq, p = chisquare([*statistics.values()], [100/3, 100/3, 100/3])
print(p)