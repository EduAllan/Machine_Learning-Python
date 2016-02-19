__author__ = 'allan'


#Super classe que deve ser utilizada para modelar algum tipo de distancia
class Distance(object):



    #toda classe que herdar de Distance deve implementar uma funcao que receba exatamente esses atributos e retornar uma lista de instancias
    def search_distance(self,instances_real_set,instances_string_set,instance):



        pass



class EuclidianDistance(Distance):

    def search_distance(self,instances_real_set,instances_string_set,instance):
        lista=[]

        for i,instancia in enumerate(instances_real_set):
            resultado=self.distanciaEuclidiana(instancia,instances_string_set[i],instance)
            lista.append([self.matrizClass[i],resultado])

        return lista





