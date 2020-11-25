import pandas as  pd
import os

RUTA_DATASET = 'dataset/'

def sizeDirectory():
    contenido = os.listdir(RUTA_DATASET)
    #contenido.sort()
    print(contenido)
    return contenido


"""print(File.sheet_names)
data_frame = File.parse('day_1')
print(data_frame)"""


def imprimir(data):
    const = len(data)
    print(const)
    for dt in data:
        print(dt)


def distintData(data):
    data2 = pd.DataFrame()
    data2 = data
    data2.duplicated()
    data2 = data2.drop_duplicates()
    #data2.tolist()
    sorted(data2)
    imprimir(data2)


def uniqueDataList(dataFrm, listaA):
    listaAir1 = []
    listaAir1 = listaA
    #print(listaAir1)
    dataAux = pd.DataFrame()
    
    """for aero in listaA:
        dataAux = dataFrm[dataFrm[' airport_dep '] == aero]"""
    
    #print(dataAux)



def uploadData():
    contenido = sizeDirectory()
    data_Frame = pd.DataFrame()
    data_Aer = pd.DataFrame()
    data_Aer2 = pd.DataFrame()
    datalis = []

    for data in contenido :
        dataAux = pd.read_csv(RUTA_DATASET + data, keep_default_na=False)
        data_Frame = pd.concat([data_Frame,dataAux])


    data_Aer = data_Frame[' airport_dep ']
    data_Aer2 = data_Frame[' airport_dep '] == ' AIR4 '
    database = pd.DataFrame()
    database = data_Frame[data_Aer2]
    database.head()
    distintData(data_Aer)
    uniqueDataList(data_Frame,data_Aer)
    print(database)

    #uniqueDataList(data_Frame,distintData(data_Aer))
    return data_Frame


print(uploadData())



