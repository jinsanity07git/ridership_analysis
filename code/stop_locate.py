
import pandas as pd
import os 
import matplotlib.pyplot as plt

path = 'CTA ridership/'
file = 'CTA_-_System_Information_-_List_of__L__Stops.csv'
outfile = 'GIS/CTA_stop.csv'
df= pd.read_csv(path+file)

df.columns
'''
Index(['STOP_ID', 'DIRECTION_ID', 'STOP_NAME', 'STATION_NAME',
       'STATION_DESCRIPTIVE_NAME', 'MAP_ID', 'ADA', 'RED', 'BLUE', 'G', 'BRN',
       'P', 'Pexp', 'Y', 'Pnk', 'O', 'Location', 'Historical Wards 2003-2015',
       'Zip Codes', 'Community Areas', 'Census Tracts', 'Wards'],
      dtype='object')
'''

def latitude(x= df['Location'][1]):
    str_tup  = x
    tup = eval(str_tup)
    y = tup[0]
    return y


def longitude(x= df['Location'][1]):
    str_tup  = x
    tup = eval(str_tup)
    y = tup[1]
    return y


df['latitude'] =df['Location'].apply(latitude)
df['longitude'] =df['Location'].apply(longitude)

df.to_csv(outfile)