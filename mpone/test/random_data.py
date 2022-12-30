import numpy as np
import pandas as pd
import time

class Data:
    __value = None
    __length = None
    __seed = None

    value = None

    def __init__(self, length=None, seed=None):
        self.__length = length
        self.__seed = seed

        if self.__seed is not None:
            np.random.seed(self.__seed)

        if self.__length is None:
            self.__value = np.random.random()
        else:
            self.__value = np.random.random(self.__length)

        self.update_value()

    def set_seed(self, seed):
        self.__seed = seed
        np.random.seed(seed)

    def get_seed(self):
        return self.__seed

    def get_length(self):
        return self.__length

    def value(self):
        return self.value

    def update_value(self):
        self.value = self.__value

    def regen(self, length=None, seed=None):
        self.__length = length
        self.__seed = seed

        if self.__seed is not None:
            np.random.seed(self.__seed)

        if self.__length is None:
            self.__value = np.random.random()
        else:
            self.__value = np.random.random(self.__length)

        self.update_value()

    def step(self, up=False):
        if up:
            self.__value = np.append(self.__value, ((time.time()/167240334)%10)*10e8%500+np.random.random()+1)
        else:
            self.__value = np.append(self.__value, np.random.random())
        self.__length = len(self.__value)

        self.update_value()
