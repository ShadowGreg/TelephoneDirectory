import datetime
import time
from exception import logging
import yaml
import os

log_dir = './log_dir/'
root_dir = './'
try:
    with open(root_dir+'reg_info.yaml', 'r') as f:
          comment = yaml.safe_load(f)
except yaml.YAMLError as e:
    print('Error while opening YAML file' + str(e))


    
print(comment['descr']['search']['desciption'])
def registretion_info():
    pass

def log_info(st: str, fname ):
    log_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_time = datetime.datetime.now().strftime("%H_%M")
    try:
        with open(log_dir+'log_'+log_date+'.log', 'rw') as f:
             f.write(f'{log_date}:{log_time} :[{fname}] : {st}\n')
    except Exception as e:
        logging.debug(e)
 
    
log_info('',  comment['descr']['add_contact']['desciption'])