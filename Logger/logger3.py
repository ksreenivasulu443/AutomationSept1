import logging

logging.basicConfig(filename='logfile123.log', filemode='w',
                    format=('%(asctime)s%(levelname)s%(message)s'),
                    level=10)

# default  level='WARNING'

logger = logging.getLogger()
print("this is logger code")
logger.debug("this is debug")
logger.info(" this is information that site is working fine")
logger.warning("this is warning")
for i in range(1,1000):
    print(i)
logger.error("this is error")
for i in range(1,1000):
    print(i)
logger.critical("this is critical")
for i in range(1,1000):
    print(i)
logger.warning(" server is getting i/p to restart")
for i in range(1,1000):
    print(i)
logger.info(" server restarted")

logger.debug("this is second debug")
logger.critical("this 3rd critical")

logger.debug("this is second debug")
logger.debug("this is second debug")
logger.debug("this is second debug")
logger.debug("this is second debug")


# NOTSET -0
# DEBUG -10
# INFO 20
# Warning 30
# error 40
# critical 50