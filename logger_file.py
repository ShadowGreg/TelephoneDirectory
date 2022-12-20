import datetime
import yaml
from exception import logging

log_dir = './log_dir/'


def registretion_info():
    pass


def log_info(st: str, fname):
    log_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_time = datetime.datetime.now().strftime("%H_%M")
    try:
        with open(log_dir + 'log_' + log_date + '.log', 'a') as f:
            f.write(f'{log_date}:{log_time} :[{fname}] : {st}\n')
    except Exception as e:
        logging.debug(e)
