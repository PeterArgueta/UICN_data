import pandas as pd

directory="outputhtml_current/"
# Cargar los datos desde el archivo CSV
df = pd.read_csv('database.csv', delimiter=',', header=0)
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')
df = df.sort_values("fecha")

df[['Nombre']] = df[['Nombre']].replace('_', ' ', regex=True)
# Obtener el día más reciente
latest_date = df['fecha'].max()
df_latest = df[df['fecha'] == latest_date]
estaciones = df["Nombre"].unique()
data=df.groupby(['Nombre'])


for estacion in estaciones:
        data_estacion=data.get_group(estacion)
        lluvia=str(data_estacion['lluvia'].iloc[0])
        tmax=str(data_estacion['tmax'].iloc[0])
        tseca=str(data_estacion['tseca'].iloc[0])
        tmin=str(data_estacion['tmin'].iloc[0])
        hum_rel=str(data_estacion['hum_rel'].iloc[0])
        fecha=latest_date.strftime("%Y-%m-%d")
       

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
        <p>Datos del '''+fecha+'''</p>
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
        <a href="http://172.20.0.56/pages/dashboard/output/'''+estacion+'''.html" target="_blank"><button>Todas las variables</button></a>
        </div>
        </body>
        </html>
            
        '''

    # Imprimir el código HTML

        with open(f'{directory}{estacion}.html', 'w') as f:
            f.write(html)
    


