import pandas as pd
import os 
import matplotlib.pyplot as plt
import datetime




path = 'CTA ridership/'
file = 'rail_station_entries.csv'


df = pd.read_csv(path+file)
print(df.columns)
'''
Index(['SERVICE_DATE', 'DAY_TYPE', 'SORT_ALL', 'LINE', 'BRANCH', 'STATION',
       'ENTRIES'],
      dtype='object')

'''
print(df.describe() )

df['SERVICE_DATE'][0].datetime.today().weekday()
df.head(10)

def day_check(weekno='12/31/2018'):
      weekno = datetime.datetime.today().weekday()
      if weekno<5:
            day =  "Weekday"
      else:
            day =  "Weekend"
      return day

df['day'] = day_check(df['SERVICE_DATE'])
# df['month_beginning'].unique()
df.loc[df['day']=='Weekend']
# date0 = df['month_beginning'].min()
# date1 = df['month_beginning'].max()

# print ('Data range: {}--{}'.format(date0,date1))

df_1stop = df.loc[df['stationame'] == 'Thorndale']
df_1stop = df_1stop.drop(columns=['station_id','monthtotal'])

# fig= plt.figure(figsize=(20,5))
# ax1 =  plt.subplots(1,1)

fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot()
plt.xlabel('Number of requests every 10 minutes')

# ax0 = df_1stop.plot(x='month_beginning',y='avg_weekday_rides'  ,label='month_beginning')
# ax1 = df_1stop.plot(x='month_beginning',y='avg_saturday_rides'  )

df_1stop.plot(kind= 'line', ax=ax )
plt.show()


