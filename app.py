from asyncio.windows_events import NULL
import json
from operator import mod
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from email.policy import default
from enum import unique
import flask

from flask_cors import CORS

from champions import simular
from bundes import torneo_Bundes
from PL_simulador import torneo_PL
from simulador_LPF import torneo
from mundial import simular_qatar
app = Flask(__name__)      
CORS(app)

@app.route("/bundes")        #Bundes
def Bundes():
    nombres = []
    puntos = []
    tabla = torneo_Bundes()
    for i in range(len(tabla)):
        if i % 2 == 0:
            nombres.append(tabla[i])
        else:
            puntos.append(tabla[i])
    msg = {
        "nombre":nombres,
        "puntos":puntos
    }
    return msg

@app.route("/premier")        #premier
def premier():
    nombres = []
    puntos = []
    tabla = torneo_PL()
    for i in range(len(tabla)):
        if i % 2 == 0:
            nombres.append(tabla[i])
        else:
            puntos.append(tabla[i])
    msg = {
        "nombre":nombres,
        "puntos":puntos
    }
    return msg
@app.route("/devolver")        #lpf
def lpf():
    nombres = []
    puntos = []
    tabla = torneo()
    for i in range(len(tabla)):
        if i % 2 == 0:
            nombres.append(tabla[i])
        else:
            puntos.append(tabla[i])
    msg = {
        "nombre":nombres,
        "puntos":puntos
    }
    return msg
@app.route("/champions")        #Champion League
def champions():
    respuesta = simular()
    return respuesta
@app.route("/mundial")
def mundial():
    respuesta = simular_qatar()
    return respuesta
if __name__ == '__main__':
    app.run(debug=True, port=5000)