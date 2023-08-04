import pandas as pd
from datetime import datetime

df=pd.read_csv('salida_final.csv')


df['datetime'] = df['date'] + ' ' + df[' time']

df['datetime'] = pd.to_datetime(df['datetime'])

today = datetime.today().strftime('%Y-%m-%d')

start_date = today + ' 00:00:00'
end_date = today + ' 23:59:59'


filtered_df = df[(df['datetime'] >= start_date) & (df['datetime'] < end_date)]

print(filtered_df)