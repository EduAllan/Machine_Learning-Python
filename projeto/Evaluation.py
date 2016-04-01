

class Evaluation(object):

    def __init__(self,agrupador,instancias):
        self.agrupador=agrupador
        self.instancias=instancias

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



