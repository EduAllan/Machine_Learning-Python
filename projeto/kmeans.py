from cmath import sqrt
from numpy.lib.function_base import median,mean
import random
from projeto import Evaluation
from projeto.distance_algorithms import calcEuclidianDistance, calcManhattanDistance, calcChebychevDistance
from projeto.instancia import *

__author__ = 'allan'

class KMeans(object):
    def __init__(self,instances,k):
        self.instances=instances
        self.k=k
        self.centroides=[]
        self.calcDistance=calcEuclidianDistance

    def agrupar(self):
        self.sortPoints()
        self.defineGrupos()
        # i=0
        while(True):
            tempCentroid=copy.deepcopy(self.centroides)
            self.recalculaCentroides()
            self.defineGrupos()
            parada=0

            for ctemp,cent in zip(tempCentroid,self.centroides):

                if (self.calcDistance(ctemp,cent) == 0.0):
                    parada+=1

            if parada == len(tempCentroid):
                break

            # print self.calcEuclidianDistance(tempCentroid[0],self.centroides[0])



            # i+=1
            # if i==10:
            #
            #     break



    def recalculaCentroides(self):
        tempCentroid=copy.deepcopy(self.centroides)

        #reseta os atributos das instancias
        for tempElement in tempCentroid:
            tempElement.reset_attrs()
        #Soma em cada grupo a quantidade total pra depois tirar a media e escolher o centroide
        for instance in self.instances.data_set:
            for i,col in enumerate(instance.num_columns):
                tempCentroid[instance.grupo].num_columns[i]+=col

        for instance in tempCentroid:
            if instance.qtd==0: break
            for i,col in enumerate(instance.num_columns):

                instance.num_columns[i]/=instance.qtd


            instance.qtd=0



        self.centroides=tempCentroid


    def defineGrupos(self):
        # print self.centroides[1]

        #reseta a distancia media do centroide, ja que o grupo ira mudar
        for clean in self.centroides:
            clean.distanciaMedia=0

        for instance in self.instances.data_set:
            pertenceGrupo=0

            menorDistancia=self.calcDistance(self.centroides[0],instance)
            tempGrupo=0
            for grupo in range(1,self.k):
                temp=self.calcDistance(self.centroides[grupo],instance)

                if temp < menorDistancia:
                    menorDistancia=temp
                    tempGrupo=grupo

            instance.grupo=tempGrupo
            centroide=self.centroides[tempGrupo]
            centroide.qtd+=1
            centroide.distanciaMedia+=menorDistancia

        #Realiza a media da distancia do grupo para cada centroide
        for cent in self.centroides:
            try:
                cent.distanciaMedia/=cent.qtd
            except:
                cent.distanciaMedia=0
        # for i in range(self.k):
        #     print self.centroides[i].qtd
        #
        # print ""



    def sortPoints(self):
        del self.centroides[:]
        lista = range(0,len(self.instances.data_set))
        for ponto in range(self.k):
            indice=random.choice(lista)
            tempCentroid=copy.deepcopy(self.instances.data_set[indice])

            tempCentroid.qtd=0
            tempCentroid.grupo=ponto
            self.centroides.append(tempCentroid)




    def qtdGrupos(self):
        for i in range(self.k):
            print "grupo: %s , quantidade: %s"%(i+1,self.centroides[i].qtd)

    def qtdPorGrupo(self):
        lista=[]
        for a in self.centroides:
            lista.append(a.qtd)
        return lista

    def setDistanceFunction(self,funcao=None,valor=None):
        if funcao:
            self.calcDistance=funcao
        elif valor:
            if valor == "1":
                self.calcDistance=calcEuclidianDistance
            elif valor == "2":

                self.calcDistance = calcManhattanDistance
            elif valor == "3":

                self.calcDistance = calcChebychevDistance

        else:
            print 'oi'
            self.calcDistance=calcEuclidianDistance



# for i in range(100):
# 
# 
#     kmeans.agrupar()
# 
# 
# 
# 
#     for i,elemento in enumerate(kmeans.centroides):
#         resultado[i].append(elemento.qtd)
# 
# print median(resultado[0])
# print median(resultado[1])
# 
# print median(resultado[0])
# print median(resultado[1])
