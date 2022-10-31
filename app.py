from asyncio.windows_events import NULL
import json
from operator import mod
from pyexpat import model
from unicodedata import name
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from email.policy import default
from enum import unique
import flask
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from flask_cors import CORS
from simulador_LPF import torneo
from PL_simulador import torneo_PL
from bundes import torneo_Bundes
from champions import Octavos_json, simular_grupos,simular_octavos,simular_cuartos,simular_semis,simular_final,champions_simular

app = Flask(__name__)      
CORS(app)


@app.route("/devolver") 
def devolver_tabla():
    print("se ejecuta?")
    torneo()
    tabla_var = torneo()
    longitud = len(tabla_var)
    key_list = ["nombre","puntos"]
    equipos = []
    puntos = []
    for x in range(longitud):
        if x % 2 == 0:
            equipos.append(tabla_var[x])  
        else:
            puntos.append(tabla_var[x])
    value_list = []
    value_list.append(equipos) 
    value_list.append(puntos)
    tabla_front = dict(zip(key_list, value_list))
    return (tabla_front)
@app.route("/premier") 
def premier():
    print("se ejecuta?")
    torneo_PL()
    tabla_var = torneo_PL()
    longitud = len(tabla_var)
    key_list = ["nombre","puntos"]
    equipos = []
    puntos = []
    for x in range(longitud):
        if x % 2 == 0:
            equipos.append(tabla_var[x])  
        else:
            puntos.append(tabla_var[x])
    value_list = []
    value_list.append(equipos) 
    value_list.append(puntos)
    tabla_front = dict(zip(key_list, value_list))
    return (tabla_front)
@app.route("/bundes") 
def bundes():
    print("se ejecuta?")
    torneo_PL()
    tabla_var = torneo_Bundes()
    longitud = len(tabla_var)
    key_list = ["nombre","puntos"]
    equipos = []
    puntos = []
    for x in range(longitud):
        if x % 2 == 0:
            equipos.append(tabla_var[x])  
        else:
            puntos.append(tabla_var[x])
    value_list = []
    value_list.append(equipos) 
    value_list.append(puntos)
    tabla_front = dict(zip(key_list, value_list))
    return (tabla_front)
@app.route("/champions")        #Champion League
def champions():
    champions_simular
    grupos = simular_grupos()
    octavos = simular_octavos()
    cuartos = simular_cuartos()
    semis = simular_semis()
    final = simular_final()

    json.dumps(octavos)
    print("dddddddddddddddd",type(octavos))

    respuesta = {
        "grupos":grupos,
        "octavos":octavos,
        "cuartos":cuartos,
        "semis":semis,
        "final":final
    }
    return respuesta
if __name__ == '__main__':
    app.run(debug=True, port=5000)