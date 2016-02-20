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
        print distances
        list = []

        for i in range(self.K):
            list.append(distances[i][0])



        return max(list,key=list.count)


teste = Instances('entrada.txt')
classifier = KNN(teste,3)
input = Instance([7.0,3.2,4.7,1.4],["num","num","num","num"])
input.normalize(teste.minimum,teste.maximum)
print classifier.classify(input)