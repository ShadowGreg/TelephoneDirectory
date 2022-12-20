import logging
import os

log_dir = os.path.dirname(__file__) + '/log_dir/'

logging.basicConfig(filename=log_dir + 'app.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s [%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
