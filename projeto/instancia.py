__author__ = 'eduardo'

import csv
import copy

class Instance(object):
    num_columns = []
    str_columns = []
    instance_class = ""

    def __str__(self):
        return "%s %s %s"%(self.num_columns,self.str_columns,self.instance_class)

    def __init__(self,columns,header):
        self.num_columns = []
        self.str_columns = []
        self.instance_class = ""
        self.grupo=0
        self.qtd=0

        for i,j in zip(columns,header):
            if(j == "num"):
                self.num_columns.append(float(i));
            elif(j == "str"):
                self.str_columns.append(i);
            elif(j == "class"):
                self.instance_class = i;
    def reset_attrs(self):
        for i,eInt in enumerate(self.num_columns):

            self.num_columns[i]=0.0


    def normalize(self,min,max):
        for i in range(len(min)):
            self.num_columns[i] = (self.num_columns[i]-min[i])/(max[i]-min[i])


class Instances(object):
    data_set = []
    header = []
    minimum = []
    maximum = []

    def __init__(self,file):
        #Inicializa os atributos
        self.data_set = []
        self.header = []
        self.minimum = []
        self.maximum = []

        #Abre o arquivo
        file = open(file,'rb')
        files=list(csv.reader(file,delimiter=','))

        self.header=files[0]

        #Alimenta o dataset
        for a in range(1,len(files)):

            self.data_set.append(Instance(files[a],self.header))

        #Normaliza o dataset
        self.normalize_dataset()


    def normalize_dataset(self):
        self.maximum = copy.copy(self.data_set[0].num_columns)
        self.minimum = copy.copy(self.data_set[0].num_columns)
        self.find_min_max()

        for inst in self.data_set:
            inst.normalize(self.minimum,self.maximum)

    def find_min_max(self):
        for i in self.data_set:
            for j in range(len(i.num_columns)):
                self.minimum[j] = min([self.minimum[j],i.num_columns[j]])
                self.maximum[j] = max([self.maximum[j],i.num_columns[j]])
