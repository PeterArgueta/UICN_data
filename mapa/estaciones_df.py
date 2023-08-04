#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:40:55 2023

@author: rainy
"""
import folium
import random
import pandas as pd
import branca
from folium.plugins import FloatImage
from folium.plugins import MarkerCluster, MiniMap, MousePosition, MeasureControl, Geocoder, FloatImage, LocateControl

#Define coordinates of where we want to center our map
boulder_coords = [15.8, -90.5]
my_map = folium.Map(location = boulder_coords, zoom_start = 8, control_scale=True)
#my_map = folium.Map(location = boulder_coords, zoom_start = 8, tiles="Stamen Terrain", control_scale=True)


loc = 'INFORMACIÓN PRELIMINAR DE LAS ESTACIONES SUTRON -ALTIPLANO RESILIENTE - Departamento de Investigación y Servicios Meteorológicos - INSIVUMEH'
title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(loc)   


marker_cluster = MarkerCluster(name="Estaciones Automáticas").add_to(my_map)

#### Enlaces ####
regiones_clima='https://raw.githubusercontent.com/PeterArgueta/clima/main/rc.geojson'
departamentos='https://raw.githubusercontent.com/PeterArgueta/clima/main/deptos_gt.geojson'
belice='mapa/data/Belice.geojson'

#### Style ####
style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1,
                            'weight':0.1}


style_function2 = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1,
                            'weight':1,
                            "dashArray": "5, 5"}


def random_color(feature):
    return {'fillColor': f"#{random.randint(0, 0xFFFFFF):06x}", 'color': '#000000',
                            'fillOpacity': 0.4,
                            'weight':0.8}



#### Highlight ####

highlight_function = lambda x: {'fillColor': '#e78829', 
                                'color':'#000000', 
                                'fillOpacity': 0.5, 
                                'weight': 0.8}

#### REGIONES CLIMATICAS ####
R=folium.GeoJson(
    regiones_clima, name="Regiones Climáticas",
    style_function=style_function,
    highlight_function=random_color,
    show=(True), embed=True,
    tooltip=folium.features.GeoJsonTooltip(
        fields=['NOMBRE'],  # use fields from the json file
        aliases=[''],
        style=("background-color: white; color: #000000; font-family: arial; font-size: 12px; padding: 10px;") 
    ), 
).add_to(my_map)

folium.GeoJson(
    departamentos, name="Departamentos",
    style_function=style_function2,
    show=(True)
).add_to(my_map)

folium.GeoJson(
    belice, name="Diferendo Territorial y Marítimo",
    style_function=style_function2,
    show=(True),
    tooltip=folium.features.GeoJsonTooltip(
        fields=['Nombre'],  # use fields from the json file
        aliases=[''],
        style=("background-color: white; color: #000000; font-family: arial; font-size: 12px; padding: 10px;") 
    )
).add_to(my_map)

######################################
#### Data frame ####


df_auto=(pd.read_csv('mapa/data/automaticas.csv').dropna(subset=["Latitude","Longitude"]))
df_auto['Tipo']='automática'

#Se concatenan los 3 data frame para trabajar sólo con uno. 
#df=pd.concat([df_sino,df_auto,df_conv])

df=pd.concat([df_auto])

####HTML###

def html_chilera(row):
    i = row
    
    Estación = df['Estación'].iloc[i]                             
    #Departamento = df['Departamento'].iloc[i]                           
    #Municipio = df['Municipio'].iloc[i]
    #ID = df['Código'].iloc[i]                 
    Latitude=str(round(df['Latitude'].iloc[i],6))   
    Longitude=str(round(df['Longitude'].iloc[i],6))
    
    html = """<!DOCTYPE html>
      <html>
      <head>
      <meta charset="UTF-8">
      <style>

      /* Estilo de botones de pestañas */
      .tab button {
      background-color: #f2f2f2;
      border: none;
      outline: none;
      cursor: pointer;
      padding: 10px 20px;
      transition: 0.3s;
      font-size: 18px;
      }

      /* Cambio de color de fondo al pasar el mouse */
      .tab button:hover {
      background-color: #ddd;
      }

      /* Estilo de botones activos */
      .tab button.active {
      background-color: #ccc;
      }

      /* Estilo del contenido de pestañas */
      .tabcontent {
      display: none;
      padding: 10px;
      }

      /* Mostrar el contenido de la pestaña activa */
      .tabcontent.active {
      display: block;
      }


      body {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        font-size: 10px;
        color: #333;
        background-color: #f2f2f2;
      }

      h1 {
        font-size: 20px;
        font-weight: bold;
        margin: 10px;
        color: #224f94;
      }

      hr {
        margin: 20px;
        border: none;
        height: 1px;
        background-color: #d4d4d4;
      }

      p {
        margin: 20px;
        line-height: 1.6em;
      }

      a {
        color: #224f94;
        e font-weight: bold;
        text-decoration: none;
      }

      a:hover {
        color: #1a3d73;
        text-decoration: underline;
      }


      </style>
      <title>iframe</title>
      <link rel="stylesheet" href=/home/rainy/Documents/Rutinas/mapas/iframe/style.css" />
      </head>



      <body>
      <div class="tab">
      <button class="tablinks active" onclick="openTab(event, 'estacion')">Estación</button>
      <button class="tablinks" onclick="openTab(event, 'variables')">Variables</button>
      <button class="tablinks" onclick="openTab(event, 'contact')">Precipitación</button>
      </div>

      <div id="estacion" class="tabcontent active">

      <h1>"""  + Estación + """</h1>
      <p><strong>ID: </strong><a href="https://insivumeh.gob.gt/img/Estaciones_Met/dashboard/output/"""""".html" target="_blank">""""""</a></p>
      <p><strong>Ubicación: </strong><span>Lat: """ + Latitude + """, Lon: """ + Longitude + """</span></p>
      <p><strong>"""""", """"""</span></p>

      </div>

      <div id="variables" class="tabcontent">
       <iframe src="https://insivumeh.gob.gt/img/Estaciones_Met/dashboard/output_current/"""""".html" frameborder="0" width="100%" height="400px"></iframe>
      </div>

      <div id="contact" class="tabcontent">
       <a href="https://insivumeh.gob.gt/img/Estaciones_Met/stationsmap/""" """.html"   target="_blank">
       <img src="https://raw.githubusercontent.com/Climatologia-INSIVUMEH/graph_generator_monthly/main/output/img_output/""" """.png" alt="graph" width="430" height="250"> 
       </a>
      </div>

      <script>

      function openTab(evt, tabName) {
      // Obtener elementos con la clase "tabcontent" y ocultarlos
      var tabcontent = document.getElementsByClassName("tabcontent");
      for (var i = 0; i < tabcontent.length; i++) {
      tabcontent[i].classList.remove("active");
      }

      // Obtener elementos con la clase "tablinks" y quitar la clase "active"
      var tablinks = document.getElementsByClassName("tablinks");
      for (var i = 0; i < tablinks.length; i++) {
      tablinks[i].classList.remove("active");
      }

      // Mostrar la pestaña actual y marcar el botón como activo
      document.getElementById(tabName).classList.add("active");
      evt.currentTarget.classList.add("active");
      }

      </script>
      </body>
      </html>

      """
    return html



