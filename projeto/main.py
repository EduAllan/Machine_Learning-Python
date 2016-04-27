from numpy.core.fromnumeric import mean
from numpy.lib.function_base import median
from projeto.Evaluation import Evaluation
from projeto.instancia import Instances

from projeto.kmeans import KMeans

instancias = Instances('fertility_Diagnosisnormalized.csv')

kmeans=KMeans(instancias,2)
kmeans.setDistanceFunction(valor="2")
evaluation = Evaluation(kmeans,instancias)
resultado= evaluation.multipleRuns(30)
print median(resultado[0]),median(resultado[1])
print resultado
# for g1,g2 in zip(resultado[0],resultado[1]):
#     print "Grupo 1: %s  - Grupo 2: %s"%(g2,g1)

evaluation.maxDaviesBouldin(1)
print evaluation.BestPartition()