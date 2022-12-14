from operator import eq, le, truth
import random
from re import A
import tkinter as tk
from tkinter import *

def simular_qatar():
    def gol_local (pdg,pdd,pdc):
                global golL
                golL = 0
                for k in range (pdc):       #utilizo pdc para la cantidad de "chances" que tendra cada equipo
                    p=random.randint(0,100)
                    b=random.randint(0,25)  #Creo 2 numeros aleatorios para pdd y pdg
                    if p < pdg and b < pdd:
                        golL = golL+1
                    if k == 4:
                        return golL
                return golL
    def gol_visita (pdg,pdd,pdc):
        global golV
        golV = 0
        for k in range (pdc):
                    p=random.randint(0,100)
                    b=random.randint(0,25)
                    if p < pdg and b < pdd:
                        golV = golV+1
                    if k == 4:
                        return golV
        return golV
    class Equipo:           #Clase equipo con probabilidad de gol (pdg), nombre, probabilidad de defensa (pdd), y probabilidad de chance (pdc)
        def __init__(self, pdg , nombre, pdd, pdc):
            self.nombre = nombre
            self.pdg = pdg
            self.puntos = 0
            self.pdd = pdd
            self.pdc = pdc
            self.goles = 0
        def __repr__(self):
            return self.nombre 

    Manchester_City = Equipo(63,"Qatar",19,4)
    Real_Madrid = Equipo(90,"Belgica",9,5)
    Chelsea = Equipo(90,"Brasil",10,5)
    Tottenham = Equipo(89,"Francia",10,5)
    Milan = Equipo(89,"Argentina",9,5)
    Bayern_Múnich = Equipo(87,"Inglaterra",11,5)
    Psg = Equipo(86,"España",12,5)
    Oporto = Equipo(87,"Portugal",12,5) 
    Ajax = Equipo(80,"Dinamarca",12,4)
    Eintracht_Frankfurt = Equipo(86,"Paises Bajos",11,5)
    Atletico_madrid = Equipo(87,"Alemania",10,5)
    Barcelona  = Equipo(79,"Suiza",13,4)
    Liverpool = Equipo(80,"Croacia",12,5)
    Sevilla = Equipo(81,"Uruguay",13,5)
    Juventus = Equipo(78,"Mexico",14,5)
    RB_leipzig = Equipo(76,"Estados Unidos",15,4)
    Borussia_Dortmund = Equipo(76,"Iran",13,4)  
    RB_Salzburgo = Equipo(73,"Japon",14,4)
    Shakhtar_Donetsk = Equipo(75,"Serbia",13,4)
    Inter_milan = Equipo(74,"Corea del sur",15,5)
    #relleno
    Nápoles = Equipo(73,"Canada",14,5)
    Benfica  = Equipo(77,"Polonia",13,5)
    Sporting_lisboa = Equipo(72,"Marruecos",13,4)
    Olympique_Marsella = Equipo(74,"Senegal",15,4)
    Brujas  = Equipo(71,"Arabia Saudita",16,5)
    Celtic  = Equipo(72,"Ecuador",14,4)
    Victoria_Plzen= Equipo(69,"Ghana",17,4)
    Maccabi_Haifa  = Equipo(68,"Tunez",18,4)
    Rangers  = Equipo(68,"Camerun",18,4)  
    FC_Copenhague = Equipo(68,"Australia",17,4)
    Dinamo_Zagreb = Equipo(73,"Gales",14,4)
    Leverkusen = Equipo(69,"Costa Rica",16,4)
    #relleno
    E= [Manchester_City,Leverkusen,Chelsea,Tottenham,Real_Madrid,Milan,Bayern_Múnich, Psg,Oporto,
    Ajax,Eintracht_Frankfurt,Atletico_madrid,Barcelona,Liverpool,Sevilla,Juventus,RB_leipzig,Borussia_Dortmund,RB_Salzburgo,Shakhtar_Donetsk,
    Inter_milan,Nápoles,Benfica,Sporting_lisboa,Olympique_Marsella,Brujas,Celtic,Victoria_Plzen,Maccabi_Haifa,
    Rangers,FC_Copenhague,Dinamo_Zagreb] #Lista de equipos
    A_grupo = []        #grupos
    B_grupo = []
    C_grupo = []
    D_grupo = []
    E_grupo = []
    F_grupo = []
    G_grupo = []
    H_grupo = []        #grupos

    grupos = [A_grupo,B_grupo,C_grupo,D_grupo,E_grupo,F_grupo,G_grupo,H_grupo] #lista de grupos
    lista_fase_grupos = []      #listas de distintas instancia de la competencia
    lista_Octavos = []
    lista_Primeros = []
    lista_Segundos = []
    lista_Cuartos = [] 
    lista_Semis = []
    lista_final = []  
    cruces = []
    Grupos_json = {}
    Octavos_json = {}   
    Cuartos_json = {}   
    Semis_json = {}  
    Final_json = {}  
    retorno = {
        "grupos":"",
        "octavos":"",
        "cuartos":"",
        "semis":"",
        "final":""
    }                            
    equipo_aleatorio = 0
    for i in range(8):
            grupo_actual = grupos[i]
            for k in range(4):                              #asignacion de grupos aleatoriamente
                try:
                    longitud = len(E)
                    equipo_aleatorio = random.randint(0,longitud+1)
                    grupo_actual.append(E[equipo_aleatorio])
                    print("escudo 1")
                    E.pop(equipo_aleatorio)
                except IndexError:
                    try:
                        longitud = len(E)
                        equipo_aleatorio = random.randint(0,longitud+1)
                        grupo_actual.append(E[equipo_aleatorio])
                        E.pop(equipo_aleatorio)
                        print("escudo 2")

                    except IndexError:
                        try:
                            longitud = len(E)
                            equipo_aleatorio = random.randint(0,longitud+1)
                            grupo_actual.append(E[equipo_aleatorio])
                            E.pop(equipo_aleatorio)
                            print("escudo 3")

                        except IndexError:
                            try:
                                longitud = len(E)
                                equipo_aleatorio = random.randint(0,longitud+1)
                                grupo_actual.append(E[equipo_aleatorio])
                                E.pop(equipo_aleatorio)
                                print("escudo 4")

                            except IndexError:
                                try:
                                    longitud = len(E)
                                    equipo_aleatorio = random.randint(0,longitud+1)
                                    grupo_actual.append(E[equipo_aleatorio])
                                    E.pop(equipo_aleatorio)           
                                    print("escudo 5")

                                except IndexError:
                                    try:
                                        longitud = len(E)
                        
                                        equipo_aleatorio = random.randint(0,longitud+1)
                                        grupo_actual.append(E[equipo_aleatorio])
                                        E.pop(equipo_aleatorio)
                                        print("escudo 6")
                                    except IndexError:
                                        try:
                                            longitud = len(E)
                            
                                            equipo_aleatorio = random.randint(0,longitud+1)
                                            grupo_actual.append(E[equipo_aleatorio])
                                            E.pop(equipo_aleatorio)
                                            print("escudo 7")
                                        except IndexError:
                                            try:
                                                longitud = len(E)
                                
                                                equipo_aleatorio = random.randint(0,longitud+1)
                                                grupo_actual.append(E[equipo_aleatorio])
                                                E.pop(equipo_aleatorio)
                                                print("escudo 8")
                                            except IndexError:
                                                longitud = len(E)
                                
                                                equipo_aleatorio = random.randint(0,longitud+1)
                                                grupo_actual.append(E[equipo_aleatorio])
                                                E.pop(equipo_aleatorio)
                                                print("escudo 9")                             #asignacion de grupos aleatoriamente


    for grupos_iterador in range(8):
            Puntos = []
            GF = []
            GC = []
            DG = []

            for j in range (4):
                Puntos += [0]
                GF += [0]
                GC += [0]
                DG += [0]

                
            
            for i in range (4):
                print(grupos[grupos_iterador][i].nombre,"en casa:") 
                for c in range (4):
                    l = 0
                    v = 0
                    if grupos[grupos_iterador][c].nombre != grupos[grupos_iterador][i].nombre: #Para evitar que un equipo juegue contra si mismo
                        l = gol_local(grupos[grupos_iterador][i].pdg,grupos[grupos_iterador][c].pdd,grupos[grupos_iterador][i].pdc) #Asigno el gol al equipo local
                        v = gol_visita(grupos[grupos_iterador][c].pdg,grupos[grupos_iterador][i].pdd,grupos[grupos_iterador][c].pdc)   #Asigno el gol al equipo visitante
                        grupos[grupos_iterador][i].goles += l
                        grupos[grupos_iterador][c].goles += v
                        print(grupos[grupos_iterador][i].nombre,l,":",v,grupos[grupos_iterador][c].nombre) #imprimo resultado
                        if v < l:                            #Asignacion de puntos
                            Puntos[i] = Puntos[i]+3
                        elif v == l:
                            Puntos[i] = Puntos[i]+1
                            Puntos[c] = Puntos[c]+1     
                        elif v > l:
                            Puntos[c] = Puntos[c]+3         #Asignacion de puntos
                
            Q = []
            for i in range(4):
                grupos[grupos_iterador][i].puntos = Puntos[i]
                print(grupos[grupos_iterador][i].nombre,":",grupos[grupos_iterador][i].puntos, grupos[grupos_iterador][i].goles) #imprimo puntos y goles hechos por equipo
                Q.append(Puntos[i])
            grupo_ordenado = sorted(grupos[grupos_iterador], key=lambda t: t.puntos , reverse=True) #Ordenar primeros y segundos
            lista_fase_grupos.append(grupo_ordenado)
            print("grupo ordenado:",grupo_ordenado)
            lista_Octavos.append(grupo_ordenado[0])          
            lista_Octavos.append(grupo_ordenado[1]) 
            A = sorted(grupos[0], key=lambda t: t.puntos , reverse=True)
            B = sorted(grupos[1], key=lambda t: t.puntos , reverse=True)
            C = sorted(grupos[2], key=lambda t: t.puntos , reverse=True)
            D = sorted(grupos[3], key=lambda t: t.puntos , reverse=True)
            E2 = sorted(grupos[4], key=lambda t: t.puntos , reverse=True)
            F = sorted(grupos[5], key=lambda t: t.puntos , reverse=True)
            G = sorted(grupos[6], key=lambda t: t.puntos , reverse=True)
            H = sorted(grupos[7], key=lambda t: t.puntos , reverse=True)
    Grupos_json = {
            "A":[A[0].nombre,A[0].puntos,A[1].nombre,A[1].puntos,A[2].nombre,A[2].puntos,A[3].nombre,A[3].puntos,],
            "B":[B[0].nombre,B[0].puntos,B[1].nombre,B[1].puntos,B[2].nombre,B[2].puntos,B[3].nombre,B[3].puntos,],
            "C":[C[0].nombre,C[0].puntos,C[1].nombre,C[1].puntos,C[2].nombre,C[2].puntos,C[3].nombre,C[3].puntos,],
            "D":[D[0].nombre,D[0].puntos,D[1].nombre,D[1].puntos,D[2].nombre,D[2].puntos,D[3].nombre,D[3].puntos,],
            "E":[E2[0].nombre,E2[0].puntos,E2[1].nombre,E2[1].puntos,E2[2].nombre,E2[2].puntos,E2[3].nombre,E2[3].puntos,],
            "F":[F[0].nombre,F[0].puntos,F[1].nombre,F[1].puntos,F[2].nombre,F[2].puntos,F[3].nombre,F[3].puntos,],
            "G":[G[0].nombre,G[0].puntos,G[1].nombre,G[1].puntos,G[2].nombre,G[2].puntos,G[3].nombre,G[3].puntos,],
            "H":[H[0].nombre,H[0].puntos,H[1].nombre,H[1].puntos,H[2].nombre,H[2].puntos,H[3].nombre,H[3].puntos,]}
        #Ordenar primeros y segundos
            
    for i in range(16):                 #Identificar primeros y segundos
                if i % 2 == 0:
                    lista_Primeros.append(lista_Octavos[i])

                if i % 2 != 0:
                    lista_Segundos.append(lista_Octavos[i])                 #Identificar primeros y segundos
        # return Grupos_json 
    retorno.update({"grupos":Grupos_json})      
    cruces = []
    print("Octavos")
    p = 8
    for i in range(8):
        print("iiiii",i)                  #Simular Octavos
        try:
                
                                              #sorteo de cruces
                if i ==0:
                    equipo_1 = A[0]
                    equipo_2 = B[1]   
                elif i == 1:
                    equipo_1 = A[1]
                    equipo_2 = B[0]
                elif i == 2:
                    equipo_1 = C[0]
                    equipo_2 = D[1]       
                elif i == 3:
                    equipo_1 = C[1]
                    equipo_2 = D[0]     
                elif i == 4:
                    equipo_1 = E2[0]
                    equipo_2 = F[1]       
                elif i == 5:
                    equipo_1 = E2[1]
                    equipo_2 = F[0]
                elif i == 6:
                    equipo_1 = G[0]
                    equipo_2 = H[1]     
                elif i == 7:
                    equipo_1 = G[1]
                    equipo_2 = H[0]            #sorteo de cruces
                p = p-1
                l_V = 0
                v_V = 0
                l_V = gol_local(equipo_2.pdg, equipo_1.pdd, equipo_2.pdc )
                v_V = gol_visita(equipo_1.pdg, equipo_2.pdd, equipo_1.pdc)
                equipo_2.goles += l_V
                equipo_1.goles += v_V
                print(equipo_2.nombre,l_V,":",v_V,equipo_1.nombre)
                goles_primero = v_V
                goles_segundo = l_V      
                if goles_primero > goles_segundo:
                        lista_Cuartos.append(equipo_1)
                elif goles_segundo > goles_primero:
                        lista_Cuartos.append(equipo_2)
                else:                                             #Simulacion penales (en caso de empate)
                            "EMPATARON"     
                            anotados_primero = 0
                            anotados_segundo = 0
                            for i in range(5):
                                penal = random.randint(0,10)
                                if penal > 3:
                                    anotados_primero = anotados_primero + 1
                                else:
                                    anotados_primero = anotados_primero + 0
                            for j in range(5):
                                penal = random.randint(0,10)
                                if penal > 3:
                                    anotados_segundo = anotados_segundo + 1
                                else:
                                    anotados_segundo = anotados_segundo + 0
                            if anotados_primero > anotados_segundo:
                                lista_Cuartos.append(equipo_1)
                                print("gano 1 por penales")
                            elif anotados_primero < anotados_segundo:
                                lista_Cuartos.append(equipo_2)
                                print("gano 2 por penales")                     #Simulacion penales (en caso de empate)

                            else:                                              #En caso de que emapten los 5 primeros penales
                                
                                print("empataron los 5 penales")
                                while anotados_primero == anotados_segundo:
                                    penal = random.randint(0,10)
                                    if penal > 3:
                                        anotados_primero = anotados_primero + 1
                                    else:
                                        anotados_primero = anotados_primero + 0
                                    penal = random.randint(0,10)
                                    if penal > 3:
                                        anotados_primero = anotados_primero + 1
                                    else:
                                        anotados_primero = anotados_primero + 0
                                if anotados_primero > anotados_segundo:
                                    lista_Cuartos.append(equipo_1)
                                    print("clasifico por penales", equipo_1)
                                elif anotados_primero < anotados_segundo:
                                    lista_Cuartos.append(equipo_2)
                                    print("clasifico por penales", equipo_2)
                if goles_primero != goles_segundo:
                            a = equipo_1.nombre,goles_primero ,":", goles_segundo,equipo_2.nombre
                else:
                            a = equipo_1.nombre,goles_primero ,":", goles_segundo,equipo_2.nombre,anotados_primero,anotados_segundo
                cruces.append(a)
                print(cruces)
                print(len(cruces))
                
        except IndentationError:
                print("error 1") 
    Octavos_json ={
                            "cruce1":cruces[0],
                            "cruce2":cruces[1],
                            "cruce3":cruces[2],
                            "cruce4":cruces[3],
                            "cruce5":cruces[4],
                            "cruce6":cruces[5],
                            "cruce7":cruces[6],
                            "cruce8":cruces[7],
                        }
    print("lista cuartos",Octavos_json)
    retorno.update({"octavos":Octavos_json})      

    # return(Octavos_json)
    cruces = []
    print("Cuartos")   
    lista_Semis = []
                                                    #Simulacion IDA y VUELTA
    for i in range(4):                  #Simular Cuartos
            try:
                print("lista semis",lista_Semis)
                      #sorteo de cruces
                equipo_1=lista_Cuartos[i]
                equipo_2=lista_Cuartos[i+1]

                    #sorteo de cruces
              
                l_V = 0
                v_V = 0
                l_V = gol_local(equipo_2.pdg, equipo_1.pdd, equipo_2.pdc )
                v_V = gol_visita(equipo_1.pdg, equipo_2.pdd, equipo_1.pdc)
                equipo_2.goles += l_V
                equipo_1.goles += v_V
                print(equipo_2.nombre,l_V,":",v_V,equipo_1.nombre)
                equipo_2.goles += l_V
                equipo_1.goles += v_V 
                if goles_primero > goles_segundo:
                                lista_Semis.append(equipo_1)
                elif goles_segundo > goles_primero:
                                lista_Semis.append(equipo_2)
                else:                                             #Simulacion penales (en caso de empate)
                                "EMPATARON"     
                                anotados_primero = 0
                                anotados_segundo = 0
                                for i in range(5):
                                    penal = random.randint(0,10)
                                    if penal > 3:
                                        anotados_primero = anotados_primero + 1
                                    else:
                                        anotados_primero = anotados_primero + 0
                                for j in range(5):
                                    penal = random.randint(0,10)
                                    if penal > 3:
                                        anotados_segundo = anotados_segundo + 1
                                    else:
                                        anotados_segundo = anotados_segundo + 0
                                if anotados_primero > anotados_segundo:
                                    lista_Semis.append(equipo_1)
                                    print("gano 1 por penales")
                                elif anotados_primero < anotados_segundo:
                                    lista_Semis.append(equipo_2)
                                    print("gano 2 por penales")                     #Simulacion penales (en caso de empate)

                                else:                                              #En caso de que emapten los 5 primeros penales
                                    
                                    print("empataron los 5 penales")
                                    while anotados_primero == anotados_segundo:
                                        penal = random.randint(0,10)
                                        if penal > 3:
                                            anotados_primero = anotados_primero + 1
                                        else:
                                            anotados_primero = anotados_primero + 0
                                        penal = random.randint(0,10)
                                        if penal > 3:
                                            anotados_primero = anotados_primero + 1
                                        else:
                                            anotados_primero = anotados_primero + 0
                                    if anotados_primero > anotados_segundo:
                                        lista_Semis.append(equipo_1)
                                        print("clasifico por penales", equipo_1)
                                    elif anotados_primero < anotados_segundo:
                                        lista_Semis.append(equipo_2)
                                        print("clasifico por penales", equipo_2)    #En caso de que emapten los 5 primeros penales
                if goles_primero != goles_segundo:
                                a = equipo_1.nombre,goles_primero ,":", goles_segundo,equipo_2.nombre
                else:
                                a = equipo_1.nombre,goles_primero ,":", goles_segundo,equipo_2.nombre,anotados_primero,anotados_segundo
                cruces.append(a)
                print(cruces)
                        
            except IndentationError:
                    print("error")                       
            print("lista semis:",lista_Semis)
    Cuartos_json ={
            "cruce1":cruces[0],
            "cruce2":cruces[1],
            "cruce3":cruces[2],
            "cruce4":cruces[3], }
    print("gggggggggg",Cuartos_json)
    retorno.update({"cuartos":Cuartos_json})      

        # return Cuartos_json

    cruces = []
    print("Semis")
    print(lista_Semis)
    lista_final = []
    for i in range(2):                  #Simular Semis
            try:
                
                equipo_1 = lista_Semis[i]
                equipo_2 = lista_Semis[i+2]
                #sorteo de cruces
                l_V = 0
                v_V = 0
                l_V = gol_local(equipo_2.pdg, equipo_1.pdd, equipo_2.pdc )
                v_V = gol_visita(equipo_1.pdg, equipo_2.pdd, equipo_1.pdc)
                equipo_2.goles += l_V
                equipo_1.goles += v_V
                print(equipo_2.nombre,l_V,":",v_V,equipo_1.nombre)
                equipo_2.goles += l_V
                equipo_1.goles += v_V    
                if goles_primero > goles_segundo:
                                lista_final.append(equipo_1)
                elif goles_segundo > goles_primero:
                                lista_final.append(equipo_2)
                else:                                             #Simulacion penales (en caso de empate)
                                "EMPATARON"     
                                anotados_primero = 0
                                anotados_segundo = 0
                                for i in range(5):
                                    penal = random.randint(0,10)
                                    if penal > 3:
                                        anotados_primero = anotados_primero + 1
                                    else:
                                        anotados_primero = anotados_primero + 0
                                for j in range(5):
                                    penal = random.randint(0,10)
                                    if penal > 3:
                                        anotados_segundo = anotados_segundo + 1
                                    else:
                                        anotados_segundo = anotados_segundo + 0
                                if anotados_primero > anotados_segundo:
                                    lista_final.append(equipo_1)
                                    print("gano 1 por penales")
                                elif anotados_primero < anotados_segundo:
                                    lista_final.append(equipo_2)
                                    print("gano 2 por penales")                     #Simulacion penales (en caso de empate)

                                else:                                              #En caso de que emapten los 5 primeros penales
                                    
                                    print("empataron los 5 penales")
                                    while anotados_primero == anotados_segundo:
                                        penal = random.randint(0,10)
                                        if penal > 3:
                                            anotados_primero = anotados_primero + 1
                                        else:
                                            anotados_primero = anotados_primero + 0
                                        penal = random.randint(0,10)
                                        if penal > 3:
                                            anotados_primero = anotados_primero + 1
                                        else:
                                            anotados_primero = anotados_primero + 0
                                    if anotados_primero > anotados_segundo:
                                        lista_final.append(equipo_1)
                                        print("clasifico por penales", equipo_1)
                                    elif anotados_primero < anotados_segundo:
                                        lista_final.append(equipo_2)
                                        print("clasifico por penales", equipo_2)    #En caso de que emapten los 5 primeros penales
                if goles_primero != goles_segundo:
                                a = equipo_1.nombre,goles_primero ,":", goles_segundo,equipo_2.nombre
                else:
                                a = equipo_1.nombre,goles_primero ,":", goles_segundo,equipo_2.nombre,anotados_primero,anotados_segundo
                cruces.append(a)
                            
            except IndentationError:
                    print("error")                       
    print("lista final:",lista_final)
    Semis_json ={
                                "cruce1":cruces[0],
                                "cruce2":cruces[1],
                                
                            }
    retorno.update({"semis":Semis_json})      

    cruces = []
    print("Final")
    print("finalistas",lista_final)
    equipo_1 = lista_final[0]
    equipo_2 = lista_final[1]
    l_I = 0
    v_I = 0
    l_I = gol_local(equipo_1.pdg, equipo_2.pdd, equipo_1.pdc )
    v_I = gol_visita(equipo_2.pdg, equipo_1.pdd, equipo_2.pdc)
    equipo_1.goles += l_I
    equipo_2.goles += v_I
    print(equipo_1.nombre,l_I,":",v_I,equipo_2.nombre)
    if l_I > v_I:
            ganador = equipo_1.nombre
            print("Ganador:",ganador)
    elif l_I < v_I:
            ganador = equipo_2.nombre
            print("Ganador",ganador)
    else:
            print("desempate de la final")     
            anotados_primero = 0
            anotados_segundo = 0
            for i in range(5):
                penal = 0
                penal = random.randint(0,10)
                if penal > 3:
                    anotados_primero = anotados_primero + 1
                else:
                    anotados_primero = anotados_primero + 0
            for j in range(5):
                penal = 0
                penal = random.randint(0,10)
                if penal > 3:
                    anotados_segundo = anotados_segundo + 1
                else:
                    anotados_segundo = anotados_segundo + 0
            if anotados_primero > anotados_segundo:
                    ganador = equipo_1.nombre
                    print("el ganador es", ganador)
            elif anotados_primero < anotados_segundo:
                    ganador = equipo_2.nombre
                    print("el ganador es", ganador)
                    print(equipo_1.nombre,anotados_primero,":",anotados_segundo,equipo_2.nombre)
            else:                                              #En caso de que emapten los 5 primeros penales
                print("empataron los 5 penales")
                while anotados_primero == anotados_segundo:
                        penal = random.randint(0,10)
                        if penal > 3:
                            anotados_primero = anotados_primero + 1
                        else:
                            anotados_primero = anotados_primero + 0
                        penal = random.randint(0,10)
                        if penal > 3:
                            anotados_primero = anotados_primero + 1
                        else:
                            anotados_primero = anotados_primero + 0
                        if anotados_primero > anotados_segundo:
                            ganador = equipo_1.nombre
                            print("el ganador es", ganador)
                        elif anotados_primero < anotados_segundo:
                            ganador = equipo_2.nombre
                            print("el ganador es", ganador)                              #En caso de que emapten los 5 primeros penales

                            #Ejecucion de funciones
    if l_I != v_I:
            a = equipo_1.nombre,l_I ,":", v_I,equipo_2.nombre
    else:
            a = equipo_1.nombre,l_I,":",v_I,equipo_2.nombre,anotados_primero,anotados_segundo
    cruces.append(a)
    Final_json ={
            "cruce1":cruces[0],
            "campeon":ganador
                            }
    retorno.update({"final":Final_json})      

    return retorno
a  = simular_qatar()
print(a)