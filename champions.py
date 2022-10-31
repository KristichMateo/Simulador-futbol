from operator import eq, le, truth
import random
from re import A
import tkinter as tk
from tkinter import *


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

Manchester_City = Equipo(81,"Manchester City",9,5)
Liverpool = Equipo(80,"Liverpool",9,5)
Chelsea = Equipo(78,"Chelsea",9,5)
Tottenham = Equipo(77,"Tottenham",10,5)
Leicester_City = Equipo(73,"Leicester City",11,5)
West_Ham = Equipo(72,"West Ham",11,5)
Man_Utd = Equipo(76,"Manchester United",9,5)
Aston_Villa = Equipo(74,"Aston Villa",10,5) 
Crystal_palace = Equipo(72,"Crystal Palace",12,5)
Arsenal_eng = Equipo(75,"Arsenal",9,5)
Brentford = Equipo(67,"Brentford",11,4)
Newcastle = Equipo(69,"Newcaste",10,4)
Everton = Equipo(70,"Everton",11,4)
Southampton = Equipo(65,"Southampton",12,4)
Leeds = Equipo(67,"Leeds United",12,4)
Brighton = Equipo(65,"Brighton",10,4)
Wolverhampton = Equipo(70,"Wolverhampton",9,4)  
Burnley = Equipo(65,"Burnley",13,4)
Watford = Equipo(64,"Watford",13,4)
Norwich_City = Equipo(63,"Norwich City",14,4)
#relleno
Crystal_palace_2 = Equipo(72,"Crystal Palace_2",12,5)
Arsenal_eng_2 = Equipo(75,"Arsenal_2",9,5)
Brentford_2 = Equipo(67,"Brentford_2",11,4)
Newcastle_2 = Equipo(69,"Newcaste_2",10,4)
Everton_2 = Equipo(70,"Everton_2",11,4)
Southampton_2 = Equipo(65,"Southampton_2",12,4)
Leeds_2 = Equipo(67,"Leeds United_2",12,4)
Brighton_2 = Equipo(65,"Brighton_2",10,4)
Wolverhampton_2 = Equipo(70,"Wolverhampton_2",9,4)  
Burnley_2 = Equipo(65,"Burnley_2",13,4)
Watford_2 = Equipo(64,"Watford_2",13,4)
Norwich_City_2 = Equipo(63,"Norwich City_2",14,4)
#relleno
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
E= [Manchester_City,Liverpool,Chelsea,Tottenham,Leicester_City,West_Ham,Man_Utd, Aston_Villa,Crystal_palace,
Brentford,Newcastle,Everton,Southampton,Leeds,Brighton,Wolverhampton,Burnley,Watford,Norwich_City,Arsenal_eng,
Crystal_palace_2,Arsenal_eng_2,Brentford_2,Newcastle_2,Everton_2,Southampton_2,Leeds_2,Brighton_2,Wolverhampton_2,
Burnley_2,Watford_2,Norwich_City_2] #Lista de equipos
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
def simular_grupos():
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
    Grupos_json = {
        "A":str(sorted(grupos[0], key=lambda t: t.puntos , reverse=True)),
        "B":str(sorted(grupos[0], key=lambda t: t.puntos , reverse=True)),
        "C":str(sorted(grupos[0], key=lambda t: t.puntos , reverse=True)),
        "D":str(sorted(grupos[0], key=lambda t: t.puntos , reverse=True)),
        "E":str(sorted(grupos[0], key=lambda t: t.puntos , reverse=True)),
        "F":str(sorted(grupos[0], key=lambda t: t.puntos , reverse=True)),
        "G":str(sorted(grupos[0], key=lambda t: t.puntos , reverse=True)),
        "H":str(sorted(grupos[0], key=lambda t: t.puntos , reverse=True))}   
      #Ordenar primeros y segundos
        
    for i in range(16):                 #Identificar primeros y segundos
            if i % 2 == 0:
                lista_Primeros.append(lista_Octavos[i])

            if i % 2 != 0:
                lista_Segundos.append(lista_Octavos[i])                 #Identificar primeros y segundos
    return Grupos_json                                                                
