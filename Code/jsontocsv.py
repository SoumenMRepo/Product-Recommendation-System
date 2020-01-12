# Convert json dataset t csv format
import json
import csv
import pandas as pd
with open ('MusicalDataset.json','r') as f:
        data=f.readlines()
        data=map(lambda x: x.rstrip(),data)
        data_json_str= "[" + ','.join(data) + "]"
        data_df=pd.read_json(data_json_str)
data_df.to_csv('MusicalDataset.csv', index=False)

