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
from simulador import tabla
app = Flask(__name__)      
CORS(app)
tabla_var = tabla()
longitud = len(tabla_var)
key_list = []
value_list = []
for x in range(longitud):
    if x % 2 == 0:
      key_list.append(tabla_var[x])  
    else:
      value_list.append(tabla_var[x])
print(key_list)
tabla_front = dict(zip(key_list, value_list))
@app.route("/devolver") 
def devolver_tabla():
    return (tabla_front)

if __name__ == '__main__':
    app.run(debug=True, port=5000)