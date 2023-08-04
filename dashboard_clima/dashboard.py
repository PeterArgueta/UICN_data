
import pandas as pd


directory="outputhtml/"
df = pd.read_csv('database.csv', delimiter=',', header=0)
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')
df = df.sort_values("fecha")

df[['Nombre']] = df[['Nombre']].replace('_', ' ', regex=True)

latest_date = df['fecha'].max()
df_latest = df[df['fecha'] == latest_date]
estaciones = df["Nombre"].unique()
data=df.groupby(['Nombre'])
df = df[df['fecha'] == latest_date]
# data_estacion=data.get_group('LABOR OVALLE')
# lluvia=data_estacion['lluvia'].iloc[-1]

for estacion in estaciones:
        data_estacion=data.get_group(estacion)
        lluvia=str(data_estacion['lluvia'].iloc[-1])
        tmax=str(data_estacion['tmax'].iloc[-1])
        tseca=str(data_estacion['tseca'].iloc[-1])
        tmin=str(data_estacion['tmin'].iloc[-1])
        eva_tan=str(data_estacion['eva_tan'].iloc[-1])
        hum_rel=str(data_estacion['hum_rel'].iloc[-1])
        bri_solar=str(data_estacion['bri_solar'].iloc[-1])
        nub=str(data_estacion['nub'].iloc[-1])
        vel_viento=str(data_estacion['vel_viento'].iloc[-1])
        dir_vient=str(data_estacion['dir_viento'].iloc[-1])
        pre_atmos=str(data_estacion['pre_atmos'].iloc[-1])
        rad_solar=str(data_estacion['rad_solar'].iloc[-1])

        html = '''
            <!DOCTYPE html>
            <meta http-equiv="content-type" content="text/html;charset=utf-8"/>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <html>
            <head>
                <title>ESTACIÓN '''+estacion+'''</title>
                <style type="text/css">
                    body {font-family: Arial, sans-serif;margin: 0;padding: 0;}
                    header {background-color: #117ce7;color: white;padding: 20px;text-align: center;}
                    h1 {margin: 0;}
                    .container {display: grid;grid-template-columns: repeat(4, 1fr);grid-gap: 20px;margin: 20px;}
                    .card {background-color: white;border: 1px solid #ccc;border-radius: 5px;box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);padding: 10px;}
                    .card h2 {margin-top: 0;font-size: 1em;}
                    .card p {margin-bottom: 0;}
                    .card .value {font-size: 1.5em;font-weight: bold;margin-bottom: 5px;}
                    .card .label {font-size: 0.8em;margin-bottom: 2px;}
                    .button {
                    background-color: #117ce7;
                    border: none;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                    }

     body {
            font-family: Arial, sans-serif;
        }
        
        h2 {
            margin-bottom: 10px;
        }
        
        table {
            border-collapse: collapse;
        }
        
        table th, table td {
            border: 1px solid black;
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
                <header><h1>ESTACIÓN '''+estacion+ '''. DATOS PRELIMINARES.</h1></header>
                <div class="container">
                    <div class="card"><h2>Precipitación</h2><p class="value">'''+lluvia+ '''mm</p><p class="label">Últimas 24 horas</p></div>
                    <div class="card"><h2>Temperatura Mínima</h2><p class="value">'''+tmin+ ''' °C</p><p class="label">Hoy</p></div>
                    <div class="card"><h2>Temperatura Media</h2><p class="value">'''+tseca+ ''' °C</p><p class="label">Hoy</p></div>
                    <div class="card"><h2>Temperatura Máxima</h2><p class="value">'''+tmax+ ''' °C</p><p class="label">Hoy</p></div>
                    <div class="card"><h2>Evaporación de Tanque</h2><p class="value">'''+eva_tan+ ''' mm</p><p class="label">Últimas 24 horas</p></div>
                    <div class="card"><h2>Humedad Relativa</h2><p class="value">'''+hum_rel+ '''%</p><p class="label">Hoy</p></div>
                    <div class="card"><h2>Brillo Solar</h2><p class="value"> '''+bri_solar+ ''' horas</p><p class="label">Hoy</p></div>
                    <div class="card"><h2>Velocidad del Viento</h2><p class="value"> '''+vel_viento+ ''' km/h</p><p class="label">Hoy</p></div>
                    <div class="card"><h2>Dirección del Viento</h2><p class="value">'''+dir_vient+ ''' °</p><p class="label">Hoy</p></div>
                    <div class="card"><h2>Presión Atmosférica</h2><p class="value">'''+pre_atmos+ ''' mb</p><p class="label">Hoy</p></div>
                    <div class="card"><h2>Radiación Solar</h2><p class="value">'''+rad_solar+ ''' </p><p class="label">Hoy</p></div>
                </div>
                <a href="https://insivumeh.gob.gt/img/Estaciones_Met/csvpage/'''+estacion+'''.html" target="_blank" class="button">Datos Mensuales</a>
            </body>
            </html>
        '''

    # Imprimir el código HTML

        with open(f'{directory}{estacion}.html', 'w') as f:
            f.write(html)
    





