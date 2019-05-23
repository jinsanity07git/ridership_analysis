import pandas as pd
import os 

path = 'CTA ridership/'
ls_file = os.listdir(path )

for file in ls_file:
    try: 
        df_iter = pd.read_csv(path+file)
        print('*'*30 + file)
        print(df_iter.columns())
        print(df_iter.describe() )
        print(df_iter.describe(include=['object']))

    except ValueError:
        print ('$'*30 + 'error: ' + file)
# for iter_num, chunk in enumerate(df_iter, 1):
#     print(f'Processing iteration {iter_num}')





df_iter['DAY_TYPE'].unique()



# df_iter.describe(include='all')

