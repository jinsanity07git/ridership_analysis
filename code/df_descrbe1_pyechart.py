import pandas as pd
import os 
import matplotlib.pyplot as plt

path = 'CTA ridership/'
file = 'CTA_-_Ridership_-__L__Station_Entries_-_Monthly_Day-Type_Averages___Totals.csv'


df = pd.read_csv(path+file, index_col='month_beginning')
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
sta_id =40080
df[df['station_id']==sta_id]
df.head(10)


# df['month_beginning'].unique()

# date0 = df['month_beginning'].min()
# date1 = df['month_beginning'].max()

# print ('Data range: {}--{}'.format(date0,date1))
Sta_name = df[df['station_id']==sta_id]['stationame'][0]

df_1stop = df.loc[df['stationame'] == Sta_name]
df_1stop = df_1stop.drop(columns=['station_id','monthtotal'])

# fig, ax = plt.subplots()

fig = plt.figure()
ax = fig.add_subplot(111)
# ax = fig.add_subplot()


# ax0 = df_1stop.plot(x='month_beginning',y='avg_weekday_rides'  ,label='month_beginning')
# ax1 = df_1stop.plot(x='month_beginning',y='avg_saturday_rides'  )
ls= list(df_1stop.index)
df_1stop.plot(kind= 'line', ax=ax  ,figsize=(20,8))

ax.get_xticks()

# ax.set_xlabel('stationame')
# # df_1stop.index
# ax.set_xticklabels(df_1stop.index)
# [n if i%5==0 else  for i,n in enumerate(df_1stop.index)  ]

# [x if x % 2 else x * 100 for x in range(1, 10) ]

ls2= []
for i,n in enumerate(df_1stop.index):
     if int(i)%10==0:
           ls2.append(n)

fig.get_facecolor()

ax.set_title(Sta_name)
           
ax.set_xticks([i for i in range(0,215,10)])
ax.set_xticklabels(ls2, rotation = 60, ha="right")
# plt.show()
try:
      fig.savefig(Sta_name)
except FileNotFoundError:
      fig.savefig('Sta_name')