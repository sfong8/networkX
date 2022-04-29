import pandas as pd
df1 = pd.read_csv(r'./data/yellow_tripdata_2021-01.csv')
import os
df= pd.DataFrame()
for filename in os.listdir('./data/'):
    if filename.startswith('yellow_tripdata_2021'):
        temp=pd.read_csv(fr'./data/{filename}')
        df=pd.concat([df,temp])
##distinct ratecode

df['RatecodeID'].value_counts()

##standard rates only
df = df[df['RatecodeID']==1]

##crete a column for trip duration
df['tpep_pickup_datetime_dt'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime_dt'] = pd.to_datetime(df['tpep_dropoff_datetime'])

df['duration'] = df['tpep_dropoff_datetime_dt'] -df['tpep_pickup_datetime_dt']

df['duration'] =df['duration'].apply(lambda x:x.seconds/60)
df['hour'] = df['tpep_pickup_datetime_dt'].apply(lambda x:x.hour)
df['amount'] = df['total_amount'] - df['tip_amount']
from matplotlib import pyplot as plt
df=df[df['amount']>0]
df=df[df['trip_distance']>0]
df2 = df[df['duration']<180]
df3 = df2.sort_values(['tip_amount'],ascending=False)

columns_take = ['duration','amount','trip_distance','PULocationID','DOLocationID']
df2=df2[columns_take]

df2=df2[df2['PULocationID']!=df2['DOLocationID']]

df3=df2[(df2['PULocationID']!=265) & (df2['DOLocationID']!=265) ]
df3=df3[(df3['PULocationID']!=264) & (df3['DOLocationID']!=264) ]
df3['count']=1
df3_grouped = df3.groupby(['PULocationID','DOLocationID']).mean().reset_index()
df3_grouped2 = df3.groupby(['PULocationID','DOLocationID']).agg({'amount':'mean', 'duration':'mean','count':'sum','trip_distance':'mean'}).reset_index()
df3_grouped2=df3_grouped2[df3_grouped2['count']>100 ]

df3_grouped2.to_parquet('combined_processed.parquet')