# import plotly.express as px
# import pandas as pd

# df = pd.read_csv("dataset.csv")

# df.dropna(
#     axis=0,
#     how='any',
#     subset=None,
#     inplace=True
# )

# color_scale = [(0, 'orange'), (1,'red')]

# fig = px.scatter_mapbox(df, 
#                         lat="Lat", 
#                         lon="Long", 
#                         hover_name="Address", 
#                         hover_data=["Address", "Listed"],
#                         color="Listed",
#                         color_continuous_scale=color_scale,
#                         size="Listed",
#                         zoom=8, 
#                         height=800,
#                         width=800)

# fig.update_layout(mapbox_style="open-street-map")
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.write_html('first_figure.html', auto_open=True)

# Address,Lat,Long,Listed
# Address #1,-33.941,18.467,1250000
# Address #2,-33.942,18.468,1900000
# Address #3,-33.941,18.467,1200000
# Address #4,-33.936,18.467,1195000
# Address #5,-33.944,18.470,2400000


# import folium

# m = folium.Map(location=[11.5577494,43.1404894], zoom_start=10)

# folium.Marker(
#     location=[11.5577494,43.1404894],
#     popup="The Red Sea",
# ).add_to(m)

# m.save("first_figure.html")


import folium
import pandas as pd

df = pd.read_csv("dataset.csv")

coords = df[["Place", "Lat", "Long"]].values.tolist()
locationMap = folium.Map(location=[0,0], zoom_start=2)

for idx, coord in enumerate(coords):
    locationMap.add_child(folium.Marker(location=[coord[1], coord[2]], popup=coord[0], icon=folium.Icon(color="purple")))
    # if idx == 0:
    #     locationMap = folium.Map(location=[coord[1], coord[2]], zoom_start=10)
    # else: 
    #     locationMap.add_child(folium.Marker(location=[coord[1], coord[2]], popup=coord[0], icon=folium.Icon(color="purple")))

locationMap.save("first_figure.html")