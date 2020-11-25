from loadData import LoadData

class Vertex:

    def __init__(self):
        self.objloadata = LoadData()


    def recorrerDictionary(self):
        self.objloadata.upLoadData()
        listaAdyancen = self.objloadata.getBasesConexiones()
        print(type(listaAdyancen))
        llaves = listaAdyancen.keys()
        print(llaves)


verti = Vertex()
verti.recorrerDictionary()