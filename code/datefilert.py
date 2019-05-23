import pandas as pd
from datetime import datetime


outfile = 'DIvvy/Divvy_Stations_2013.csv'
df =pd.read_csv('DIvvy/Divvy_Stations_2017_Q1Q2.csv')
df.columns

'''
Index(['id', 'name', 'city', 'latitude', 'longitude', 'dpcapacity',
       'online_date'],
      dtype='object')
'''
## online_date  string convert to datetime
df['online_date'][1]

def convert(s):
    return datetime.strptime(s, '%m/%d/%Y %H:%M:%S')

df['date']= df['online_date'].apply(convert)

filter_date = '1/1/2014 00:00:00'
df_new = df[df['date'] <= datetime.strptime('1/1/2014 00:00:00', '%m/%d/%Y %H:%M:%S')]

df_new.to_csv(outfile)