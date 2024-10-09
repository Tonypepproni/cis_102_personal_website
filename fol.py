import folium
import pandas as pd

df=pd.read_csv('static/info/parks.csv')

m = folium.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron")

for i in range(0,len(df)):
    if df.iloc[i]['type']=='NP':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
            popup=df.iloc[i]['name'], #creates a popup
            icon=folium.Icon(color='green',icon='tree', prefix='fa')#creates a marker with this style
        ).add_to(m)

    elif df.iloc[i]['type']=='NHP':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
            popup=df.iloc[i]['name'], #creates a popup
            icon=folium.Icon(color='purple',icon='landmark', prefix='fa')#creates a marker with this style
        ).add_to(m)
    elif df.iloc[i]['type']=='NPres':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
            popup=df.iloc[i]['name'], #creates a popup
            icon=folium.Icon(color='red',icon='binoculars', prefix='fa')#creates a marker with this style
        ).add_to(m)

m.save("footprint.html")