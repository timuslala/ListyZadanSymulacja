from cmath import e
import math
from time import time
from base import RandomNum
import matplotlib.pyplot as plt
import numpy as np
class Player1():
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

p1 = Player1()

class Player2():
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

p2 = Player2()
class ArcherGame():
    def __init__(self, p1: Player1, p2: Player2):
        self.player_1 = p1
        self.player_2 = p2
        self.winner = None
        self.win_statistics = {"wins": 0, "loses": 0, "draws": 0}

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



