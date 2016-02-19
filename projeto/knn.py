from math import sqrt, pow
import numpy as np
import csv
from projeto.distance_algorithms import EuclidianDistance

__author__ = 'allan'

class KNN(object):
    matrizNumber=[]
    matrizStr=[]
    matrizClass=[]
    minimo=[]
    maximo=[]
    STR='str'
    NUM='num'
    CLASS='class'
    def __init__(self,arquivo):
        self.matrizNumber=[]
        self.matrizStr=[]
        self.matrizClass=[]
        self.minimo=[]
        self.maximo=[]
        self.cabecalho=""
        self.loadMatrix(arquivo)
        self.min_max()
        self.normalizacao()
        self.distancia=EuclidianDistance(self.instances)

        print self.matrizNumber


    def loadMatrix(self,arquivo):
        arquivo = open(arquivo,'rb')
        reader=list(csv.reader(arquivo,delimiter=','))
        for a in range(len(reader)-1):
            self.matrizNumber.append([])
            self.matrizStr.append([])
            self.matrizClass.append([])

        self.cabecalho=reader.pop(0)




        for j,linha in enumerate(reader):

            for index,elemento in enumerate(linha):

                if(self.cabecalho[index]==KNN.NUM):

                    self.matrizNumber[j].append(float(elemento))

                elif(self.cabecalho[index]==KNN.STR):
                    self.matrizStr[j].append(elemento)
                elif(self.cabecalho[index]==KNN.CLASS):
                    self.matrizClass[j].append(elemento)


    def normalizaEntrada(self,instancia):

        i=0
        for index in range(0,len(instancia)):

            if self.cabecalho[index]==KNN.NUM:
                instancia[index]=self.normaliza(instancia[index],self.minimo[i],self.maximo[i])

                i+=1

        return instancia

    def distanceHamming(self,elemento1,elemento2):
        tamanho=0

        if(len(elemento1)>=len(elemento2)):
            tamanho=float(len(elemento1))
        else:
            tamanho=float(len(elemento2))


        qtd_igual=0.0
        for letra1,letra2 in zip(elemento1,elemento2):
            if(letra1 == letra2):

                qtd_igual+=1


        return (len(elemento1)-qtd_igual+abs(len(elemento1)-len(elemento2)))/tamanho

    def normaliza(self,a,min,max):
       return (a-min)/(max-min)



    def normalizacao(self):
        colunas =len(self.minimo)
        linhas=len(self.matrizNumber)
        for a in range(linhas):
            for b in range(colunas):

                self.matrizNumber[a][b]=self.normaliza(self.matrizNumber[a][b],self.minimo[b],self.maximo[b])





    def distanciaEuclidiana(self,instanciaN,instanciaS,entrada):
        resultado=0
        indexN=0
        indexS=0

        for i,elemento in enumerate(entrada):

            if(self.cabecalho[i]==KNN.NUM):
               temp=(instanciaN[indexN]-elemento)
               indexN+=1

            elif (self.cabecalho[i]==KNN.STR):
                temp=self.distanceHamming(instanciaS[indexS],elemento)
                indexS+=1
            else:
                continue
            resultado+=pow(temp,2)



        return sqrt(resultado)


    def findNeightbours(self,entrada):



    def min_max(self):
        matriz=np.array(self.matrizNumber)

        self.minimo=matriz.min(0).tolist()
        self.maximo=matriz.max(0).tolist()

    def executa(self,instancia):
        instancia=self.normalizaEntrada(instancia=instancia)

        lista = self.distanceSet(instancia)
        lista.sort(key = lambda c: c[1])
        for i,elemento in enumerate(lista):
            print i,elemento



x1=[10,1.35,60,"alto"]
x2=[11,1.65,65,"baixo"]
x3=[12,1.50,55,"medio"]
x4=[15,1.65,60,"medio"]
x5=[9,1.40,50,"medio"]
x6=[5,1.10,40,"alto"]

dataSet=[x1,x2,x3,x4,x5,x6]
# print distanciaEuclidiana(l1,l2)
#
#
# xt=[8,1.25,45,"alto"]
#
#
# matriz=np.array(dataSet)
#
# minimo=matriz.min(0).tolist()
# maximo=matriz.max(0).tolist()
#
# matrizNormal=normalizacao(matriz,minimo,maximo)
# xt=normalizaEntrada(xt,minimo,maximo)
# print xt
# print(distanceSet(matrizNormal,xt))

knn=KNN('entrada.txt')

knn.executa([15,1.75,60])