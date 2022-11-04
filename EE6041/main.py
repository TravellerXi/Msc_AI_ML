import csv
import pandas as pd
df=pd.read_csv('code.csv')


for i in df['ROUTING KEY']:
    print(i)
