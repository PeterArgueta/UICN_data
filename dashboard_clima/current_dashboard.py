import pandas as pd
from datetime import datetime




directory="dashboard_clima/outputhtml_current/"
# Cargar los datos desde el archivo CSV
df = pd.read_csv('salida_final.csv', delimiter=',', header=0)


df['datetime'] = df['date'] + ' ' + df[' time']

df['datetime'] = pd.to_datetime(df['datetime'])

today = datetime.today().strftime('%Y-%m-%d')

start_date = today + ' 00:00:00'
end_date = today + ' 23:59:59'

df = df[(df['datetime'] >= start_date) & (df['datetime'] < end_date)]

df['datetime'] = pd.to_datetime(df['datetime'], format="%Y-%m-%d %H:%M:%S")
df = df.sort_values("datetime")

#df[['Nombre']] = df[['Nombre']].replace('_', ' ', regex=True)
# Obtener el día más reciente
latest_date = df['datetime'].max()
df_latest = df[df['datetime'] == latest_date]
estaciones = df["estacion"].unique()
data=df.groupby(['estacion'])

df = df[df['datetime'] == latest_date]

""" 
data_estacion=data.get_group('LABOR OVALLE')
lluvia=data_estacion['lluvia'].iloc[0]
print(data_estacion)
print(lluvia)
 """


for estacion in estaciones:
        data_estacion=data.get_group(estacion)
        lluvia=str(data_estacion[' RainDaily'].iloc[-1])
        tmax=str(data_estacion[' AT_MAX'].iloc[-1])
        tseca=str(data_estacion[' AT'].iloc[-1])
        tmin=str(data_estacion[' AT_MIN'].iloc[-1])
        hum_rel=str(data_estacion[' RH'].iloc[-1])
   #     fecha=today.strftime("%Y-%m-%d %H:%M")
       

        html = '''

        <html>
        <head>
        <title>ESTACION</title>
        <style>
        body {
            font-family: Arial, sans-serif; color: #224f94;
        }
        
        h2 {
            margin-bottom: 10px;
        }
        
        table {
            border-collapse: collapse;
        }
        
        table th, table td {
            border: 1px solid rgb(3, 3, 233);
            padding: 8px;
        }
        
        button {
            padding: 6px 12px;
            background-color: #f5f5f5;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        </style>
        </head>
        <body>
        <h2>'''+estacion+'''</h2>
        <p>Actualizado '''''' -PRELIMINAR- </p>
        <table>
        <tr>
        <th>LLUVIA</th>
        <th>TMIN</th>
        <th>TMEDIA</th>
        <th>TMAX</th>
        </tr>
        <tr>
        <td>'''+lluvia+'''</td>
        <td>'''+tmin+'''</td>
        <td>'''+tseca+'''</td>
        <td>'''+tmax+'''</td>
        </tr>
        </table>
        <div style="margin-top: 20px;">
        <a href="https://insivumeh.gob.gt/img/Estaciones_Met/dashboard/output/'''+estacion+'''.html" target="_blank"><button>Todas las variables</button></a>
        </div>
        </body>
        </html>
            
        '''

    # Imprimir el código HTML

        with open(f'{directory}{estacion}.html', 'w') as f:
            f.write(html)
    

