import functools
import streamlit as st
import pandas as pd 
import numpy as np
from streamlit_folium import st_folium
import folium
import math 

st.set_page_config(layout="wide")
st.title("Around the world in 80 days")

df = pd.read_csv("dataset2.csv")
df = df[["Place", "Lat", "Long"]].values.tolist()

locationMap = folium.Map(location=[0,0], zoom_start=2)

# for idx, coord in enumerate(df):
#     popup = folium.Popup(f"City: {coord[0]}",
#                   max_width = 250)
#     folium.Marker(location=[coord[1], coord[2]], popup=popup, icon=folium.Icon(color="purple")).add_to(locationMap)
#     # print(idx, coord)
#     if idx % 2 != 0:
#         folium.PolyLine([coord[1], coord[2]], []).add_to(locationMap)


def calculateDistance(lat1, lon1, lat2, lon2, unit):
    radlat1 = math.pi * lat1/180
    radlat2 = math.pi * lat2/180
    radlon1 = math.pi * lon1/180
    radlon2 = math.pi * lon2/180
    theta = lon1-lon2
    radtheta = math.pi * theta/180
    dist = math.sin(radlat1) * math.sin(radlat2) + math.cos(radlat1) * math.cos(radlat2) * math.cos(radtheta);
    dist = math.acos(dist)
    dist = dist * 180/math.pi
    dist = dist * 60 * 1.1515
    if (unit=="K"): 
        dist = dist * 1.609344 
    if (unit=="N"):
        dist = dist * 0.8684 
    return dist

for i in range(len(df)): 
    popup = folium.Popup(f"City: {df[i][0]}", max_width = 250)
    folium.Marker(location=df[i][1: ], popup=popup, icon=folium.Icon(color="purple")).add_to(locationMap)
    # if i != 0: 
    #     cur = df[i-1][1: ]
    #     nex = df[i][1: ]
    #     latAndLong.append([cur[0], cur[1], nex[0], nex[1]])

latAndLong = list({})

for val in df: 
    latAndLong.append({"lat": val[1], "lon": val[2]})

for i in range(len(latAndLong)):
    latAndLong[i]["distance"] = calculateDistance(latAndLong[0]["lat"], latAndLong[0]["lon"], latAndLong[i]["lat"], latAndLong[i]["lon"], "N")

def customSort(a,b): 
    return a["distance"] - b["distance"]
cmp = functools.cmp_to_key(customSort)

latAndLong.sort(key=cmp)

uniqueNodes = []
for val in latAndLong:
    uniqueNodes.append([val["lat"], val["lon"]])

folium.PolyLine(uniqueNodes).add_to(locationMap)

# folium.PolyLine(([-21.0244816,27.5147504], [35.1820319,35.9449068])).add_to(locationMap)
# folium.PolyLine(([35.1820319,35.9449068], [48.5536972,-109.677802])).add_to(locationMap)


st_folium(locationMap, key="Fig", width=1800, height=900)



