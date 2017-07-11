#!/usr/bin/env python3
import logging
import sys

logging.basicConfig(format='%(message)s', level=logging.DEBUG, stream=sys.stderr)


def get_logger():
    logger = logging.getLogger("default_logger")
    return logger
