__author__ = "Hryhorii Mosia (mosia.dev@gmail.com)"

import csv
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from settings import FILE_NAME

URL = 'https://free-proxy-list.net/'


class FreeProxyScraper:
    def __init__(self, url=URL, file_name=FILE_NAME):
        self.url = url
        self.file_name = file_name

    def get_html(self, url=None, timeout=10):
        try:
            response = requests.get(url or self.url, timeout=timeout)

            if response.status_code == 200:
                return response.text
        except requests.exceptions.RequestException as e:
            print(e)

    def scraping(self):
        print('Proxy scraping...')
        try:
            html = self.get_html()
            soup = BeautifulSoup(html, 'html.parser')
            rows = soup.find('table', id='proxylisttable').find_all('tr')
            tds = [[td.get_text() for td in row.find_all('td')]
                   for row in rows if row.find_all('td').__len__() > 0]
            return [dict(ip_address=td[0], port=int(td[1]), code=td[2],
                         country=td[3], anonymity=td[4], google=td[5],
                         https=td[6], last_checked=td[7])
                    for td in tqdm(tds)]
        except Exception as e:
            print(e)

    def save_to_csv(self, data):
        with open(self.file_name, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(('IP Address', 'Port', 'Code', 'Country',
                            'Anonymity', 'Google', 'Https', 'Last Checked'))

            for item in data:
                row = (
                    item['ip_address'],
                    item['port'],
                    item['code'],
                    item['country'],
                    item['anonymity'],
                    item['google'],
                    item['https'],
                    item['last_checked'],
                )
                writer.writerow(row)
