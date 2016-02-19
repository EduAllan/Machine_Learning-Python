__author__ = 'allan'

class Instance(object):
    num_columns = []
    str_columns = []
    instance_class = ""

    def __init__(self,line,header):
        columns = str.split()
        for i,j in zip(line,header):
            if(j == "num"):
                self.num_columns.append(i);
            if(j == "str"):
                self.str_columns.append(i);
            if(j == "class"):
                self.instance_class = i;

    def normalize(self,min,max):
        for i,j,k in zip(min,max,self.num_columns):
            k = (k-i)/(j-i)





print teste()