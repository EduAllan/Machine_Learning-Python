from math import sqrt, pow
import numpy as np
import csv
from projeto.distance_algorithms import EuclidianDistance

__author__ = 'allan'

class KNN(object):
    K = 0

    def __init__(self,instances,k):
        self.instances = instances
        self.K = k
        self.distance_algorithm = EuclidianDistance(self.instances)

