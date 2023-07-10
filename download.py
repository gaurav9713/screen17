from scrape import get_urls_to_download
import pandas as pd
import threading
import os
import requests
import re

url = 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'

urls_to_download = get_urls_to_download(url)

print(f"Total files for Yellow Taxi that can be downloaded are: {len(urls_to_download)}")

#Since I am devloping this on my local machine and not on cloud, I will be only considering 10 latest URLs to download

def download_file(url, folder_name):
    file_pattern = r'yellow_tripdata_\d{4}-\d{2}\.parquet'
    file_name = re.search(file_pattern, url).group()
    file_request = requests.get(url)
    with open(os.path.join(folder_name, file_name), 'wb') as f:
        f.write(file_request.content)

if __name__ == '__main__':
    folder = 'yellow_tripdata'
    os.mkdir(folder)

    for url in urls_to_download[:5]:
        
        process_thread = threading.Thread(
            target=download_file,
            args=(url, folder)
        )
        process_thread.start()

    print('File download complete!')
    # download_file(urls_to_download, 'downloaded_files')