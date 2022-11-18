from enum import Enum
from time import time
import math
from scipy.stats import chisquare
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import numpy as np
class RandomNum():
    def __init__(self, a=75, c=74, m=math.pow(2, 16) + 1, seed=round(time())):
        self.a = a
        self.c = c
        self.m = m
        self.x = (seed * a + c) % m
        self.uniform_x = self.x / m
    
    def gen_next(self):
        self.x = (self.x * self.a + self.c) % self.m
        self.uniform_x = self.x / self.m
        return self.uniform_x

    def __call__(self):
        return self.gen_next()

class DicePlayer():
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
    def __init__(self, p1: DicePlayer, p2: DicePlayer):
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

class ArcherPlayer1():
    def __init__(self, seed=round(time())):
        self.random_num = RandomNum(seed=seed)
        self.distance_from_center: float
        self.points = 0
        self.center_scores = 0
        self.generate_move()

    def generate_move(self):
        degree = math.ceil(self.random_num() * 360)
        power = math.ceil(self.random_num() * 1000)
        self.distance_from_center = power
        return self.distance_from_center

class ArcherPlayer2():
    def __init__(self, seed=round(time())):
        self.random_num = RandomNum(seed=seed)
        self.distance_from_center: float
        self.points = 0
        self.center_scores = 0 
        self.generate_move()

    def generate_move(self):
        dis1 = math.ceil(self.random_num() * 900)
        dis2 = math.ceil(self.random_num() * 900)
        self.distance_from_center = (dis1**2 + dis2**2)**(1/2)
        return self.distance_from_center

class ArcherGame():
    def __init__(self, p1: ArcherPlayer1, p2: ArcherPlayer2):
        self.player_1 = p1
        self.player_2 = p2
        self.winner = None
        self.win_statistics = {"wins": 0, "loses": 0, "draws": 0}
        self.player_1_scores = []
        self.player_2_scores = []
    def check_winner(self, num_of_games):
        for j in range(num_of_games):
            for i in range(10):
                for player in [self.player_1, self.player_2]:
                    player.generate_move()
                    if player.distance_from_center <= 61:
                        player.points += 10
                        player.center_scores += 1
                    elif player.distance_from_center <= 122:
                        player.points += 10
                    elif player.distance_from_center <= 244:
                        player.points += 9
                    elif player.distance_from_center <= 366:
                        player.points += 8
                    elif player.distance_from_center <= 488:
                        player.points += 7
                    elif player.distance_from_center <= 610:
                        player.points += 6
                    elif player.distance_from_center <= 732:
                        player.points += 5
                    elif player.distance_from_center <= 854:
                        player.points += 4
                    elif player.distance_from_center <= 976:
                        player.points += 3
                    elif player.distance_from_center <= 1098:
                        player.points += 2
                    elif player.distance_from_center <= 1220:
                        player.points += 1
            
            self.player_1_scores.append(self.player_1.points)
            self.player_2_scores.append(self.player_2.points)
            if self.player_1.points == self.player_2.points:
                if self.player_1.center_scores == self.player_2.center_scores:
                    self.win_statistics["draws"] += 1
                elif self.player_1.center_scores > self.player_2.center_scores:
                    self.win_statistics["wins"] += 1
                else:
                    self.win_statistics["loses"] += 1
            elif self.player_1.points > self.player_2.points:
                self.win_statistics["wins"] += 1
            else:
                self.win_statistics["loses"] += 1
            self.player_1.points = 0
            self.player_2.points = 0
        return self.win_statistics

def zad2():
    dataset = []
    exp = []
    exp.append(33.333333333333333333333333)
    exp.append(33.333333333333333333333333)
    exp.append(33.333333333333333333333333)
    dataset.append(34)
    dataset.append(34)
    dataset.append(32)
    
    dist, pvalue = chisquare(dataset,exp)
    uni = 'YES' if pvalue > 0.05 else 'NO'
    print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8}")
    print("koniec zad 2")

def zad3():
    dice_game = DiceGame(DicePlayer(seed=1), DicePlayer())

    win_statistics, advantage_statistics = dice_game.play(30)

    fig, axs = plt.subplots(2, figsize=(10,10), dpi=80)

    fig.suptitle(f'gra w kości')

    axs[0].bar(win_statistics.keys(), win_statistics.values(), align='center')
    axs[0].set_title('wyniki pierwszego gracza')
    axs[1].bar(advantage_statistics.keys(), advantage_statistics.values(), align='center')
    axs[1].set_xticks(np.arange(-12, 12))
    axs[1].set_title('przewagi punktowe pierwszego gracza')

    plt.show()

def zad4():
    p1 = ArcherPlayer1()
    p2 = ArcherPlayer2()
    game = ArcherGame(p1,p2)
    game.check_winner(20)
    testobj = ttest_ind(game.player_1_scores,game.player_2_scores)
    print(testobj)

if __name__ == "__main__":
    #zad2()
    #zad3()
    #zad4()
    zadofftop()