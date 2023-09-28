import logging

logging.basicConfig(filename='test.log',
    level=logging.DEBUG, format= '%(levelname)s%(asctime)s%(message)s')

logger = logging.getLogger()

for i in range(1,20):
    if i%2==0:
        logger.debug("a")
        logger.info("b")
        logger.warning("c")
        logger.error("d")
        logger.critical("e")
        print(i)

#NOTSET,DEBUG,

import logging

name = 'John'

logging.error('%s raised an error', name)