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

from prueba import simular

app = Flask(__name__)      
CORS(app)



@app.route("/champions")        #Champion League
def champions():
    


    respuesta = simular()
    return respuesta
if __name__ == '__main__':
    app.run(debug=True, port=5000)