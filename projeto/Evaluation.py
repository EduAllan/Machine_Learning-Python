from projeto.distance_algorithms import calcEuclidianDistance


class Evaluation(object):

    def __init__(self,agrupador,instancias):
        self.agrupador=agrupador
        self.instancias=instancias
        self.distanciaMedia=[]
        self.calcDistance=agrupador.calcDistance

    def multipleRuns(self,qtd):
        resultado=[]
        for i in range(qtd):
            self.agrupador.agrupar()
            for i,elemento in enumerate(self.agrupador.centroides):

                try:
                    resultado[i].append(elemento.qtd)
                except:
                    resultado.append([])
                    resultado[i].append(elemento.qtd)
        return resultado

    def indiceDaviesBouldin(self,a,b):
        centroides=self.agrupador.centroides

        grupo1=centroides[a].distanciaMedia
        grupo2=centroides[b].distanciaMedia
        distancia=self.calcDistance(centroides[a],centroides[b])

        try:
            return ((grupo1+grupo2)/distancia)
        except:
            return 0
    def maxDaviesBouldin(self,analise):
        centroides=self.agrupador.centroides
        maxSimilar=0
        grupo=-1
        for i,particao in enumerate(centroides):
            if i!= analise:
                dist=self.indiceDaviesBouldin(analise,i)
                if dist> maxSimilar:
                    maxSimilar=dist
                    grupo=i
        return maxSimilar

    def BestPartition(self):
        k=self.agrupador.k
        maximo=0
        for i in range(k):
            maximo+=self.maxDaviesBouldin(i)

        return maximo/k