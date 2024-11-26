#!/usr/bin/env python3
"""
This is a Python example to show how logging library
can be used to log to a file.
"""

import logging

"""
initialize the logger
Logging levels:
https://docs.python.org/3/library/logging.html#logging-levels
logging.NOTSET
logging.DEBUG
logging.INFO
logging.WARNING
logging.ERROR
logging.CRITICAL
"""

logger = logging.getLogger(__name__)
LOG_LEVEL = logging.INFO
CONSOLE_LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def init_logging():
    f = logging.basicConfig(filename=__file__ + ".log", format=LOG_FORMAT, level=LOG_LEVEL)# create console handler and set level to debug
    print(logger.handlers)
    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(CONSOLE_LOG_LEVEL)

    # create formatter
    formatter = logging.Formatter(LOG_FORMAT)

    # add formatter to handlers
    ch.setFormatter(formatter)


    # add ch to logger
    logger.addHandler(ch)


def main():
    init_logging()
    logger.info('Started')

    print("Enter the dividend:")
    dividend = input()

    if dividend.isnumeric():
        print("Now enter the divisor:")
        divisor = input()

        if divisor.isnumeric():
            divide(float(dividend), float(divisor))
        else:
            logger.warning("You must enter a number as the dividend!")
    else:
        log.warning("You must enter a number as the divisor!")

    logger.debug

def divide(dividend, divisor):
    logger.debug("in divide | dividend: %s divisor: %s", dividend, divisor)
    try:
        result = dividend / divisor
        print(f"Result: {result}")
    except ZeroDivisionError:
        logger.exception("Ooops! Divide by zero exception!")


if __name__ == '__main__':
    main()
