import requests
import html2text
from bs4 import BeautifulSoup
import os
import time

def get_text_from_url(url):
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text)
    title = soup.find("title")
    h = html2text.HTML2Text()
    h.ignore_links = True
    contents = h.handle(res.text)
    return (title.text, contents)

def save_contents(title, contents, original_service_id):
    if not os.path.exists(f'data_{original_service_id}'):
        os.mkdir(f'data_{original_service_id}')
    f = open(f'data_{original_service_id}/{title}.txt', 'w')
    f.write(contents)
    f.close
