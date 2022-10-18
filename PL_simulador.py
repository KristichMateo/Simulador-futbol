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


E= [Manchester_City,Liverpool,Chelsea,Tottenham,Leicester_City,West_Ham,Man_Utd, Aston_Villa,Crystal_palace,
Brentford,Newcastle,Everton,Southampton,Leeds,Brighton,Wolverhampton,Burnley,Watford,Norwich_City,Arsenal_eng]
def simular():
	Puntos = []
	GF = []
	GC = []
	DG = []

	for j in range (20):
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
	for i in range (20):
		print(E[i].nombre,"en casa:")
		for c in range (20):
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
	for i in range(20):
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
   
def torneo_PL():
	simular()
	tabla()
	return tabla()
torneo_PL()
