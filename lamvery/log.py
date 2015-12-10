# -*- coding: utf-8 -*-

import logging
import sys
from termcolor import colored

class ColoredStreamHandler(logging.StreamHandler):

    def format(self, record):
        message = super(ColoredStreamHandler, self).format(record)
        if record.levelno == logging.INFO:
            message = colored(message, 'green')
        elif record.levelno == logging.WARN:
            message = colored(message, 'yellow')
        return message

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = ColoredStreamHandler(stream=sys.stderr)
    handler.setLevel(logging.INFO)
    handler.setFormatter(
        logging.Formatter('%(name)s: %(message)s'))
    logger.addHandler(handler)
    return logger