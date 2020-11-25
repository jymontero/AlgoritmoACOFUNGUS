from random import randrange, choice
import random
import sys

listadebases=[0,1,2]
listadeciudades=[0,1,2,3,4,5,6]


listaciudad0=[1,1,2,4]
listaciudad1=[2,2,0,0,0]
listaciudad2=[1,1,3,3,4,5]
listaciudad3=[0,1]
listaciudad4=[0,6]
listaciudad5=[2,6]
listaciudad6=[4,5]


emparejamiento=[]

def elegirbase():
    return randrange(3);

def e():
    
    basep = elegirbase();
    print ("eligio la base", basep);
    emparejamiento.append(basep);

    if basep==0:
        print ("sus destinos posibles son: ",listaciudad0);
        #print(emparejamiento);
        destino = random.choice(listaciudad0);
        print ("el destino elegido es",destino);
        emparejamiento.append(destino);
        #listaciudad0.pop(destino);
        #print("lista actual",listaciudad0);
        
        #print(emparejamiento);
        
        a(destino,basep);
        
    if basep==1:
        print ("sus destinos posibles son: ",listaciudad1);
        #print(emparejamiento);
        destin = random.choice(listaciudad1);
        print ("el destino elegido es",destin);
        emparejamiento.append(destin);
        #listaciudad1.pop(destin);
        #print("lista actual",listaciudad1);
        #print(emparejamiento);
        
        a(destin,basep);
        
    if basep==2:
        print ("sus destinos posibles son: ",listaciudad2);
        #print(emparejamiento);
        desti = random.choice(listaciudad2);
        print ("el destino elegido es",desti);
        emparejamiento.append(desti);
        #listaciudad2.pop(desti);
        #print("lista actual",listaciudad2);
        #print(emparejamiento);

        a(desti,basep);


def a(destinom,basep):

    print("\nNUEVO ORIGEN ES: ", destinom);
    #print("base principal es: ",basep);
    while True:
        if destinom==0:
            proximo=random.choice(listaciudad0);
            print("sus destinos son: ",listaciudad0);
            print("el destino elegido ahora es ",proximo);
            emparejamiento.append(proximo);
            #listaciudad0.pop(proximo);
            #print("lista actual",listaciudad0);
            #print(emparejamiento);
            if (proximo==basep):
                print("\n\nregreso a la base\n");
                print ("el emparejamiento es ",emparejamiento);
                sys.exit()
                break;
            else:
                a(proximo,basep);

        if destinom==1:
            proximo=random.choice(listaciudad1);
            print("sus destinos son: ",listaciudad1);
            print("el destino elegido ahora es ",proximo);
            emparejamiento.append(proximo);
            #listaciudad1.pop(proximo);
            #print("lista actual",listaciudad1);
            #print(emparejamiento);
            if (proximo==basep):
                print("\n\nregreso a la base\n");
                print ("el emparejamiento es ",emparejamiento);
                sys.exit()
                break;
            else:
                a(proximo,basep);

        if destinom==2:
            proximo=random.choice(listaciudad2);
            print("sus destinos son: ",listaciudad2);
            print("el destino elegido ahora es ",proximo);
            emparejamiento.append(proximo);
            #listaciudad2.pop(proximo);
            #print("lista actual",listaciudad2);
            #print(emparejamiento);
            if (proximo==basep):
                print("\n\nregreso a la base\n");
                print ("el emparejamiento es ",emparejamiento);
                sys.exit()
                break;
            else:
                a(proximo,basep);

        if destinom==3:
            proximo=random.choice(listaciudad3);
            print("sus destinos son: ",listaciudad3);
            print("el destino elegido ahora es ",proximo);
            emparejamiento.append(proximo);
            #listaciudad3.pop(proximo);
            #print("lista actual",listaciudad3);
            #print(emparejamiento);
            if (proximo==basep):
                print("\n\nregreso a la base\n");
                print ("el emparejamiento es ",emparejamiento);
                sys.exit()
                break;
            else:
                a(proximo,basep);

        if destinom==4:
            proximo=random.choice(listaciudad4);
            print("sus destinos son: ",listaciudad4);
            print("el destino elegido ahora es ",proximo);
            emparejamiento.append(proximo);
            #listaciudad4.pop(proximo);
            #print("lista actual",listaciudad4);
            #print(emparejamiento);
            if (proximo==basep):
                print("\n\nregreso a la base\n");
                print ("el emparejamiento es ",emparejamiento);
                sys.exit()
                break;
            else:
                a(proximo,basep);

        if destinom==5:
            proximo=random.choice(listaciudad5);
            print("sus destinos son: ",listaciudad5);
            print("el destino elegido ahora es ",proximo);
            emparejamiento.append(proximo);
            #listaciudad5.pop(proximo);
            #print("lista actual",listaciudad5);
            #print(emparejamiento);
            if (proximo==basep):
                print("\n\nregreso a la base \n");
                print ("el emparejamiento es ",emparejamiento);
                sys.exit()
                break;
            else:
                a(proximo,basep);

        if destinom==6:
            proximo=random.choice(listaciudad6);
            print("sus destinos son: ",listaciudad6);
            print("el destino elegido ahora es ",proximo);
            emparejamiento.append(proximo);
            #listaciudad6.pop(proximo);
            #print("lista actual",listaciudad6);
            #print(emparejamiento);
            if (proximo==basep):
                print("\n\nregreso a la base \n");
                print ("el emparejamiento es ",emparejamiento);
                sys.exit()
                break;
            else:
                a(proximo,basep);


def fin():
    for ejecucion in range(3):
        e();


fin()

    #sys.exit()
    #raise SystemExit


