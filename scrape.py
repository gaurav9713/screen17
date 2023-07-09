import requests
from bs4 import BeautifulSoup
import re

def get_urls_to_download(home_url):
    r = requests.get(url=home_url, timeout=2.5)
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')

    anchor_tags = soup.find_all("a")

    pattern = r'https:\/\/d37ci6vzurychx\.cloudfront\.net\/trip-data\/yellow_tripdata_\d{4}-\d{2}\.parquet'

    required_urls = []

    for anchor_tag in anchor_tags:
        match = re.search(pattern, str(anchor_tag))
        if match:
            required_urls.append(match.group())

    return required_urls


