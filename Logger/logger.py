# importing module
import logging

# Create and configure logger
logging.basicConfig(#filename="newfile.log",
                    level=logging.NOTSET,
                    #filemode='w',
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Creating an object
logger = logging.getLogger()

# Test messages
a=10+15
logger.debug(f"a values is {a}")
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

#NOTSET<DEBUG<INFo<WARNING<ERROR<CRITICAL


import logging

logging.basicConfig(filename='logfile.log',filemode='w',
                    level='DEBUG',
                    format= '%(asctime)s%(levelname)s%(message)s%(user_id)s')
logger = logging.getLogger()
#NDIWEC
logger.debug("this is debug")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")
logger.critical("this is critical")