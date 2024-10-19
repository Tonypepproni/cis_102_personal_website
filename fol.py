import folium
import pandas as pd

df=pd.read_csv('static/info/parks.csv')

m = folium.Map(location=(39.50, -98.35), zoom_start=3, tiles="cartodb positron")

def iconMaker(color,icon,prefix):
    return folium.Icon(color=color,icon=icon,prefix=prefix)

def popupMaker(df,i):
    return df.iloc[i]['name']

for i in range(0,len(df)):
    if df.iloc[i]['type']=='NP':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
            popup=df.iloc[i]['name'], #creates a popup
            icon=iconMaker('green','tree','fa')#creates a marker with this style
        ).add_to(m)

    elif df.iloc[i]['type']=='NHP':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
            popup=df.iloc[i]['name'], #creates a popup
            icon=iconMaker('purple','landmark','fa')#creates a marker with this style
        ).add_to(m)
    elif df.iloc[i]['type']=='NPres':
        folium.Marker(
            location=[df.iloc[i]['lat'],df.iloc[i]['long']],#locates long and lat from the data frame and displays it
            popup=df.iloc[i]['name'], #creates a popup
            icon=iconMaker('red','binoculars','fa')#creates a marker with this style
        ).add_to(m)

m.save("static/footprint.html")