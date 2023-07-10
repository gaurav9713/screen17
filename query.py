from download import download_file
from scrape import get_urls_to_download
import pandas as pd
import os
import glob

url = 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'

urls_to_download = get_urls_to_download(url)

folder = 'yellow_tripdata_trip_average'
os.mkdir(folder)

def download_month_file():
    month = int(input("Choose a month between 1-12: "))
    year = int(input("Choose a year between 2010-2023: "))

    if month < 10:
        url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-0{month}.parquet'
    else:
        url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month}.parquet'

    if url in urls_to_download:
        print('URL Found!')
        download_file(url=url, folder_name=folder)
        print('File downloaded!')
    else:
        print('URL not found for the month an year')



def calc_avg():
    download_month_file()
    file_paths = glob.glob(os.path.join(folder, '*'))
    for file in file_paths:
        df = pd.read_parquet(file, engine='pyarrow')

        print(f'Average total_amount for the selected month and year are: ${round(df["trip_distance"].mean(),2)}')

        os.remove(file)

    os.rmdir(folder)

calc_avg()