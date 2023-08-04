import pandas as pd

df=pd.read_csv('salida_final.csv')


df['datetime'] = df['date'] + ' ' + df[' time']

df['datetime'] = pd.to_datetime(df['datetime'])

start_date = '2023-08-03 00:00:00'
end_date = '2023-08-03 23:59:00'

filtered_df = df[(df['datetime'] >= start_date) & (df['datetime'] < end_date)]

print(filtered_df)