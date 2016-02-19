__author__ = 'allan'

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

        for i,j in zip(columns,header):
            if(j == "num"):
                self.num_columns.append(float(i));
            elif(j == "str"):
                self.str_columns.append(i);
            elif(j == "class"):
                self.instance_class = i;

    def normalize(self,min,max):
        for i,j,k in zip(min,max,self.num_columns):
            k = (k-i)/(j-i)








class Instances(object):
    data_set = []
    header = []
    minimum = []
    maximum = []

    def __init__(self,file):
        self.data_set = []
        self.header = []
        self.minimum = []
        self.maximum = []

        file = open(file,'rb')
        files=list(csv.reader(file,delimiter=','))
        #print files
        self.header=files.pop(0);

        for a in range(0,len(files)):
            self.data_set.append(Instance(files[a],self.header));

        self.maximum = copy.copy(self.data_set[0].num_columns);
        self.minimum = copy.copy(self.data_set[0].num_columns);

        self.find_min_max()
        #self.normalize_dataset()

    def normalize_dataset(self):
        for inst in self.data_set:
            inst.normalize(self.minimum,self.maximum)

    def find_min_max(self):
        for i in self.data_set:
            print len(i.num_columns)
            for j in range(len(i.num_columns)):
                self.minimum[j] = min([self.minimum[j],i.num_columns[j]])
                self.maximum[j] = max([self.maximum[j],i.num_columns[j]])

teste = Instances('entrada.txt');
#print teste.data_set
#print teste.header
print teste.data_set[1]
#print teste.data_set[2]
print teste.maximum
print teste.minimum

