import pandas as pd


df = pd.read_parquet('yellow_tripdata/yellow_tripdata_2023-03.parquet', engine='pyarrow')

print(df.shape)
print(df.head(5))
print(df.columns)