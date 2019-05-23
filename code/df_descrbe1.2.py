import pandas as pd
import os 
import matplotlib.pyplot as plt

path = 'CTA ridership/'
file = 'CTA_-_Ridership_-__L__Station_Entries_-_Monthly_Day-Type_Averages___Totals.csv'


df = pd.read_csv(path+file)
print(df.columns)
'''
Index(['station_id', 'stationame', 'month_beginning', 'avg_weekday_rides',
       'avg_saturday_rides', 'avg_sunday-holiday_rides', 'monthtotal'],
      dtype='object')

avg_sunday-holiday_rides  + avg_saturday_rides
vs
avg_weekday_rides

'''
print(df.describe() )

# df[df['station_id']==41450]
df.head(10)


# df['month_beginning'].unique()

# date0 = df['month_beginning'].min()
# date1 = df['month_beginning'].max()

# print ('Data range: {}--{}'.format(date0,date1))

df_1stop = df.loc[df['stationame'] == 'Thorndale']
df_1stop = df_1stop.drop(columns=['station_id','monthtotal'])

# fig= plt.figure(figsize=(20,5))
# ax1 =  plt.subplots(1,1)

fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot()

# ax0 = df_1stop.plot(x='month_beginning',y='avg_weekday_rides'  ,label='month_beginning')
# ax0 = df_1stop.plot(x='month_beginning',y='avg_weekday_rides'  ,label='month_beginning')
# ax1 = df_1stop.plot(x='month_beginning',y='avg_saturday_rides'  )
x = df_1stop.month_beginning

df.plot(x='month_beginning',y='avg_weekday_rides', kind= 'line', ax=ax ,xticks= 'month_beginning')
plt.show()


