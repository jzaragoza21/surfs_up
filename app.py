# ----- Import  dependencies -----
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# ----- Set up the Database -----
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# ----- Set up Flask -----
app = Flask(__name__)

#"Instance" is a general term in programming to refer to a singular version of something
#The __name__ variable denotes the name of the function
#Variables with underscores before and after them are called magic methods in Python

#Define the stating point or root
#The foward slash denotates tht we we want to put our data at the root of our routes
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
#When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route.
#This convention signifies that this is version 1 of our application.

# ----- Precipation Route -----
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
