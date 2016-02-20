from math import sqrt, pow
import numpy as np
import csv
from projeto.distance_algorithms import EuclidianDistance

__author__ = 'allan'

class KNN(object):
    K = 0

    def __init__(self,instances,k=1):
        self.instances = instances
        self.K = k
        self.distance_algorithm = EuclidianDistance()

    def classify(self,input):
        distances = self.distance_algorithm.search_distance(self.instances,input)
        list = []

        for i in range(self.K):
            list.append(distances[i][0])

        return max(list,key=list.count())

