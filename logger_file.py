import datetime
import time
from exception import logging
import yaml


def log_info(st: str):
    date = datetime.datetime.now().strftime("%Y, %m, %d, %H:%M")
    try:
        with open('log.txt', 'a') as f:
            f.writelines(f'{date} : {st}')
    except Exception as e:
        logging.debug(e)

with open('registr_info.yaml', 'r') as f:
    comment = yaml.safe_load(f)
    print(comment)
def registretion_info():
    pass