from copy import copy
from math import sqrt

__author__ = 'allan'


#Super classe que deve ser utilizada para modelar algum tipo de distancia
class Distance(object):
    def __init__(self,instances):
        self.instances=instances



    #toda classe que herdar de Distance deve implementar uma funcao que receba exatamente esses atributos e retornar uma lista de instancias
    def search_distance(self,entrada):



        pass



class EuclidianDistance(Distance):

    def __init__(self,instances):

        self.distanceSTR=HammingDistance()
        super(Distance, self).__init__()

        print self.instances

    def search_distance(self,entrada):
        lista=[]

        for i,instance in enumerate(self.instances):
            resultado=self.distanciaEuclidiana(instance,entrada)
            lista.append([instance,resultado])
        lista.sort(key = lambda c: c[1])
        return lista




    def distanciaEuclidiana(self,instance,entrada):
            resultado=0

            for elemento1,elemento2 in zip(instance.num_columns,entrada.num_columns):
                resultado+= pow(elemento1-elemento2,2)
            for elemento1,elemento2 in zip(instance.str_columns,entrada.str_columns):
                resultado+=pow(self.distanceSTR.distance(elemento1,elemento2),2)

            return sqrt(resultado)



class HammingDistance(object):


    def distance(self,elemento1,elemento2):
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


h=HammingDistance()

