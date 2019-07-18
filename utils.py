__author__ = "Mosia Hryhorii (grishamosya@gmail.com)"

import datetime


def run_time(f):
    def wrap():
        print('Start...')
        start = datetime.datetime.now()
        f()
        end = datetime.datetime.now()
        print('End')
        print("Time: ", end - start)
    return wrap


def get_current_datetime(delimiter_time):
    return datetime.datetime.now().\
        strftime(f'%Y.%m.%d_%H{delimiter_time}%M{delimiter_time}%S')