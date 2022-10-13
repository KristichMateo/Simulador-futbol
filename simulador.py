import random
import tkinter as tk
from tkinter import *


class Equipo:
	def __init__(self, pdg , nombre, pdd, pdc):
		self.nombre = nombre
		self.pdg = pdg
		self.puntos = 0
		self.pdd = pdd
		self.pdc = pdc

	def __repr__(self):
		return self.nombre 

Talleres = Equipo(75,"Talleres de Cordoba",8,5)
River = Equipo(80,"River Plate",8 ,5)
Estudiantes = Equipo(75,"Estudiantes de la Plata",9,5)
Lanus = Equipo(73,"Lanus",14,5)
Independiente = Equipo(81,"Independiente",9,5)
Tomba = Equipo(73,"Godoy Cruz",14,5)
Boca = Equipo(78,"Boca Juniors",7,5)
Velez = Equipo(77,"Velez Sarfield",8,5) 
Colon = Equipo(76,"Colon",12,5)
Racing = Equipo(78,"Racing",5,5)
Gimnasia = Equipo(68,"Gimnasia y Esgrima de la Plata",11,4)
Rosario_Central = Equipo(72,"Rosario Central",14,4)
Defensa = Equipo(73,"Defensa y Justicia",9,4)
Argentinos = Equipo(74,"Argentinos Juniors",6,5)
Newells = Equipo(73,"Newell's Old Boys",15,4)
Atletico = Equipo(70,"Atletico Tucuman",13,4)
Patronato = Equipo(65,"Patronato",10,4)
Huracan = Equipo(67,"Huracan",6,5)
San_Lorenzo = Equipo(72,"San Lorenzo",11,4)
Sarmiento = Equipo(63,"Sarmiento de Junin",11,4)
Aldosivi = Equipo(63,"Aldosivi",19,4)
Platense = Equipo(62,"Platense",13,4)
Union = Equipo(63,"Union de Santafe",13,4)
Central_Cordoba = Equipo(62,"Central Cordoba",14,4)
Banfield = Equipo(65,"Banfield",10,4)
Arsenal = Equipo(61,"Arsenal de Sarandi",14,4)

E= [Tomba,Boca,Talleres,River,Estudiantes,Lanus,Independiente,Velez,Colon,Racing,Gimnasia,Rosario_Central,
Defensa,Argentinos,Newells,Atletico,Patronato,Huracan,San_Lorenzo,Sarmiento,Aldosivi,Platense,Union,Central_Cordoba,
Banfield,Arsenal]
Puntos = []
GF = []
GC = []
DG = []
for j in range (26):
	Puntos += [0]
	GF += [0]
	GC += [0]
	DG += [0]

def gol_local (pdg,pdd,pdc):
	global golL
	golL = 0
	for k in range (pdc):
		p=random.randint(0,100)
		b=random.randint(0,25)
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
for i in range (26):
	print(E[i].nombre,"en casa:")
	for c in range (26):
		l = 0
		v = 0
		if E[c].nombre != E[i].nombre:
			l = gol_local(E[i].pdg,E[c].pdd,E[i].pdc)
			v = gol_visita(E[c].pdg,E[i].pdd,E[c].pdc)
			print(E[i].nombre,l,":",v, E[c].nombre)
			if v < l:
				Puntos[i] = Puntos[i]+3
			elif v == l:
				Puntos[i] = Puntos[i]+1
				Puntos[c] = Puntos[c]+1
			elif v > l:
				Puntos[c] = Puntos[c]+3
	
Q = []
for i in range(26):
	E[i].puntos = Puntos[i]
	Q.append(Puntos[i])
	
S = sorted(E, key=lambda t: t.puntos, reverse=True)

def tabla():
	tabla_print = []
	print("El campeon es:", S[0])
	for E in S:
		
		tabla_print.append(E.nombre)
		tabla_print.append(E.puntos,)
	print(tabla_print)
	return(tabla_print)
tabla()
   
