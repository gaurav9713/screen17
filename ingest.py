import pandas as pd
import sqlalchemy
import os 
import glob
from dotenv import dotenv_values
import threading
from urllib.parse import quote

env = dotenv_values('.env')

db_username = env['DB_USERNAME']
db_password = env['DB_PASSWORD']
db_host = env['DB_HOST']
db_name = env['DB_NAME']
db_port = env['DB_PORT']


def ingest_data(df_chunk):
    try:
        engine = sqlalchemy.create_engine(db_connection_string)
        df_chunk.to_sql('yellow_trip', engine, if_exists='append', index=False)

        print('Data ingestion successful')
    except Exception as e:
        print(f'Error ingesting data: {e}')
        

def create_chunks(file_name):
    num_threads = 4
    chunk_size = 10000
    file_name = str(file_name).replace('\\','/')
    df = pd.read_parquet(file_name, engine='pyarrow')
    df_chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]

    return df_chunks

if '__name__' == '__main__':
    db_connection_string = f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
    engine = sqlalchemy.create_engine(db_connection_string)

    folder_path = 'yellow_tripdata'

    file_paths = glob.glob(os.path.join(folder_path, '*'))

    threads = []
    for file in file_paths:
        chunks = create_chunks(file)
        for chunk in chunks:
            process_thread = threading.Thread(
                target=ingest_data,
                args=(chunk,)
            )
            threads.append(process_thread)
            process_thread.start()

    for thread in threads:
        thread.join()

    for file in file_paths:
        os.remove(file)
    os.rmdir(folder_path)

