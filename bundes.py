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

Bayern_Munich = Equipo(81,"Bayern Munich",10,5)
Borussia_Dortmund = Equipo(79,"Borussia Dortmund",9,5)
Bayer_Leverkusen = Equipo(80,"Bayer Leverkusen",8,5)
Leipzig = Equipo(77,"Leipzig",9,5)
Union_Berlín = Equipo(77,"Unión Berlín",11,5)
Friburgo = Equipo(75,"Friburgo",10,5)
Colonia = Equipo(75,"Colonia",11,5)
Mainz = Equipo(74,"	Mainz",12,5) 
Hoffenheim = Equipo(72,"Hoffenheim",12,5)
Borussia_Mönchengladbach = Equipo(76,"Borussia Mönchengladbach",9,5)
Eintracht = Equipo(76,"	Eintracht de Frankfurt",12,4)
Wolfsburgo = Equipo(73,"Wolfsburgo",11,4)
Bochum = Equipo(73,"Bochum",11,4)
Augsburgo = Equipo(69,"Augsburgo",12,4)
Stuttgart = Equipo(68,"Stuttgart",13,4)
Hertha = Equipo(66,"Hertha de Berlín",11,4)
Greuther_Fürth = Equipo(66,"Greuther Fürth",9,4)  
Bielefeld = Equipo(65,"	Bielefeld",13,4)


E= [Bayern_Munich,Borussia_Dortmund,Bayer_Leverkusen,Leipzig,Union_Berlín,
Friburgo,Colonia,Mainz,Hoffenheim,Borussia_Mönchengladbach,Eintracht,Wolfsburgo,Bochum,Augsburgo,Stuttgart,
Hertha,Greuther_Fürth,Bielefeld]
def simular():
	Puntos = []
	GF = []
	GC = []
	DG = []

	for j in range (18):
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
	for i in range (18):
		print(E[i].nombre,"en casa:")
		for c in range (18):
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
	for i in range(18):
		E[i].puntos = Puntos[i]
		Q.append(Puntos[i])
		
	S = sorted(E, key=lambda t: t.puntos, reverse=True)
	return S
def tabla():
	tabla_print = []
	print("El campeon es:", simular()[0])
	
	for E in simular():
		
		tabla_print.append(E.nombre)
		tabla_print.append(E.puntos)
	print(tabla_print)
	return(tabla_print)
   
def torneo_Bundes():
	simular()
	tabla()
	return tabla()
torneo_Bundes()
