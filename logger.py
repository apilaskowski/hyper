#!/usr/bin/env python3
import logging

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


def get_logger():
    logger = logging.getLogger("default_logger")
    return logger