def icono_chilero(row):
    i=row
    
    Tipo=df['Tipo'].iloc[i]
    
    html="""<!DOCTYPE html>
    <html>

   ''<img src="https://github.com/PeterArgueta/clima/raw/main/"""+Tipo +""".svg" style="width:35px;height:35px;">'

    </html>
    """ 
    return html


for i in range(0,len(df)):
    html = html_chilera(i)
    icono= icono_chilero(i)
    iframe = branca.element.IFrame(html=html,width=450,height=300)
    popup = folium.Popup(iframe,parse_html=True)
    folium.Marker([df['Latitude'].iloc[i],df['Longitude'].iloc[i]],
                  popup=popup, icon=folium.DivIcon(icono)).add_to(marker_cluster) 

        
logo = ("https://raw.githubusercontent.com/PeterArgueta/clima/main/logo.png")


FloatImage(logo, bottom=5, left=1, width='80px').add_to(my_map)



folium.LayerControl(position="topright").add_to(my_map)
my_map.keep_in_front(R)


MousePosition( 
    position='bottomright', 
    separator=' | ', 
    prefix="Mouse:", 
    num_digits=3, 
    #lat_formatter=fmtr, 
    #lng_formatter=fmtr 
).add_to(my_map) 

LocateControl().add_to(my_map)
#Geocoder().add_to(my_map)
my_map.get_root().html.add_child(folium.Element(title_html))

my_map.save("index.html")

