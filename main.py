__author__ = "Hryhorii Mosia (mosia.dev@gmail.com)"

import argparse

from utils import run_time

from scraper import FreeProxyScraper
from db import DB
from settings import SCHEMA_SQLITE, DB_NAME_SQLITE, \
    SCHEMA_MYSQL, USER_MYSQL, PASS_MYSQL, HOST_MYSQL, DB_NAME_MYSQL, LIMIT


def get_args():
    parser = argparse.ArgumentParser(
        'Scraping free proxy list and use '
        'sqlalchemy to save it to database or CSV file')
    parser.add_argument('-db', '--database',
                        help='The database you selected to save proxies.')
    parser.add_argument('-f', '--file',
                        help='The file you selected to save proxies.')
    parser.add_argument('--echo',
                        help='''
                        echo=False: if True, the Engine will log all statements
        as well as a ``repr()`` of their parameter lists to the default log
        handler, which defaults to ``sys.stdout`` for output.
                         ''', default=False)
    args = parser.parse_args()
    return args


@run_time
def main():
    args = get_args()
    scraper = FreeProxyScraper()
    proxies = scraper.scraping()

    echo = True if args.echo == 'yes' else False

    if args.file == 'csv':
        print('Save to CSV file')
        scraper.save_to_csv(proxies)

    if args.database == 'sqlite':
        print('Save to sqlite database')
        db = DB(SCHEMA_SQLITE, db_name=DB_NAME_SQLITE, echo=echo,
                limit=LIMIT,
                which_db='sqlite')
        db.save_to_db(proxies)

    if args.database == 'mysql':
        print('Save to mysql database')
        db = DB(SCHEMA_MYSQL, USER_MYSQL, PASS_MYSQL, HOST_MYSQL, DB_NAME_MYSQL,
                echo=echo, limit=LIMIT, which_db='mysql')
        db.save_to_db(proxies)


if __name__ == '__main__':
    main()
