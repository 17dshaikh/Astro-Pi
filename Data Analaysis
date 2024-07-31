import sys
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.interpolate import UnivariateSpline
import plotly.express as px
import matplotlib.pyplot as plt
import geopy.distance
import os
import time

#E:\AstroPi\Data\HHorizon\HHorizon\data.csv

def menu(location):
    data = pd.read_csv(location)
    Longitude = data.ISSLongitude
    Latitude = data.ISSLatitude
    Elevation = data.ISSElevation
    Magnetometer = data.MagMagnitude
    MagX = data.MagX
    MagY = data.MagY
    MagZ = data.MagZ
    DateTime = data.DateTime
    os.system("cls")
    print("--------------------------------MENU------------------------------------")
    print("1) Plot graph of raw magnetic field strength against distance travelled")
    print("2) Plot map of Astro Pi path with elevation shading")
    print("3) Get distance travelled of the ISS from longitude and latitude")
    print("4) Create univariate interpolated spline of raw data and plot graph")
    print("5) Overlay univariate interpolated spline and raw data ")
    print("6) Plot graph of elevation against time")
    print("7) Plot magnetic field strength against time")
    print("8) Plot magnetic field strength in 3D")
    print("9) End program")
    UserChoice = input("Enter your choice: ")
    if UserChoice == "1":
        option1(Magnetometer,location)
    elif UserChoice == "2":
        option2(Longitude, Latitude, location,Elevation)
    elif UserChoice == "3":
        option3(Latitude, Longitude, location)
    elif UserChoice == "4":
        option4(Magnetometer, location)
    elif UserChoice == "5":
        option5(Magnetometer, location)
    elif UserChoice == "6":
        option6(Elevation, DateTime, location)
    elif UserChoice == "7":
        option7(DateTime,Magnetometer, location)
    elif UserChoice == "8":
        option8(MagX,MagY,MagZ,location)
    elif UserChoice == "9":
        sys.exit()


def option1(Magnetometer,Location):
    data = pd.read_csv(location)
    DistanceTravelled = data.DistanceTravelled
    plt.plot(DistanceTravelled, Magnetometer, label="Raw Data")
    plt.xlabel("Distance Travelled / 1000 km")
    plt.ylabel("Magnetic Field Strength / T")
    plt.legend()
    plt.show()
    menu(Location)


def option2(Longitude, Latitude,Location,Elevation):
    data = pd.read_csv(location)
    fig = px.scatter_geo(data,lat="ISSLatitude",lon="ISSLongitude",color="ISSElevation",color_continuous_scale="plasma")
    fig.update_layout(title = 'Astro Pi Path around the world', title_x=0.5)
    fig.show()
    menu(Location)

def option3(Latitude, Longitude,Location):
    Distance = 0
    for i in range(1, len(Longitude)):
        Distance = (Distance + geopy.distance.geodesic((Latitude[i - 1], Longitude[i - 1]),(Latitude[i], Longitude[i])).km)
    print("Distance travelled by the ISS in the duration of our experiment was " + str(Distance) + "km")
    time.sleep(5)
    menu(Location)

def option4(Magnetometer,Location):
    data = pd.read_csv(location)
    DistanceTravelled = data.DistanceTravelled
    spl = UnivariateSpline(DistanceTravelled, Magnetometer, k=5)
    xs = np.linspace(0, 182, 1000)
    plt.xlabel("Distance Travelled / 1000 km")
    plt.ylabel("Magnetic Field Strength / T")
    plt.plot(xs, spl(xs), label="Fitted Line")
    plt.legend()
    plt.show()
    menu(Location)

def option5(Magnetometer, Location):
    data = pd.read_csv(location)
    DistanceTravelled = data.DistanceTravelled
    spl = UnivariateSpline(DistanceTravelled, Magnetometer, k=5)
    xs = np.linspace(0, 182, 1000)
    plt.xlabel("Distance Travelled / 1000 km")
    plt.ylabel("Magnetic Field Strength / T")
    plt.plot(DistanceTravelled,Magnetometer,label = "Raw Data")
    plt.plot(xs, spl(xs), label="Fitted Line")
    plt.legend()
    plt.show()
    menu(Location)

def option6(Elevation, DateTime,Location):
    fig = px.scatter(y=Elevation,x=DateTime,title="Elevation agaisnt Time")
    fig.show()
    menu(Location)


def option7(DateTime, MagneticFieldStrength,Location):
    fig = px.scatter(y=MagneticFieldStrength,x=DateTime,title="Magnetic Field Strength agaisnt Time")
    fig.show()
    menu(Location)

def option8(MagX, MagY, MagZ, Location):
    marker_data = go.Scatter3d(
        x=MagX,
        y=MagY,
        z=MagZ,
        marker=go.scatter3d.Marker(size=3),
        opacity=0.8,
        mode='markers'
    )
    fig = go.Figure(data=marker_data)
    fig.update_layout(scene=dict(
        xaxis_title='Magnetometer X',
        yaxis_title='Magnetometer Y',
        zaxis_title='Magnetometer Z'),
        width=700,
        margin=dict(r=20, b=10, l=10, t=10))
    fig.show()
    menu(Location)

location = input("Enter location of csv file: ")
#location = "E:\AstroPi\Data\HHorizon\HHorizon\data.csv"
menu(location)
