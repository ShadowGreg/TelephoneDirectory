import logging

logging.basicConfig(filename='app.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s [%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
