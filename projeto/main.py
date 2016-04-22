from numpy.core.fromnumeric import mean
from numpy.lib.function_base import median
from projeto.Evaluation import Evaluation
from projeto.instancia import Instances

from projeto.kmeans import KMeans

instancias = Instances('fertility_Diagnosisnormalized.csv')

kmeans=KMeans(instancias,5)
kmeans.setDistanceFunction(valor="3")
evaluation = Evaluation(kmeans,instancias)
resultado= evaluation.multipleRuns(1)

# for g1,g2 in zip(resultado[0],resultado[1]):
#     print "Grupo 1: %s  - Grupo 2: %s"%(g2,g1)

print evaluation.indiceDaviesBouldin(0,1)
evaluation.maxDaviesBouldin(0)