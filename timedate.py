from datetime import datetime, date, time, timezone, timedelta

class HoraData:

    def __init__(self):
        pass

    def restarHora(self,hora1, hora2):
        formato = "%H:%M:%S"
        horaSalida = datetime.strptime(hora2,formato)
        horallegad = datetime.strptime(hora1,formato)
        resultado = horallegad - horaSalida
        seconds = resultado.seconds
        minutos = (seconds/60)
        return minutos

    def horaMinSeparate(self, lista_horas):
        hora = int(lista_horas[0])
        minuto = int(lista_horas[1])
        return hora,minuto

    def hourDate(self,hour_arr, hour_dep):
        hora_arr,min_arr = self.horaMinSeparate(hour_arr)
        hora_dep,min_dep = self.horaMinSeparate(hour_dep)
        t_dep = str(time(hora_dep, min_dep))
        t_arr = str(time(hora_arr, min_arr))
        minutos = self.restarHora(t_arr,t_dep)
        return int(minutos)

"""hora = HoraData()
lista1 = ['21','36']
lista2 = ['18','30']

hora.hourDate(lista1,lista2)"""
