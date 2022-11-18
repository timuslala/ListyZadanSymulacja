from enum import Enum
from time import time
import math

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