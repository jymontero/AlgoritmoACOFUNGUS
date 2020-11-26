from loadData import LoadData
import pandas as pd

class Vertex:

    def __init__(self):
        self.objloadata = LoadData()

    def recorrerDataFrame(self, dataF):

        for indiceF, fila in  dataF.iterrows():
            print(fila)

    def recorrerDictionary(self, clave):
        self.objloadata.upLoadData()
        listaAdyancen = self.objloadata.getBasesConexiones()
        print(listaAdyancen.keys())
        aux = pd.DataFrame()
        if clave in listaAdyancen:
            aux = listaAdyancen.get(clave)
            print(type(aux))
            self.recorrerDataFrame(aux)
            print('*******')
        else:
            print('Base o aeropuerto no existe')


verti = Vertex()
cadena = ' AIR14    '
cadenaclear = cadena.strip()
print(cadenaclear)
verti.recorrerDictionary(cadenaclear)