import networkx as nx
import matplotlib.pyplot as plt
from loadData import LoadData
class Grafo:

    def __init__(self, nodo, aristas):
        self.vertices  = nodo
        self.aristas = aristas
        self.grafo = nx.Graph()#Grafo no dirigido 
        #self.gradoD = nx.DiGraph()
        self.gradoD = nx.MultiDiGraph()
        self.objLoadData = LoadData()


    def existeNodo(self, nodo):
        if nodo in self.vertices:
            return True
        return False

    def getGrafo(self):
        return self.gradoD

    def addVertex(self, nodo):
        pass

    def addArista(self):
        for base in self.aristas:
            aux = self.aristas.get(base)
            print(base)
            consultaColum = self.objLoadData.uniqueColumn(' airport_arr ', aux)
            for destino in consultaColum:
                self.gradoD.add_edge(base,destino)
                print(base,destino)

        print (len((self.gradoD.edges)))
        print(self.gradoD.edges)

    def addNode(self):
        nodoBases = [' BASE1 ', ' BASE2 ', 'BASE3 ']
        for nodo in self.vertices:
            if nodo in nodoBases:
                self.gradoD.add_node(nodo)

    def drawGraph(self):
        self.gradoD.add_nodes_from(self.vertices)
        self.addArista()
        pos = nx.spring_layout(self.gradoD)
        plt.figure()
        nx.draw(self.gradoD, pos, edge_color = 'black', width = 1, linewidths =2,
                node_size= 1500 , node_color = 'purple', alpha= 0.7,ax=None)

        nx.draw_networkx_labels(self.gradoD,pos,
                                labels= {node: node for node in self.gradoD.nodes()},
                                font_size=9, alpha=1, horizontalalignment='center',verticalalignment='center'
                                ,ax=None)
        plt.show()



objload = LoadData()
objload.upLoadData()
print(objload.getBasesConexiones())
objgrafo = Grafo(objload.getDataAirport(),objload.getBasesConexiones())
objgrafo.drawGraph()



