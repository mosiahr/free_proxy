__author__ = "Mosia Hryhorii (grishamosya@gmail.com)"

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class FreeProxyScraper:
    def __init__(self, url):
        self.url = url

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
            soup = BeautifulSoup(html, 'lxml')
            rows = soup.find('table', id='proxylisttable').find_all('tr')
            tds = [[td.get_text() for td in row.find_all('td')]
                   for row in rows if row.find_all('td').__len__() > 0]
            return [dict(ip_address=td[0], port=int(td[1]), code=td[2],
                         country=td[3], anonymity=td[4], google=td[5],
                         https=td[6], last_checked=td[7])
                    for td in tqdm(tds)]
        except Exception as e:
            print(e)


