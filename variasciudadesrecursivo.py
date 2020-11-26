from random import randrange, choice
import random
import sys
import math
from loadData import LoadData


def inicializar (self):
    objload = LoadData()

listadebases=[0,1,2]

lista=[1,2,3,4,5,6]

listafinal=[]
emparejamiento=[]


def viajar():
    global sumando
    sumando=0
    global listaciudad1
    global listaciudad2
    global listaciudad3
    global listaciudad4
    global listaciudad5
    global listaciudad6

    global vuelosciudad1
    global vuelosciudad2
    global vuelosciudad3
    global vuelosciudad4
    global vuelosciudad5
    global vuelosciudad6
    
    listaciudad1=[2,3,4,5,6]
    listaciudad2=[1,3,4,5,6]
    listaciudad3=[1,2,4,5,6]
    listaciudad4=[1,2,3,5,6]
    listaciudad5=[1,2,3,4,6]
    listaciudad6=[1,2,3,4,5]
    #[vuelo,duracion,dia,hora,minuto]
    vuelosciudad1=[[2.01,50,1,6,30],[2.02,20,1,7,30],[3.03,12,1,8,30],[3.04,34,1,9,30],[4.05,32,1,10,30],[4.06,12,1,11,30],[5.07,31,1,12,30],[5.08,43,1,13,30],[6.09,54,1,14,30],[6.10,25,1,15,30]]
    vuelosciudad2=[[1.11,22,1,6,30],[1.12,23,1,7,30],[3.13,31,1,8,30],[3.14,43,1,9,30],[4.15,10,1,10,30],[4.16,11,1,11,30],[5.17,44,1,12,30],[5.18,32,1,13,30],[6.19,23,1,14,30],[6.20,12,1,15,30]]
    vuelosciudad3=[[1.21,12,1,10,30],[1.22,13,1,11,30],[2.23,14,1,12,30],[2.24,21,1,13,30],[4.25,32,1,14,30],[4.26,31,1,15,30],[5.27,12,1,16,30],[5.28,54,1,17,30],[6.29,32,1,18,30],[6.30,76,1,19,30]]
    vuelosciudad4=[[1.31,34,1,10,30],[1.32,55,1,11,30],[2.33,54,1,12,30],[2.34,24,1,13,30],[3.35,33,1,14,30],[3.36,54,1,15,30],[5.37,32,1,16,30],[5.38,43,1,17,30],[6.39,23,1,18,30],[6.40,44,1,19,30]]
    vuelosciudad5=[[1.41,12,1,10,30],[1.42,33,1,11,30],[2.43,32,1,12,30],[2.44,43,1,13,30],[3.45,42,1,14,30],[3.46,52,1,15,30],[4.47,12,1,16,30],[4.48,21,1,17,30],[6.49,22,1,18,30],[6.50,33,1,19,30]]
    vuelosciudad6=[[1.51,44,1,10,30],[1.52,23,1,11,30],[2.53,54,1,12,30],[2.54,41,1,13,30],[3.55,14,1,14,30],[3.56,76,1,15,30],[4.57,42,1,16,30],[4.58,22,1,17,30],[5.59,11,1,18,30],[5.60,22,1,19,30]]
 
    global base
    base=escogerbase();
    print("\nla base es: ",base);
    emparejamiento.append(base);
    armandolo(base);
    
def escogerbase():
    return random.randint(1,2);


def seleccion(self, base):

def armandolo(base):
    global tiempototal
    if base==1:
        #print("sus destinos son: ", vuelosciudad1);
        vuelo = random.choice(vuelosciudad1);
        emparejamiento.append(vuelo[0]);
        #print("vuelo escogido es :",vuelo[0])
        aja=vuelo[0]
        tdv=vuelo[1]
        #print("tiempo de vuelo es: ",tdv)
        parte_decimal, parte_entera = math.modf(aja)
        #print ("el siguiente vuelo es : ",vuelo);
        a = format(parte_entera);
        destino = float(a);
        
        #print("\nposicion escogida es: ",listaciudad1.index(destino));
        vuelosciudad1.pop(vuelosciudad1.index(vuelo));
        tiempototal=sumando+tdv;
        listando(destino,base,tiempototal,vuelo);
    if base==2:
        #print("sus destinos son: ",vuelosciudad2);
        vuelo = random.choice(vuelosciudad2);
        emparejamiento.append(vuelo[0]);
        #print("vuelo escogido es: ",vuelo[0])
        aja=vuelo[0]
        tdv=vuelo[1]
        #print("tiempo de vuelo es: ",tdv)
        parte_decimal, parte_entera = math.modf(aja)
        #print ("el siguiente vuelo es: ",vuelo);
        a = format(parte_entera);
        destino = float(a);
        #print("\nposicion escogida es: ",listaciudad2.index(destino));
        vuelosciudad2.pop(vuelosciudad2.index(vuelo));
        
        tiempototal=sumando+tdv;
        listando(destino,base,tiempototal,vuelo);
    
def listando(destino,base,tiempototal,vuelo):
    #print("\nnuevo origen: ",destino);
    tiempototal=tiempototal+0;
    if destino==base:
        #print("\nregreso a base")
        print("el emparejamiento es: ",emparejamiento);
        print("tiempo total de vuelo: ",tiempototal);
        listafinal.append(emparejamiento);
        
        while len (emparejamiento) != 0:
            emparejamiento.pop();
        if 1==1:
            #print("aqui acaba");
            hormigas=7
            if len (listafinal) == hormigas:
                print("\nprograma termino");
                #print(listafinal);
                sys.exit();
            for i in range(hormigas):
                #print(" ");
                viajar();
    else:
        recu(destino,tiempototal,vuelo);
            

def hormigas():
        objload = LoadData()
        
        aux = objload.getBasesConexiones()
        print(aux)
        viajar();
       
def recu(destino,tiempototal,vuelo):
    for i in range(7):
        i=i+1;
        if (i==destino):
            if(i==1):
                vuelosciudadx=vuelosciudad1;
            if(i==2):
                vuelosciudadx=vuelosciudad2;
            if(i==3):
                vuelosciudadx=vuelosciudad3;
            if(i==4):
                vuelosciudadx=vuelosciudad4;
            if(i==5):
                vuelosciudadx=vuelosciudad5;
            if(i==6):
                vuelosciudadx=vuelosciudad6;

    if len (vuelosciudadx) == 0:
        print ("no se logro ir a la base");
        while len (emparejamiento) != 0:
            emparejamiento.pop();
                
    else: 
        proximo=random.choice(vuelosciudadx);
        #print("sus destinos son: ",vuelosciudadx);
        emparejamiento.append(proximo[0]);
        odia=vuelo[3]
        ddia=proximo[3]
        resta=ddia-odia
        #print(" resta ",resta)
        #print("proximo: ",proximo)
        aja=proximo[0]
        tdv=proximo[1]
        tiempototal=tiempototal+tdv;
        parte_decimal, parte_entera = math.modf(aja)
        #print ("el siguiente vuelo es: ",proximo);
        #print("sumando:",tiempototal);
        a = format(parte_entera);
        destino = float(a);
        #print("posicion escogida es: ",listaciudad1.index(proximo));
        vuelosciudadx.pop(vuelosciudadx.index(proximo));
            
        listando(destino,base,tiempototal,proximo);
            

hormigas();

