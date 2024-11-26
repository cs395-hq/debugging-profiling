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
LOG_LEVEL = logging.DEBUG

def init_logging():
    logger.debug("in main")
    logging.basicConfig(filename=__file__ + ".log", level=logging.DEBUG)

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
