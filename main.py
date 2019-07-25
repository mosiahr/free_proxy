__author__ = "Mosia Hryhorii (grishamosya@gmail.com)"

from utils import run_time

from scraper import FreeProxyScraper
from db import DB
from settings import URL, SCHEMA, USER, PASS, HOST, DB_NAME, LIMIT


@run_time
def main():
    scrap_rez = FreeProxyScraper(URL).scraping()
    db = DB(SCHEMA, USER, PASS, HOST, DB_NAME, echo=False, limit=LIMIT)
    db.save_to_db(scrap_rez)
    proxies = db.get_proxy()
    print(proxies[-1].ip_address, proxies[-1].port)


if __name__ == '__main__':
    main()
