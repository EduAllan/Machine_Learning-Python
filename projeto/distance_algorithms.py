
from math import sqrt

__author__ = 'allan'


#Super classe que deve ser utilizada para modelar algum tipo de distancia
class Distance(object):


    #toda classe que herdar de Distance deve implementar uma funcao que receba exatamente esses atributos e retornar uma lista de instancias
    def search_distance(self,instances,input):
        pass



class EuclidianDistance(Distance):

    def __init__(self):

        self.distanceSTR=HammingDistance()




    def search_distance(self,instances,input):
        lista=[]

        for i,instance in enumerate(instances):
            result=self.calcEuclidianDistance(instance,input)
            lista.append([instance.instance_class,result])
        lista.sort(key = lambda c: c[1])
        return lista




    def calcEuclidianDistance(self,instance,input):
            result=0

            for element1,element2 in zip(instance.num_columns,input.num_columns):
                result+= pow(element1-element2,2)
            for element1,element2 in zip(instance.str_columns,input.str_columns):
                result+=pow(self.distanceSTR.distance(element1,element2),2)

            return sqrt(result)



class HammingDistance(object):


    def distance(self,element1,element2):
        tamanho=max(float(len(element1)),float(len(element2)))

        diference=0.0
        for letra1,letra2 in zip(element1,element2):
            if(letra1 != letra2):

                diference+=1


        return (diference+abs(len(element1)-len(element2)))/tamanho