def simular_octavos(): 
    cruces = []
    print("Octavos")
    for i in range(8):                  #Simular Octavos
        try:
            numero1 = random.randrange(0,8-i)           #sorteo de cruces
            equipo_1 = lista_Primeros.pop(numero1)
            numero2 = random.randrange(0,8-i)
            equipo_2 = lista_Segundos.pop(numero2)      #sorteo de cruces
            for k in range(2):                                                      #Simulacion IDA y VUELTA
                if k == 0:
                    print("IDA")
                    l_I = 0
                    v_I = 0
                    l_I = gol_local(equipo_1.pdg, equipo_2.pdd, equipo_1.pdc )
                    v_I = gol_visita(equipo_2.pdg, equipo_1.pdd, equipo_2.pdc)
                    equipo_1.goles += l_I
                    equipo_2.goles += v_I
                    print(equipo_1.nombre,l_I,":",v_I,equipo_2.nombre)
                elif k == 1:
                    print("VUELTA")
                    l_V = 0
                    v_V = 0
                    l_V = gol_local(equipo_2.pdg, equipo_1.pdd, equipo_2.pdc )
                    v_V = gol_visita(equipo_1.pdg, equipo_2.pdd, equipo_1.pdc)
                    equipo_2.goles += l_V
                    equipo_1.goles += v_V
                    print(equipo_2.nombre,l_V,":",v_V,equipo_1.nombre)
                    goles_primero = l_I + v_V
                    goles_segundo = v_I + l_V      
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
    print("lista cuartos",lista_Cuartos)
    return(Octavos_json)
def simular_cuartos():
    cruces = []
    print("Cuartos")   
    global lista_Semis
    lista_Semis = []
                                                 #Simulacion IDA y VUELTA
    for i in range(4):                  #Simular Cuartos
        try:
            print("lista semis",lista_Semis)
            numero1 = random.randrange(0,4-i)           #sorteo de cruces
            equipo_1 = lista_Cuartos.pop(numero1)
            numero2 = random.randrange(0,4-i)
            equipo_2 = lista_Cuartos.pop(numero2)      #sorteo de cruces
            for k in range(2):                                                      #Simulacion IDA y VUELTA
                    if k == 0:
                        print("IDA")
                        l_I = 0
                        v_I = 0
                        l_I = gol_local(equipo_1.pdg, equipo_2.pdd, equipo_1.pdc )
                        v_I = gol_visita(equipo_2.pdg, equipo_1.pdd, equipo_2.pdc)
                        equipo_1.goles += l_I
                        equipo_2.goles += v_I
                        print(equipo_1.nombre,l_I,":",v_I,equipo_2.nombre)
                    elif k == 1:
                        print("VUELTA")
                        l_V = 0
                        v_V = 0
                        l_V = gol_local(equipo_2.pdg, equipo_1.pdd, equipo_2.pdc )
                        v_V = gol_visita(equipo_1.pdg, equipo_2.pdd, equipo_1.pdc)
                        equipo_2.goles += l_V
                        equipo_1.goles += v_V
                        print(equipo_2.nombre,l_V,":",v_V,equipo_1.nombre)
                        goles_primero = l_I + v_V
                        goles_segundo = v_I + l_V      
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
    return Cuartos_json

def simular_semis():
    cruces = []
    print("Semis")
    print(lista_Semis)
    global lista_final
    lista_final = []
    for i in range(2):                  #Simular Semis
        try:
            
            equipo_1 = lista_Semis[i]
            equipo_2 = lista_Semis[i+2]
            #sorteo de cruces
            for k in range(2):                                                      #Simulacion IDA y VUELTA
                    if k == 0:
                        print("IDA")
                        l_I = 0
                        v_I = 0
                        l_I = gol_local(equipo_1.pdg, equipo_2.pdd, equipo_1.pdc )
                        v_I = gol_visita(equipo_2.pdg, equipo_1.pdd, equipo_2.pdc)
                        equipo_1.goles += l_I
                        equipo_2.goles += v_I
                        print(equipo_1.nombre,l_I,":",v_I,equipo_2.nombre)
                    elif k == 1:
                        print("VUELTA")
                        l_V = 0
                        v_V = 0
                        l_V = gol_local(equipo_2.pdg, equipo_1.pdd, equipo_2.pdc )
                        v_V = gol_visita(equipo_1.pdg, equipo_2.pdd, equipo_1.pdc)
                        equipo_2.goles += l_V
                        equipo_1.goles += v_V
                        print(equipo_2.nombre,l_V,":",v_V,equipo_1.nombre)
                        goles_primero = l_I + v_V
                        goles_segundo = v_I + l_V      
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
    return Semis_json
def simular_final():
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
    return Final_json

grupos_front = simular_grupos()
octavos_front = simular_octavos()
Cuartos_front = simular_cuartos()
Semis_front = simular_semis()
Final_front = simular_final()
print("Grupos simulados",grupos_front)
print("Octavos simulados",octavos_front)
print("Cuartos simulados",Cuartos_front)
print("Semis simuladas",Semis_front)
print("Final simulada",Final_front)