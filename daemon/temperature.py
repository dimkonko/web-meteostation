#!/usr/bin/python

import datetime
import time
import urllib
import urllib2

import Adafruit_DHT as dht


def enable_logging():
    import logging.handlers
    import sys

    # Deafults
    LOG_FILENAME = "/tmp/temperature.log"
    LOG_LEVEL = logging.ERROR  # Could be e.g. "DEBUG" or "WARNING"

    # Give the logger a unique name (good practice)
    logger = logging.getLogger(__name__)
    # Set the log level to LOG_LEVEL
    logger.setLevel(LOG_LEVEL)
    # Make a handler that writes to a file, making a new file at midnight and keeping 3 backups
    handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", backupCount=3)
    # Format each log message like this
    formatter = logging.Formatter('%(asctime)s %(levelname)-2s %(message)s')
    # Attach the formatter to the handler
    handler.setFormatter(formatter)
    # Attach the handler to the logger
    logger.addHandler(handler)

    # Make a class we can use to capture stdout and sterr in the log
    class MyLogger(object):
        def __init__(self, loggerObj, level):
            """Needs a logger and a logger level."""
            self.logger = loggerObj
            self.level = level

        def write(self, message):
            # Only log if there is a message (not just a new line)
            if message.rstrip() != "":
                self.logger.log(self.level, message.rstrip())

    # Replace stdout with logging to file at INFO level
    sys.stdout = MyLogger(logger, logging.INFO)
    # Replace stderr with logging to file at ERROR level
    sys.stderr = MyLogger(logger, logging.ERROR)

    return logger


DELAY_SECONDS = 30
logger = enable_logging()


def send_request(t, h):
    url = 'http://dimkonko.pythonanywhere.com/add_data'
    values = {
        't': t,
        'h': h
    }
    logger.info('Sending data to %s with values: %s' % (url, str(values)))
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    # TODO: Handle response data?
    # response = urllib2.urlopen(req).read()
    urllib2.urlopen(req).read()


while True:
    try:
        h, t = dht.read_retry(dht.DHT11, 4)
        cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        send_request(t, h)
    except Exception as ex:
        logger.error(ex.message)
    finally:
        time.sleep(DELAY_SECONDS)
