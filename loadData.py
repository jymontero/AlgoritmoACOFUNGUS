import pandas as pd
import os
from timedate import HoraData

RUTA_DATASET = 'dataset/'

class LoadData:

   def __init__(self):
      self.data_Frame = pd.DataFrame()
      #elf.dataAirport = pd.DataFrame()
      self.dataAirport = []
      self.listaBases = []
      self.dictnary_Base_Aer = {}
      self.horasObj = HoraData()
      self.upLoadData()

   def printed(self, data):
      const = len(data)
      for data3 in data:
         print(data3)

   def uniqueColumn(self,nameColum,data):
      data3 = pd.DataFrame()
      data3 = data[nameColum]
      return data3

#Metod que filtra todas las filas de un datafram
#nameColumn: nombre de la columna por el cual filtrar
#conditional: condicion de filtrado
   def uniqueData(self,nameColum, conditional):
      data3 = pd.DataFrame()
      database = pd.DataFrame()

      data3 = self.data_Frame[nameColum] == conditional
      database = self.data_Frame[data3]
      return database

#Metodo que filtra datos de acuerdo a una columna del dataframe
   def distintData(self, columnNam):
      self.dataAirport = pd.unique(self.data_Frame[columnNam])
      aux = pd.DataFrame()

      for base in self.dataAirport:
         aux = self.uniqueData(columnNam,base)
         self.listaBases.append(aux)

#Metodo que recorre un dataFrame
   def recorrerDataFrame(self, dataF):
         aux = pd.DataFrame()
         for indiceF, fila in  aux.iterrows():
            print(fila)

#Metodo que obtiene el tiempo de vuelo
   def getTimeFly(self, row):
      hora_dep = (row[' hour_dep '])
      hora_arr = (row[' hour_arr'])
      listHora_dep = hora_dep.lstrip().split(sep=':')
      listHora_arr = hora_arr.lstrip().split(sep= ':')
      minuto = self.horasObj.hourDate(listHora_arr,listHora_dep)
      return minuto

#Metodo que agrega una columna con el tiempo de vuelo
   def addTimeFly(self):
      self.data_Frame['time_fly']= self.data_Frame.apply(self.getTimeFly,axis=1)

#Metodo que listael conido de un directorio
   def sizeDirectory(self):
      contenido = os.listdir(RUTA_DATASET)
      return contenido

#Metodo que crear un diccionario Clave:nombre de aeropuerto obase
#valor es el listado de todos los vuelos que parten  de aeropuerto o base
   def crearDiccionario(self):
      self.dictnary_Base_Aer = dict(zip(self.dataAirport,self.listaBases))

#Retorna el datafraeme
   def getDataFrame(self):
      return self.data_Frame

   def getDataAirport(self):
      return self.dataAirport

#retorna listadebases
   def getListaBases(self):
      return self.listaBases

   def getBasesConexiones(self):
      return self.dictnary_Base_Aer

#Descripción = Metodo que carga el dataframe de un directorio
#Parametrros =
   def upLoadData(self):
      contenido = self.sizeDirectory()

      for data in contenido:
            dataRead = pd.read_csv(RUTA_DATASET + data, keep_default_na = True)
            self.data_Frame = pd.concat([self.data_Frame,dataRead])

      self.data_Frame.reindex()
      self.addTimeFly()
      self.distintData(' airport_dep ')
      self.crearDiccionario()
      print('DATASET CARGADO....\n','TIEMPO VUELO OK\n','DICCIONARIO OK')