from numpy.core.fromnumeric import mean
from numpy.lib.function_base import median
from projeto.Evaluation import Evaluation
from projeto.instancia import Instances

from projeto.kmeans import KMeans

instancias = Instances('fertility_Diagnosisnormalized.csv')

kmeans=KMeans(instancias,2)
kmeans.setDistanceFunction(valor="3")
evaluation = Evaluation(kmeans,instancias)
for grupo in evaluation.multipleRuns(30):
    print grupo
