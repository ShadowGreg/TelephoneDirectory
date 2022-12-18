import datetime
import yaml
from exception import logging

log_dir = './log_dir/'


# with open('registr_info.yaml', 'r') as f:
#     comment = yaml.safe_load(f)
#     print(comment['descr']['search']['desciption'])


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

# log_info('',  comment['descr']['add_contact']['desciption'])
