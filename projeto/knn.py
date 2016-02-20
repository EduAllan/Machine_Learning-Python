from math import sqrt, pow
import numpy as np
import csv
from projeto.distance_algorithms import EuclidianDistance
from projeto.instancia import Instances
from projeto.instancia import Instance

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


        return max(list,key=list.count)


teste = Instances('entrada.txt')
classifier = KNN(teste,3)
input = Instance([6.5,3.0,5.2,2.0],["num","num","num","num"])
print classifier.classify(input)