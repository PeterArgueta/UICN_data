import pandas as pd

directory="monthly_data_by_station_csv/outputcsv/"
df = pd.read_csv('salida_final.csv', delimiter=',', header=0)

df['datetime'] = df['date'] + ' ' + df[' time']

df['datetime'] = pd.to_datetime(df['datetime'])

start_date = '2023-08-03 00:00:00'
end_date = '2023-08-03 23:59:00'

df = df[(df['datetime'] >= start_date) & (df['datetime'] < end_date)]


df = df.sort_values("datetime")

# Obtener la fecha más reciente en el dataframe
latest_date = df['datetime'].max()

# Obtener el primer día del último mes
thirty_days_ago = latest_date - pd.Timedelta(days=29)

# Filtrar los datos para que solo incluyan los de los últimos 30 días
last_30_days_data = df[df['datetime'] >= thirty_days_ago]
last_30_days_data = last_30_days_data.sort_values("datetime")


last_30_days_data[['estacion']] = last_30_days_data[['estacion']].replace('_', ' ', regex=True)
# Obtener la lista de estaciones disponibles en el dataframe
estaciones = last_30_days_data["estacion"].unique()

data=last_30_days_data.groupby(['estacion'])
 
for estacion in estaciones:
    # Filtrar los datos para la estación actual
    data_estacion=data.get_group(estacion)
    data_estacion = data_estacion.dropna(axis=1, how='all')
    data_estacion = data_estacion.drop(labels=['estacion'], axis=1)
    data_estacion = data_estacion.iloc[:, 1:]
    data_estacion = data_estacion.reset_index(drop=True)
    data_estacion.index += 1
    data_estacion=data_estacion.rename_axis("No.")
    data_estacion.to_csv(f"{directory}{estacion}.csv")

