import folium
import os
import numpy as np
from folium import plugins
import webbrowser

print(folium.__version__)

print("="*20)

m = folium.Map([45, 3], zoom_start=4)

folium.Marker([45.01, 3.01], popup='여긴 어디').add_to(m)

m.save("map.html")

html_file='map.html'

webbrowser.open(html_file)

folium.Map().get_root().render()


#https://dailyheumsi.tistory.com/85
#folium 튜토리얼